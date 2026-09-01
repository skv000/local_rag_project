# Local RAG Project

A local Retrieval-Augmented Generation (RAG) application built with Python and Ollama.

The goal of this project is to learn and implement a local GenAI system from the fundamentals, without initially relying on high-level frameworks such as LangChain or LlamaIndex.

## Current Stack

- Python 3.12
- uv
- Ollama
- Llama 3.2 3B
- NVIDIA RTX 3050 4GB

## Current Features

- Local LLM inference using Ollama
- Python integration with Ollama
- Basic interactive AI assistant

## Planned Features

- Conversation history
- Streaming responses
- Structured outputs
- Local embeddings
- Semantic search
- Document ingestion
- Text chunking
- Vector database
- Retrieval-Augmented Generation (RAG)
- PDF/DOCX support
- Source citations
- FastAPI backend
- Web UI
- RAG evaluation
- Advanced retrieval

## Architecture

```text
User
 |
 v
Python Application
 |
 v
Ollama
 |
 v
Llama 3.2 3B
 |
 v
Local GPU / CPU