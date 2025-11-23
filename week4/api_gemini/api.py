from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_gemini = os.getenv("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=api_gemini)

with open("input.txt", encoding="utf-8") as file:
    input_context = file.read().strip()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=input_context
)

with open("env.md", "w", encoding="utf-8") as file:
    file.write(str(response.text))
