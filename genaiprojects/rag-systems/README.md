# 🔍 RAG Systems (Retrieval Augmented Generation)

AI systems that combine knowledge retrieval with text generation for accurate, contextual responses.

## 📁 Folder Structure

```
rag-systems/
├── README.md                   # This file
├── architecture.md             # RAG system designs
├── requirements.txt            # Dependencies
├── core/
│   ├── __init__.py
│   ├── document_loader.py     # Load various document types
│   ├── text_splitter.py       # Chunk text intelligently
│   ├── embeddings.py          # Text vectorization
│   ├── vector_store.py        # Vector database operations
│   └── retriever.py           # Similarity search logic
├── databases/
│   ├── __init__.py
│   ├── faiss_store.py         # FAISS vector database
│   ├── chroma_store.py        # ChromaDB integration
│   ├── pinecone_store.py      # Pinecone cloud vector DB
│   └── opensearch_store.py    # AWS OpenSearch
├── retrievers/
│   ├── __init__.py
│   ├── semantic_search.py     # Semantic similarity
│   ├── hybrid_search.py       # Keyword + semantic
│   ├── multi_query.py         # Multiple query strategies
│   └── contextual_compression.py # Compress retrieved context
├── generators/
│   ├── __init__.py
│   ├── basic_rag.py           # Simple RAG implementation
│   ├── conversational_rag.py  # Chat with memory
│   ├── multi_document_rag.py  # Multiple document sources
│   └── adaptive_rag.py        # Self-improving RAG
├── examples/
│   ├── __init__.py
│   ├── document_qa.py         # Document Q&A system
│   ├── knowledge_base.py      # Company knowledge base
│   ├── research_assistant.py  # Research with citations
│   ├── code_documentation.py  # Code Q&A system
│   └── legal_assistant.py     # Legal document analysis
├── evaluation/
│   ├── __init__.py
│   ├── metrics.py             # RAG evaluation metrics
│   ├── benchmarks.py          # Standard benchmarks
│   └── human_eval.py          # Human evaluation tools
└── tests/
    ├── __init__.py
    ├── test_retrieval.py      # Retrieval accuracy tests
    ├── test_generation.py     # Generation quality tests
    └── test_end_to_end.py     # Full pipeline tests
```

## 🔄 RAG Pipeline

1. **Document Ingestion**: Load and preprocess documents
2. **Text Chunking**: Split into meaningful segments
3. **Embedding**: Convert text to vectors
4. **Storage**: Store in vector database
5. **Query Processing**: Understand user question
6. **Retrieval**: Find relevant context
7. **Generation**: Create answer with context
8. **Post-processing**: Format and validate response

## 🎯 RAG Variants

### Basic RAG
- Simple retrieval + generation
- Good for straightforward Q&A

### Conversational RAG
- Maintains chat history
- Context-aware follow-ups

### Multi-Document RAG
- Searches across multiple sources
- Provides source attribution

### Adaptive RAG
- Self-improving retrieval
- Dynamic context selection

## 📊 Evaluation Metrics

- **Retrieval**: Precision, Recall, MRR
- **Generation**: BLEU, ROUGE, BERTScore
- **End-to-End**: Faithfulness, Relevance, Completeness