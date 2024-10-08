from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
import sys

load_dotenv()

def main(url: str) -> None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("Has Sagar worked in  a company called Smollan and what has he worked on at that company?")
    print(response)

if __name__ == "__main__":
    
    main(url = 'data')