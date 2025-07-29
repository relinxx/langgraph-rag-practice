from llm import generate_response
from chroma_db import document_ids
from langgraph.graph import START, StateGraph
from project_flow import State
from chroma_db import vector_store
from langchain import hub



prompt = hub.pull("rlm/rag-prompt")


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search_with_relevance_scores(state["question"])
    return {"context", retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    answer = generate_response(context=docs_content, query=state["question"])
    return {"answer": answer}

graph_builder = StateGraph(State).add_sequence([retrieve,generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile