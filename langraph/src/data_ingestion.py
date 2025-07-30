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
    
    @staticmethod
    def doc_processor():

        directory = "/home/relinxx/Documents/langgraph_integrated_rag_wm/langraph/src/data/"

        pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
        docx_files = [f for f in os.listdir(directory) if f.endswith('.docx')]
        xlsx_files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]
        csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

        loaded_pdfs = []
        for file_path in pdf_files:
            loader = PyPDFLoader(os.path.join(directory, file_path))
            loaded_pdfs.extend(loader.load())

        loaded_docx = []
        for file_path in docx_files:
            loader = Docx2txtLoader(os.path.join(directory, file_path))
            loaded_docx.extend(loader.load())

        loaded_xlsx = []
        for file_path in xlsx_files:
            loader = UnstructuredXMLLoader(os.path.join(directory, file_path))
            loaded_xlsx.extend(loader.load())

        loaded_csv = []
        for file_path in csv_files:
            loader = CSVLoader(os.path.join(directory, file_path))
            loaded_csv.extend(loader.load())

        text_splitter = RecursiveCharacterTextSplitter(CHUNK_SIZE, CHUNK_OVERLAP, add_start_index=True)

        pdf_splits = text_splitter.split_documents(loaded_pdfs)

        csv_splits = text_splitter.split_documents(loaded_csv)
            
        xlsx_splits = text_splitter.split_documents(loaded_xlsx)
            
        docx_splits = text_splitter.split_documents(loaded_docx)

        all_doc_splits = docx_splits + csv_splits + pdf_splits + xlsx_splits
        
        Text_Extractor.all_docs = all_doc_splits
        return all_doc_splits




        #     docx_splits = []
        # for doc in loaded_docx:
        #     docx_splits.extend(text_splitter.split_documents(doc))
            
        

        
        













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
