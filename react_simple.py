
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from google import genai
# pyrefly: ignore [missing-import]
from google.genai import types




load_dotenv()
client = genai.Client(api_key = os.environ["GOOGLE_API_KEY"])


def get_weather(city:str) -> str:
    """Get current weather of the city . """
    return "35°C, sunny"


question = "What's the Weather in Delhi ?"



response = client.models.generate_content(
    model = "gemini-flash-lite-latest",
    contents = question,
    config={
        "tools":[get_weather],
        "automatic_function_calling": {"disable":True}
    }
)

# print(response)


part = response.candidates[0].content.parts[0]

print("--------")
print("Function name: ", part.function_call.name)
print("Function args:", part.function_call.args)



city_asked = part.function_call.args["city"]
result = get_weather(city_asked)

print()
print("---------")
print(result)



content_updated = [
    types.Content(role="user",parts = [types.Part(text=question)]),
    response.candidates[0].content,
    types.Content(role="user" , parts=[
       types.Part.from_function_response(
        name= "get_weather",
        response={"result":result}
       )
    ])

]


final_response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=content_updated,
    config={"tools":[get_weather]}
)
print()
print("---------Final Answer")
print(final_response.text)