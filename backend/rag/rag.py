import os
from langchain_community.vectorstores import Chroma # type: ignore
from langchain_ollama import OllamaEmbeddings # type: ignore
from langchain.text_splitter import CharacterTextSplitter # type: ignore
from langchain_community.document_loaders import TextLoader # type: ignore

#Load document 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.abspath(
    os.path.join(BASE_DIR, "../../docs/knowledge.txt")
)
loader = TextLoader(file_path) # type: ignore
documents = loader.load() # type: ignore

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50) # type: ignore
docs = splitter.split_documents(documents) # type: ignore

# Create embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text") # type: ignore

#store in vector DB
vectorstore = Chroma.from_documents(docs, embeddings) # type: ignore

#Search Function

def search_docs(query): # type: ignore
    results = vectorstore.similarity_search(query, k=2) # type: ignore
    return "\n".join([r.page_content for r in results]) # type: ignore



