# RagBucket

<div align="center">

## Portable Executable RAG Artifacts for Python

Build Retrieval-Augmented Generation systems as reusable, shareable, and executable `.rag` artifacts.

<p align="center">
  <a href="https://pypi.org/project/ragbucket/">PyPI</a> •
  <a href="#installation">Installation</a> •
  <a href="#quickstart">Quickstart</a> •
  <a href="#features">Features</a> •
  <a href="#vision">Vision</a>
</p>

</div>

---

# What is RagBucket?

Traditional machine learning models are portable.

```text
model.pt
model.onnx
model.gguf
model.h5
```

They can be:

- saved
- reused
- shared
- deployed anywhere

But modern Retrieval-Augmented Generation (RAG) systems are still fragmented.

A typical RAG pipeline depends on:

- vector databases
- embedding pipelines
- chunking systems
- retrievers
- metadata stores
- external infrastructure
- provider-specific integrations

This makes RAG systems:

- difficult to distribute
- tightly coupled to infrastructure
- hard to reproduce
- non-portable

---

# Introducing `.rag`

RagBucket introduces:

# `.rag`

A portable executable artifact format for Retrieval-Augmented Generation systems.

A `.rag` artifact packages:

- semantic embeddings
- vector indexes
- chunked knowledge
- retrieval configuration
- runtime metadata

into a single reusable file.

Build once. Load anywhere.

---

# Core Idea

```text
Documents
    ↓
RagBuilder
    ↓
model.rag
    ↓
RagRuntime
    ↓
Question Answering
```

The builder converts raw documents into a portable retrieval artifact.

The runtime loads the artifact and performs:

- semantic retrieval
- contextual augmentation
- provider-based generation

using external LLM providers like:

- Groq
- OpenAI
- Gemini
- Anthropic

---

# Installation

## Using uv

```bash
uv add ragbucket
```

---

## Using pip

```bash
pip install ragbucket
```

---

# Quickstart

# Step 1 — Build a `.rag` Artifact

```python
from ragbucket import RagBuilder
from ragbucket import RagConfig


config = RagConfig(

    embedding_model="BAAI/bge-small-en-v1.5",

    chunk_size=512,

    chunk_overlap=50,

    top_k=3
)


builder = RagBuilder(
    config=config
)


builder.build(
    doc_path="docs",
    op_path="artifacts/demo.rag"
)
```

This generates:

```text
artifacts/demo.rag
```

---

# Step 2 — Load and Use the Artifact

```python
from ragbucket import RagRuntime

import os

from dotenv import load_dotenv


load_dotenv()


system_prompt = """
you are Anik's personal chatbot.

keep answers short and crisp.
"""


rag = RagRuntime(

    rag_path="artifacts/demo.rag",

    provider="groq",

    api_key=os.getenv("GROQ_API_KEY"),

    model="llama-3.1-8b-instant",

    system_prompt=system_prompt
)


response = rag.ask(
    "What are Anik's AIML skills?"
)

print(response)
```

---

# Multi-Provider Runtime

RagBucket supports multiple LLM providers through a unified runtime abstraction.

---

## Groq

```python
provider="groq"
model="llama-3.1-8b-instant"
```

---

## OpenAI

```python
provider="openai"
model="gpt-4o-mini"
```

---

## Gemini

```python
provider="gemini"
model="gemini-1.5-flash"
```

---

## Anthropic

```python
provider="anthropic"
model="claude-3-haiku-20240307"
```

---

# Runtime Pipeline

```text
User Query
    ↓
Query Embedding
    ↓
Semantic Vector Search
    ↓
Relevant Context Retrieval
    ↓
LLM Provider
    ↓
Generated Response
```

---

# Dynamic Configuration System

RagBucket supports configurable retrieval pipelines using `RagConfig`.

You can customize:

- embedding model
- chunk size
- chunk overlap
- retrieval top-k

Example:

```python
from ragbucket import RagConfig


config = RagConfig(

    embedding_model="sentence-transformers/all-MiniLM-L6-v2",

    chunk_size=1024,

    chunk_overlap=100,

    top_k=5
)
```

Any missing configuration values are automatically filled using framework defaults.

---

# Supported Embedding Models

RagBucket works with any compatible Sentence Transformers model.

Examples:

```python
"BAAI/bge-small-en-v1.5"
```

```python
"sentence-transformers/all-MiniLM-L6-v2"
```

```python
"sentence-transformers/all-mpnet-base-v2"
```

```python
"BAAI/bge-base-en-v1.5"
```

---

# What a `.rag` File Contains

A `.rag` artifact stores:

- semantic embeddings
- FAISS vector index
- chunked document memory
- retrieval metadata
- runtime configuration
- artifact manifest

The only requirement during inference is:

- an LLM provider API key

---

# Features

## Portable RAG Artifacts

Serialize retrieval systems into reusable `.rag` files.

---

## Built-in Semantic Search

Uses FAISS for efficient vector similarity retrieval.

---

## Multi-Provider Runtime

Unified runtime interface for:

- Groq
- OpenAI
- Gemini
- Anthropic

---

## Configurable Retrieval Pipeline

Customize chunking and embedding behavior using `RagConfig`.

---

## Lightweight Runtime

Load and execute `.rag` artifacts anywhere using Python.

---

## Self-Contained Retrieval Memory

The artifact itself contains the retrieval system.

---

## Simple Developer API

Minimal abstractions for building and querying portable RAG systems.

---

## Extensible Architecture

Designed for future support of:

- reranking
- metadata filtering
- hybrid retrieval
- distributed vector stores
- remote artifact registries

---

# Technology Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Embeddings      | Sentence Transformers |
| Vector Search   | FAISS                 |
| Chunking        | LangChain             |
| Runtime         | Python                |
| Packaging       | zipfile               |
| Artifact Format | `.rag`                |

---

# Philosophy

RagBucket treats RAG systems as:

# portable intelligence artifacts

instead of:

# fragmented retrieval pipelines

This separates:

- retrieval memory
  from
- language generation

allowing:

- reusable semantic memory
- infrastructure-independent retrieval
- portable execution
- simplified deployment

---

# Current Scope

RagBucket currently supports:

- local `.rag` artifact generation
- semantic retrieval
- configurable chunking
- multi-provider inference
- FAISS vector indexing
- provider-based generation

The project is intentionally lightweight and focused on:

# portable RAG execution

---

# Future Roadmap

Planned features:

- hybrid retrieval
- metadata-aware search
- reranking support
- artifact versioning
- remote artifact loading
- distributed vector stores
- multi-vector retrieval
- `.rag` registries

---

# Vision

RagBucket aims to become:

> "The portable runtime layer for Retrieval-Augmented Generation systems."

A future where RAG systems can be:

- built once
- shared anywhere
- executed everywhere

through standardized portable intelligence artifacts.

---

# License

MIT License
