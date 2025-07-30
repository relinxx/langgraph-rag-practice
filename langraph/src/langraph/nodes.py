import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from llm import generate_response
from chroma_db import vector_store
from langgraph.graph import START, StateGraph
from project_flow import State



def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"], k=5)
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    answer = generate_response(context=docs_content, query=state["question"])
    return {"answer": answer}

graph_builder = StateGraph(State)
graph_builder.add_node("retrieve", retrieve)
graph_builder.add_node("generate", generate)
graph_builder.add_edge(START, "retrieve")
graph_builder.add_edge("retrieve", "generate")
graph = graph_builder.compile()