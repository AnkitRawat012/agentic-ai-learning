# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()  # reads .env file
# client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# response = client.models.generate_content(
#     model="gemini-flash-latest",
#     contents="Explain what an API is , in 2 sentences."
# )


# print(response.text)

# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents="Explain what is Machine Learning , in 2 sentences."
# )

# print(response.text)
















# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# client= genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# response = client.models.generate_content(
#     model= "gemini-flash-lite-latest",
#     contents= "What is Ai and how they affect the jobs ? in 2 sentences"
# )

# print(response.text)


import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

intraction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how Ai is work in few words."
)

print(intraction.output_text)