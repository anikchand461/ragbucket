# RagBucket

<div align="center">

### Portable Executable RAG Artifacts for Python

Build Retrieval-Augmented Generation systems as reusable, shareable, and executable `.rag` artifacts.

<p align="center">
  <a href="https://pypi.org/project/ragbucket/">PyPI</a> •
  <a href="#installation">Installation</a> •
  <a href="#quickstart">Quickstart</a> •
  <a href="#core-idea">Core Idea</a>
</p>

</div>

---

# Why RagBucket?

Traditional machine learning models are portable.

```text
model.pt
model.onnx
model.gguf
```

They can be:

- saved
- shared
- deployed
- reused anywhere

But Retrieval-Augmented Generation (RAG) systems are still fragmented.

A modern RAG pipeline usually depends on:

- vector databases
- embedding pipelines
- chunking systems
- retrievers
- metadata stores
- external infrastructure

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

The `.rag` artifact packages:

- vector memory
- semantic embeddings
- chunked knowledge
- retrieval metadata
- FAISS indexes
- runtime configuration

into a single reusable file.

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

The builder converts knowledge into a portable retrieval artifact.

The runtime loads the artifact and performs:

- semantic retrieval
- contextual augmentation
- LLM-powered generation

using an external model provider like Groq.

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

## Step 1 — Build a `.rag` Artifact

```python
from ragbucket import RagBuilder

builder = RagBuilder()

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

## Step 2 — Load and Use the Artifact

```python
from ragbucket import RagRuntime

system_prompt = """
you are Anik's personal chatbot.
you know all things about anik.

If anyone asks about the resume of anik
please share the details as required.

keep the answers super simple and crisp.
"""

rag = RagRuntime(
    rag_path="artifacts/demo.rag",
    api_key="your_groq_api_key",
    model="llama-3.1-8b-instant",
    system_prompt=system_prompt
)

response = rag.ask(
    "Can you tell me Anik's skills related to AIML?"
)

print(response)
```

---

# Example Output

```text
Anik's AI/ML skills include:
- Hugging Face
- LangChain
- Streamlit
- FastAPI
- Deep Learning
- Transformers
```

---

# What a `.rag` File Contains

A `.rag` artifact stores everything required for retrieval:

- semantic embeddings
- FAISS vector index
- chunked document memory
- retrieval metadata
- artifact manifest
- runtime configuration

The only thing required during inference is:

- an LLM provider API key

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
LLM Generation
    ↓
Final Response
```

---

# Features

## Portable RAG Artifacts

Serialize retrieval systems into reusable `.rag` files.

---

## Built-in Semantic Search

Uses FAISS for efficient vector similarity retrieval.

---

## Groq-Powered Generation

Use Groq-hosted LLMs for fast inference.

---

## Lightweight Runtime

Load and execute `.rag` artifacts anywhere using Python.

---

## Self-Contained Retrieval Memory

The artifact itself contains the retrieval system.

---

## Simple Developer API

Minimal abstraction for building and querying RAG artifacts.

---

## Extensible Design

Designed for future support of:

- hybrid retrieval
- metadata filtering
- reranking
- distributed vector stores
- multi-model runtimes

---

# Technology Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Embeddings      | Sentence Transformers |
| Vector Search   | FAISS                 |
| Chunking        | LangChain             |
| Runtime         | Python                |
| Generation      | Groq                  |
| Packaging       | zipfile               |
| Artifact Format | `.rag`                |

---

# Philosophy

RagBucket treats RAG systems as:

# portable intelligence artifacts

instead of:

# fragmented retrieval pipelines

This separates:

- knowledge retrieval
  from
- language generation

allowing:

- reusable semantic memory
- portable RAG execution
- simplified deployment
- infrastructure-independent retrieval systems

---

# Current Scope

RagBucket currently supports:

- local `.rag` artifact generation
- FAISS vector indexing
- semantic retrieval
- Groq-powered response generation

The project is intentionally lightweight and focused on:

# portable RAG execution

---

# Future Roadmap

Planned features include:

- hybrid retrieval
- metadata-aware search
- artifact versioning
- reranking support
- Milvus integration
- multi-provider LLM runtime
- distributed retrieval
- `.rag` registries

---

# Vision

RagBucket aims to become:

> “The portable runtime layer for Retrieval-Augmented Generation systems.”

A future where RAG systems can be:

- built once
- shared anywhere
- executed everywhere

through standardized portable intelligence artifacts.

---

# License

MIT License
