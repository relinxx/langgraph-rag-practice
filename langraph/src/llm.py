from langchain_community.llms import Ollama
from langchain import PromptTemplate, LLMChain

llm = Ollama(model = "llama3")