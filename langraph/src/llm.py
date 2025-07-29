from langchain_community.llms import Ollama
from langchain import PromptTemplate, LLMChain



def generate_response(context, query):
    llm = Ollama(model = "llama3")

    prompt = """ YOU ARE A PROFESSIONAL AGENT WHO ANSWERS THE QUERIES BASED ON THE PROVIDED CHUNKS OF INFORMATION

            context: here is the provided context of the query: {context}
            query: {query}

            follow instructions as you will answer precisely and based on the given context
    """

    template = PromptTemplate(template=prompt, input_variables=["query","context"])

    chain = LLMChain(llm=llm, template=template)
    response = chain.run({"query": query, "context": context})
    return response
