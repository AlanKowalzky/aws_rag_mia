Hands-on Task: RAG Question-Answering System
Task Description
Build a question-answering system for the museum documentation using RAG (Retrieval-Augmented Generation) architecture.

Technical Requirements
Part 1: Data Preparation and Vectorization
Document Loading and Processing

Create a script to load text documents from a folder
Implement document splitting into chunks of 500-1000 tokens
Ensure overlap between chunks of 50-100 tokens
Embedding Creation

Use an embedding model to create vector representations (e.g., sentence-transformers)
Store embeddings in a vector database (ChromaDB, FAISS, or Pinecone)
Implement a function to search for the most relevant documents
Part 2: LLM Integration
LLM Setup

Connect any available LLM (OpenAI API, Hugging Face, local model)
Create a prompt template for generating answers based on retrieved documents
Handle errors and timeouts properly
RAG Pipeline

Combine search and generation into a unified pipeline
Implement a function that takes a question and returns an answer with sources
Add logging for all processing stages
Part 3: API and Interface
REST API

Create a simple API with an endpoint for questions (FastAPI/Flask on Python or express/fastify on Node.js)
Implement input data validation
Add swagger/openapi documentation
Simple Interface

Create a basic web interface or CLI for testing
Display answers and information sources
Bonus Part: Optimization and Monitoring (proceed with it if you have time)
Caching

Implement answer caching for identical questions
Use Redis or simple in-memory caching
Metrics and Logging

Add processing time metrics
Log questions, retrieved documents, and answer quality
Technical Stack
Required Technologies:
Any vector database (ChromaDB, FAISS, or Pinecone)
LLM API or local model
Web framework for API
Option 1: Python Implementation
Core Libraries:

# Essential
langchain>=0.1.0
sentence-transformers>=2.2.0
chromadb>=0.4.0
fastapi>=0.100.0
uvicorn>=0.23.0

# LLM Integration
openai>=1.0.0  # if using OpenAI
transformers>=4.30.0  # for local models
anthropic>=0.25.0  # if using Claude

# Additional
redis>=4.5.0  # for caching
pytest>=7.0.0  # for testing
Option 2: Node.js Implementation
Core Libraries:

// Essential
"@langchain/core": "^0.1.0",
"@langchain/community": "^0.0.1",
"chromadb": "^1.5.0",
"express": "^4.18.0",

// LLM Integration
"openai": "^4.0.0",  // if using OpenAI
"@anthropic-ai/sdk": "^0.20.0",  // if using Claude
"@huggingface/inference": "^2.6.0",

// Additional
"redis": "^4.6.0",  // for caching
"jest": "^29.0.0",  // for testing
"dotenv": "^16.0.0",
"cors": "^2.8.0"
Test Data
Use the Minneapolis Institute of Art collection dataset from https://github.com/artsmia/collection. The dataset contains JSON files with artwork metadata including descriptions, titles, artist information, and cultural context.

Example test questions:

"Show me American paintings from the 19th century" "Find artworks with floral motifs or nature themes" "What can you tell me about Japanese ceramics in the collection?" "Find portraits by female artists" "Show me artworks related to religious themes"

Evaluation Criteria
We will not evaluate your code, but we will evaluate your demo.
Prepare short video (5-10 minutes) with the demo of your solution (Please use English).
Upload your video to YouTube.
Submit the link to RS App.
Helpful Resources and Materials
Core RAG Concepts
What is RAG? - IBM
RAG explained - Pinecone
Building RAG systems - OpenAI Cookbook
Key Library Documentation
LangChain:

LangChain Documentation
RAG Tutorial with LangChain
Vector Stores in LangChain
ChromaDB:

ChromaDB Getting Started
ChromaDB Python Client
Sentence Transformers:

Sentence Transformers Documentation
Pretrained Models
FastAPI:

FastAPI Tutorial
FastAPI Advanced Features
Practical Tutorials
RAG Implementation:

Building a RAG system from scratch - Towards Data Science
RAG Pipeline with ChromaDB and OpenAI
Advanced RAG Techniques
Evaluation Metrics:

Evaluating RAG Systems - Weights & Biases
RAG Evaluation Framework
Vector Databases
Vector Database Comparison
FAISS Documentation
Weaviate Documentation
Chunking Strategies
Text Chunking Strategies
Document Splitting Best Practices
Prompt Engineering
Prompt Engineering Guide
OpenAI Prompt Engineering
RAG Prompting Techniques
Testing and Metrics
Testing LLM Applications
Pytest Documentation
Unit Testing RAG Systems
Deployment and Production
Docker for Python Applications
FastAPI Deployment
Monitoring ML Systems
Additional Tools
Document Processing:

PyPDF2 Documentation
python-docx
Unstructured.io
Caching:

Redis Python Client
Caching with FastAPI
Logging:

Python Logging
Structlog
Code Examples on GitHub
RAG Examples Repository
ChromaDB Examples
Sentence Transformers Examples
Courses and Learning Materials
DeepLearning.AI LangChain Course
Pinecone Learning Center
Hugging Face NLP Course
Research Papers
Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - original RAG paper
Dense Passage Retrieval - modern retrieval methods
REALM: Retrieval-Augmented Language Model Pre-Training
Development Tools
Jupyter Lab - for experiments
Poetry - for dependency management
Pre-commit - for code quality
Good luck!