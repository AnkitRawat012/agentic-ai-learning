
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# pyrefly: ignore [missing-import]
from google import genai

# pyrefly: ignore [missing-import]
import chromadb

load_dotenv()

client=genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name='practice_documents')


collection.add(
    documents=[
        "Paris is the capital city of France.",
        "Tokyo is the capital city of Japan.",
        "The blue whale is the largest animal on Earth.",
        "Cheetahs are the fastest land animals.",
        "Pizza originated in Italy, specifically in Naples.",
        "Sushi is a traditional Japanese dish made with rice and fish.",
        "The Great Barrier Reef is located in Australia.",
        "Mount Kilimanjaro is the highest mountain in Africa.",

    ],
    ids=["d1","d2","d3","d4","d5","d6","d7","d8"]

)

def ask_rag(question):
    """Complete RAG Pipeline - retrieval + generation"""
    results = collection.query(query_texts=[question], n_results=2)
    retrieved_docs = results['documents'][0]
    context = "\n".join(retrieved_docs)

    prompt = f"""Answert the questions using only the following context.

    Context={context}
    Question = {question}
    """

    response = client.models.generate_content(
        model = "gemini-flash-lite-latest",
        contents= prompt
    )

    print(f"Q: {question}")
    print(f"Retrieved: {retrieved_docs}")
    print(f"A: {response.text}")
    print("-" * 50)




ask_rag("What is the land animal ?")
ask_rag("What is the capital of France ?")
ask_rag("what food is famous in Japan ?")
ask_rag("Where is Mount Kilimanjaro?")
ask_rag("Which is the largest animal?")