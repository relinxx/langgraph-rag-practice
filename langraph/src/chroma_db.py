import os
from langchain_chroma import Chroma
from embedder import embedding_model

vector_store = Chroma(
    collection_name="collection_1",
    embedding_function=embedding_model,
    persist_directory=os.path.join(os.path.dirname(__file__), "..", "data", "chroma_db"),
)

