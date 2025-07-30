#!/usr/bin/env python3
"""
Test script to validate the RAG pipeline functionality
"""

def test_data_ingestion():
    """Test document processing and ingestion"""
    print("Testing data ingestion...")
    from data_ingestion import Text_Extractor
    
    try:
        docs = Text_Extractor.doc_processor()
        print(f"✅ Successfully processed {len(docs)} document chunks")
        return True
    except Exception as e:
        print(f"❌ Data ingestion failed: {e}")
        return False

def test_embeddings():
    """Test embedding model"""
    print("\nTesting embedding model...")
    try:
        from embedder import embedding_model
        test_text = "This is a test document"
        embeddings = embedding_model.embed_query(test_text)
        print(f"✅ Embedding model working, dimension: {len(embeddings)}")
        return True
    except Exception as e:
        print(f"❌ Embedding model failed: {e}")
        return False

def test_vector_store():
    """Test vector store operations"""
    print("\nTesting vector store...")
    try:
        from chroma_db import vector_store
        # Test search functionality
        results = vector_store.similarity_search("test query", k=1)
        print(f"✅ Vector store working, found {len(results)} documents")
        return True
    except Exception as e:
        print(f"❌ Vector store failed: {e}")
        return False

def test_llm():
    """Test LLM functionality"""
    print("\nTesting LLM...")
    try:
        from llm import generate_response
        context = "This is a test context about AI and machine learning."
        query = "What is this about?"
        response = generate_response(context, query)
        print(f"✅ LLM working, response length: {len(response)}")
        return True
    except Exception as e:
        print(f"❌ LLM failed: {e}")
        return False

def test_langgraph():
    """Test LangGraph workflow"""
    print("\nTesting LangGraph workflow...")
    try:
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), 'langraph'))
        
        from langraph.nodes import graph
        from langraph.project_flow import State
        
        # Test the graph with a simple query
        initial_state = {"question": "What information do you have?", "context": [], "answer": ""}
        result = graph.invoke(initial_state)
        print(f"✅ LangGraph working, answer: {result.get('answer', 'No answer')[:100]}...")
        return True
    except Exception as e:
        print(f"❌ LangGraph failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting RAG System Validation Tests\n")
    
    tests = [
        test_data_ingestion,
        test_embeddings,
        test_vector_store,
        test_llm,
        test_langgraph
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All systems working correctly!")
    else:
        print("⚠️  Some issues found, please check the errors above")

if __name__ == "__main__":
    main()
