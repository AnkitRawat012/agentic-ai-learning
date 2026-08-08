import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    fake_weather_data = {
        "delhi": "35°C, sunny",
        "mumbai": "30°C, humid",
        "london": "18°C, cloudy"
    }
    return fake_weather_data.get(city.lower(), "Weather data not available")

def calculate(expression: str) -> str:
    """Evaluate a simple math expression, e.g.  '25*4' or '100/5'."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"
# Test 1
response1 = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="What's the weather like in Delhi right now?",
    config={"tools": [get_weather]}
)
print("Test 1:", response1.text)

# Test 2
response2 = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="What's the weather in Mumbai and London?",
    config={"tools": [get_weather]}
)
print("Test 2:", response2.text)

# Test 3
response3 = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="What's the weather in Paris?",
    config={"tools": [get_weather]}
)
print("Test 3:", response3.text)



response4 = client.models.generate_content(
    model = "gemini-flash-lite-latest",
    contents="What's 45 times 12 ? Also , what's the weature in Mumbai?",
    config={"tools": [get_weather,calculate]}
)

print("Test 4:",response4.text)