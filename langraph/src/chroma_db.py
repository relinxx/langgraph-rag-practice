import os
from langchain_chroma import Chroma
from embedder import embedding_model
from data_ingestion import Text_Extractor

vector_store = Chroma(
    collection_name="collection_1",
    embedding_function=embedding_model,
    persist_directory=os.path.join(os.path.dirname(__file__), "..", "data", "chroma_db"),
)


all_docs = Text_Extractor.doc_processor()

document_ids = vector_store.add_documents(Text_Extractor.all_docs)
print(document_ids[:2])