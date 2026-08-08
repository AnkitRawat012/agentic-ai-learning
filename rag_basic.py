import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv;
# pyrefly: ignore [missing-import]
from google import genai
# pyrefly: ignore [missing-import]
import chromadb

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])



chroma_client = chromadb.Client()


collection = chroma_client.create_collection(name="my_documents")

collection.add(
    documents=[
        "Paris is the capital city of France. The Eiffel Tower is also located there.",
        "Mount Everest is the tallest mountain in the world.",
        "Python is a popular programming language for AI.",
        "The Great Wall of China is visible from space, though this is debated.",
    ],
    ids=["id1", "id2", "id3", "id4"],
)

user_question = "What is the capital of France ?"

result = collection.query(
    query_texts=[user_question],
    n_results=2
)

retrieved_docs = result["documents"][0]
print("Retrieved Context", retrieved_docs)


context = "\n".join(retrieved_docs)
prompt = f"""Answer the following question using only the context provided. if the context doesn't contain the answer, then say 'Cannot answer based on the given context.'

Context:{context}

Question:{user_question}
"""

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=prompt
)


print("\n Final Answer" , response.text)