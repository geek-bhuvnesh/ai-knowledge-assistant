import os
from langchain_community.vectorstores import Chroma # type: ignore
from langchain_ollama import OllamaEmbeddings # type: ignore
from langchain_text_splitters import CharacterTextSplitter # type: ignore
from langchain_community.document_loaders import TextLoader # type: ignore

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.abspath(
    os.path.join(BASE_DIR, "../../docs/knowledge.txt")
)

PERSIST_DIR = os.path.join(BASE_DIR, "chroma_db")

def load_documents(): # type: ignore
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    
    loader = TextLoader(file_path) # type: ignore
    return loader.load() # type: ignore

def split_documents(documents): # type: ignore
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50) # type: ignore
    return splitter.split_documents(documents) # type: ignore

def get_vectorstore(): # type: ignore
    embeddings = OllamaEmbeddings(model="nomic-embed-text") # type: ignore

    # Load existing DB if present
    if os.path.exists(PERSIST_DIR):
        return Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings) # type: ignore

    # Else create new
    documents = load_documents() # type: ignore
    docs = split_documents(documents) # type: ignore

    vectorstore = Chroma.from_documents( # type: ignore
        docs,
        embeddings,
        persist_directory=PERSIST_DIR
    )
    vectorstore.persist() # type: ignore
    return vectorstore # type: ignore


# Lazy init
vectorstore = None

def search_docs(query): # type: ignore
    global vectorstore
    if vectorstore is None:
        vectorstore = get_vectorstore() # type: ignore

    results = vectorstore.similarity_search(query, k=2) # type: ignore
    return "\n".join([r.page_content for r in results]) # type: ignore