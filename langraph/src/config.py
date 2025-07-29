import os 
from transformers import AutoTokenizer

CHUNK_SIZE = 512
CHUNK_OVERLAP = 64


#llama3 8b tokenizer
TOKENIZER = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")

