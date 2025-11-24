from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api = os.getenv("GEMINI_API_KEY")

if not gemini_api:
    raise ValueError("gemini_api不存在，请检查.env文件")

client = genai.Client(api_key=gemini_api)


def get_advise(city: str, weather_data: dict) -> str | None:
    """将天气数据发给Gemini并返回穿衣/出行建议"""
    prompt = (
        f"我现在在 {city}，当前天气数据如下：\n{weather_data}\n"
        "请根据这些数据，用幽默风趣的语气，给我尽量简短的穿衣建议和出行提示控制在几句话内。"
        "尽量输出text文本，而不是markdown"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        return response.text
    except ValueError as e:
        return f"AI 大脑暂时短路了: {e}"
