from llama_index.llms.openai import OpenAI
import llama_index.readers.web as web
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv

load_dotenv()


def main(url: str) -> None:
    document = web.SimpleWebPageReader(html_to_text=True).load_data([url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is the history of genai?")
    print(response)

if __name__ == "__main__":
    main(url="https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-1-introduction-to-ai-eadb5a71f07d")



