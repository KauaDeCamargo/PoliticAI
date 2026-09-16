from pathlib import Path
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    persist_directory='./vectorstore',
    embedding_function=embeddings
)

@tool
def search_document(pergunta: str) -> str:
    """
    Essa ferramenta busca informações no documento carregado.

    Use sempre que o usuário fizer perguntas relacionadas a propostas/planos de governo dos candidatos a presidência do Brasil em 2026.

    Args:
        pergunta (str): Pergunta do usuário que indica quais informações devem ser buscadas nos documentos.
    """

    docs = vector_store.similarity_search(
        query=pergunta,
        k=5
    )

    response = '\n\n'.join(
        f'Fonte: {doc.metadata}\nConteúdo: {doc.page_content}' for doc in docs
    )

    return response