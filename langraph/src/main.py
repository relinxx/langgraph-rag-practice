import warnings
warnings.filterwarnings("ignore")

from langraph.nodes import graph

print("RAG System - Ask questions (type 'quit' to exit)")
while True:
    try:
        q = input("Q: ").strip()
        if q.lower() in ['quit', 'exit', 'q']: break
        if q:
            try:
                result = graph.invoke({'question': q, 'context': [], 'answer': ''})
                print(f"A: {result.get('answer', 'No answer')}\n")
            except Exception as e:
                if "quota" in str(e).lower() or "429" in str(e):
                    print("API quota exceeded. Try again later.\n")
                else:
                    print(f"Error: {str(e)[:100]}...\n")
    except (KeyboardInterrupt, EOFError): 
        break
print("Goodbye!")
