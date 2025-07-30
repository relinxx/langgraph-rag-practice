#!/usr/bin/env python3
"""
Demo script showing how to use the RAG system
"""

import sys
import os

# Add langraph directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'langraph'))

from langraph.nodes import graph
from langraph.project_flow import State

def ask_question(question: str):
    """Ask a question to the RAG system"""
    print(f"Question: {question}")
    print("Processing...")
    
    try:
        # Initialize state
        initial_state = {
            "question": question,
            "context": [],
            "answer": ""
        }
        
        # Run the graph
        result = graph.invoke(initial_state)
        
        print(f"Answer: {result.get('answer', 'No answer generated')}")
        print(f"Context documents used: {len(result.get('context', []))}")
        print("-" * 50)
        
        return result
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    """Demo the RAG system with sample questions"""
    print("🤖 RAG System Demo\n")
    
    # Sample questions - adjust based on your data
    sample_questions = [
        "What information do you have?",
        "Tell me about the documents",
        "What can you help me with?"
    ]
    
    for question in sample_questions:
        ask_question(question)
    
    # Interactive mode
    print("\n🔄 Interactive Mode (type 'quit' to exit)")
    while True:
        try:
            user_question = input("\nYour question: ").strip()
            if user_question.lower() in ['quit', 'exit', 'q']:
                break
            if user_question:
                ask_question(user_question)
        except KeyboardInterrupt:
            break
    
    print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
