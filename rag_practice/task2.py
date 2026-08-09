import os
from dotenv import load_dotenv
from google import genai
import chromadb

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="practice_docs_t2")

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
    ids=["doc1", "doc2", "doc3", "doc4", "doc5", "doc6", "doc7", "doc8"]

)

def ask_rag(question , n_results=3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )
    retrieved_docs = results['documents'][0]

    distances = results['distances'][0]

    context = "\n".join(retrieved_docs)

    prompt = f"""Answer the following question based on the context below. If the answer is not contained within the context, say "I don't know".
    Context: {context}
    Question: {question}
    """

    response = client.models.generate_content(
        model = "gemini-flash-lite-latest",
        contents = prompt
    )

    print(f"Question: {question}")
    for doc , dist in zip(retrieved_docs , distances):
        print(f"Distance: {dist:.4f}-> {doc}")
    print(f"Answer: {response.text}")
    print("-"*50)

print("=== n_reuslts = 1 ===")
ask_rag("What is the fastest land animal ? ", n_results=1)

print("=== n_reuslts = 3 ===")
ask_rag("What is the fastest land animal ? ", n_results=3)

print("=== n_reuslts = 5 ===")
ask_rag("What is the fastest land animal ? ", n_results=5)



print("=== n_reuslts = 8 ===")
ask_rag("what is the quantum physics ? ", n_results=8)


