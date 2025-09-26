import os
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.llms.gemini import Gemini

from llama_index.embeddings.huggingface import HuggingFaceEmbedding


load_dotenv()

def main(folder_path: str) -> None:
    # load data from webpage
    print(f"loading data from the {folder_path}")
    document = SimpleDirectoryReader(folder_path).load_data()

    # huggingface embedding
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # create vector index
    index = VectorStoreIndex.from_documents(documents=document, embed_model=embed_model)

    # use gemini
    llm = Gemini(
        model = os.getenv("LLM_MODEL", "gemini-2.5-flash"),
        api_key=os.getenv("GEMINI_API_KEY")
    )
    query_engine = index.as_query_engine(llm=llm)

    print("\n Ready! Type your queries (or 'exit' to quit).")
    while True:
        query = input("query: ")
        if query.lower() == "exit":
            print("exiting...")
            break
        response = query_engine.query(query)
        print("\nAnswer: ", response, "\n")

if __name__ == "__main__":
    folder_path: str = input("folder_path: ")
    main(folder_path)










