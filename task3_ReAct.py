# import os
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types

# load_dotenv()
# client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# # Tool define karo (same jo pehle kiya tha)
# def get_weather(city: str) -> str:
#     """Get the current weather for a given city."""
#     fake_weather_data = {
#         "delhi": "35°C, sunny",
#         "mumbai": "30°C, humid",
#         "london": "18°C, cloudy"
#     }
#     return fake_weather_data.get(city.lower(), "Weather data not available")

# # Conversation shuru karo
# contents = [
#     types.Content(role="user", parts=[types.Part(text="What's the weather in Delhi?")])
# ]

# print("=" * 50)
# print("STEP 1: User ka sawaal bheja")
# print("=" * 50)

# # Model ko bhejo - iska tool available hai
# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents=contents,
#     config={
#         "tools": [get_weather],
#         "automatic_function_calling": {"disable": True}  # Manual control ke liye
#     }
# )

# print("STEP 2: Model ka response aaya")
# print("-" * 50)

# # Dekho model ne kya bola - text ya function call?
# part = response.candidates[0].content.parts[0]

# if part.function_call:
#     print(f"Model ACT kar raha hai: {part.function_call.name}")
#     print(f"Arguments: {dict(part.function_call.args)}")
# else:
#     print(f"Model seedha jawab de raha hai: {part.text}")







# if part.function_call:
#     print(f"Model ACT kar raha hai: {part.function_call.name}")
#     print(f"Arguments: {dict(part.function_call.args)}")
    
#     print()
#     print("=" * 50)
#     print("STEP 3: Hum khud function ko chalate hain (OBSERVE)")
#     print("=" * 50)
    
#     # Function ka naam match karke usse call karo
#     if part.function_call.name == "get_weather":
#         result = get_weather(**part.function_call.args)
    
#     print(f"Function ka result: {result}")
    
#     print()
#     print("=" * 50)
#     print("STEP 4: Result wapas model ko bhejo, final answer maango")
#     print("=" * 50)
    
#     # Conversation history mein model ka function call add karo
#     contents.append(response.candidates[0].content)
    
#     # Function ka result bhi add karo (as a "function response")
#     function_response_part = types.Part.from_function_response(
#         name="get_weather",
#         response={"result": result}
#     )
#     contents.append(types.Content(role="user", parts=[function_response_part]))
    
#     # Ab model ko dobara call karo - is baar final answer ke liye
#     final_response = client.models.generate_content(
#         model="gemini-flash-lite-latest",
#         contents=contents,
#         config={"tools": [get_weather]}
#     )
    
#     print(f"FINAL ANSWER: {final_response.text}")

# else:
#     print(f"Model seedha jawab de raha hai: {part.text}")













import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from google import genai
# pyrefly: ignore [missing-import]
from google.genai import types

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

contents = [
    types.Content(role="user", parts=[types.Part(text="What's the weather in Delhi?")])
]

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=contents,
    config={
        "tools": [get_weather],
        "automatic_function_calling": {"disable": True}
    }
)

part = response.candidates[0].content.parts[0]

if part.function_call:
    print(f"Model ACT kar raha hai: {part.function_call.name}")
    print(f"Arguments: {dict(part.function_call.args)}")
    
    result = get_weather(**part.function_call.args)
    print(f"Function ka result: {result}")
    
    contents.append(response.candidates[0].content)
    
    function_response_part = types.Part.from_function_response(
        name="get_weather",
        response={"result": result}
    )
    contents.append(types.Content(role="user", parts=[function_response_part]))
    
    final_response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=contents,
        config={"tools": [get_weather]}
    )
    
    print(f"FINAL ANSWER: {final_response.text}")