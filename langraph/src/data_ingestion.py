import config 
import os 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import UnstructuredXMLLoader
#from langchain_community.document_loaders import UnstructuredImageLoader
from config import CHUNK_SIZE, CHUNK_OVERLAP
from transformers import AutoTokenizer
from langchain.text_splitter import CharacterTextSplitter

class Text_Extractor:
    
    def doc_processor():

        directory = "/home/relinxx/Documents/langgraph_integrated_rag_wm/langraph/src/data/"

        pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
        docx_files = [f for f in os.listdir(directory) if f.endswith('.docx')]
        xlsx_files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]
        csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

        loaded_pdfs = []
        for file_path in pdf_files:
            loader = PyPDFLoader(file_path)
            loaded_pdfs.extend(loader.load())

        loaded_docx = []
        for file_path in docx_files:
            loader = Docx2txtLoader(file_path)
            loaded_docx.extend(loader.load())

        loaded_xlsx = []
        for file_path in xlsx_files:
            loader = UnstructuredXMLLoader(file_path)
            loaded_xlsx.extend(loader.load())

        loaded_csv = []
        for file_path in csv_files:
            loader = CSVLoader(file_path)
            loaded_csv.extend(loader.load())

        text_splitter = RecursiveCharacterTextSplitter(CHUNK_SIZE, CHUNK_OVERLAP, add_start_index=True)

        pdf_splits = []
        for pdf in loaded_pdfs:
            pdf_splits.extend(text_splitter.split_documents(pdf))

        csv_splits = []
        for csv in loaded_csv:
            csv_splits.extend(text_splitter.split_documents(csv))
            
        xlsx_splits = []
        for xl in loaded_xlsx:
            xlsx_splits.extend(text_splitter.split_documents(xl))
            
        docx_splits = []
        for doc in loaded_docx:
            docx_splits.extend(text_splitter.split_documents(doc))
            


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
