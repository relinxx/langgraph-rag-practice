import os 
from transformers import AutoTokenizer

#embedding model that will be used to store chunks in chromadb
EMBEDDING_MODEL = "all-MiniLM-L8-v2"


CHUNK_SIZE = 512
CHUNK_OVERLAP = 64


#llama3 8b tokenizer
TOKENIZER = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")

