from rag.rag import search_docs

def researcher_agent(query):
    context = search_docs(query)
    return context
