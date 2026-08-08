# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client=genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# chat = client.chats.create(model="gemini-flash-latest")


# response1 = chat.send_message("My name is Ankit.")
# print("Response 1:", response1.text)

# response2 = chat.send_message("What's my name?")
# print("Response 2:" , response2.text)



import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
chat = client.chats.create(model="gemini-flash-lite-latest")

response1 = chat.send_message("My name is Manthan.")
print("Response 1:", response1.text)

response2 = chat.send_message("what's my name")
print("Response 2:", response2.text)