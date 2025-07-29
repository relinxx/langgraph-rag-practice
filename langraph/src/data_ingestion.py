import config 
import os 
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import UnstructuredXMLLoader
#from langchain_community.document_loaders import UnstructuredImageLoader
from config import CHUNK_SIZE, CHUNK_OVERLAP
from transformers import AutoTokenizer
from langchain.text_splitter import CharacterTextSplitter

class Text_Extractor:

    

    
    def get_file_extension(file_path):
        return os.path.splitext(file_path)[1].lower()
    
    def doc_processor(file_path, self):



        # docs = []
        # extension = self.get_file_extension(file_path)
        
        # if extension == ".docx":
        #     docx_loader = Docx2txtLoader(file_path=/home/relinxx/Documents/langgraph_integrated_rag_wm/langraph/src/data/)
        #     doc = docx_loader.load()
        # elif extension == ".xlsx":
        #     xlsxLoader = UnstructuredXMLLoader.load(file_path)
        # elif extension == ".csv":
        #     csvLoader = CSVLoader.load(file_path)
        # elif extension == ".png":
        #     png_loader = UnstructuredImageLoader.load(file_path)
        # elif extension == ".jpg":
        #     jpg_loader = UnstructuredImageLoader.load(file_path)
