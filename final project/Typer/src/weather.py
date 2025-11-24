import os
import requests
from dotenv import load_dotenv

load_dotenv()
weather_api = os.getenv("WEATHER_API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather"  # API端点


def fetch_city_data(url: str, params: dict[str, str], city: str):
    """负责底层的网络请求和异常处理"""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # 使用内置的方法主动检测状态码
        return response
    except requests.exceptions.HTTPError as e:
        # 从异常对象获取状态码，而不是依赖可能未定义的response变量
        if e.response is not None:
            code = e.response.status_code
            if code == 404:
                raise ValueError(f"Error: City '{city}' not found.") from e
            elif code >= 500:
                raise RuntimeError(f"Remote server error {code}") from e
            else:
                raise RuntimeError(f"The API request was rejected: {code}") from e
        else:
            raise RuntimeError("HTTP error occurred but no response available") from e

    except requests.exceptions.Timeout as e:
        raise RuntimeError(
            "The request has timed out. Please check the network status"
        ) from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError("An unknown error occurred in the network connection") from e


def load_weather(city: str) -> dict:
    """构建参数和解析数据"""
    if not weather_api:
        raise RuntimeError(f"未找到weather_api，请检查.env文件")

    params = {
        "q": city,
        "appid": weather_api,
        "units": "metric",
    }

    response = fetch_city_data(url, params, city)

    data = response.json()

    weather_info = {
        "Main": data["weather"][0]["main"],
        "Description": data["weather"][0]["description"],
        "Temp": data["main"]["temp"],
        "Max_temp": data["main"]["temp_max"],
        "Min_temp": data["main"]["temp_min"],
        "Humidity": data["main"]["humidity"],
    }

    return weather_info
