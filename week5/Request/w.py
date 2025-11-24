import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

weather_api = os.getenv("WEATHER_API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather" # API端点

# API参数
param = {
    "q": "Shanghai",
    "appid": weather_api,
    "units": "metric",
}

response = requests.get(url, params=param)  # 发送请求

if response.status_code == 200:
    print("请求成功：")

    data = response.json()
    main = json.dumps(data, indent=2)

    print(main)
else:
    print("请求失败")