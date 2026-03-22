import os
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader


#Load document 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.abspath(
    os.path.join(BASE_DIR, "../../docs/knowledge.txt")
)
loader = TextLoader(file_path)
documents = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Create embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

#store in vector DB
vectorstore = Chroma.from_documents(docs, embeddings)

#Search Function

def search_docs(query):
    results = vectorstore.similarity_search(query, k=2)
    return "\n".join([r.page_content for r in results])



