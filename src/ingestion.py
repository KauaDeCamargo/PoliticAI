from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

pasta = Path("planos_governo")

documents = []

for file in pasta.glob('*.pdf'):
    candidato = file.stem

    pdf_documents = PyPDFLoader(file).load()

    for document in pdf_documents:
        document.metadata['candidato'] = candidato
        documents.append(document)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

docs_splitted = text_splitter.split_documents(documents)

persist_directory = './vectorstore'
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

vector_store = Chroma.from_documents(
    documents=docs_splitted, 
    embedding=embeddings, 
    persist_directory=persist_directory
)