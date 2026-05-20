# RagBucket

### Portable Executable RAG Artifacts for Python

<div align="center">

<img src="frontend/img/ragbucket.png" width="140" />

### Build once. Load anywhere.

[![PyPI version](https://img.shields.io/pypi/v/ragbucket?style=for-the-badge\&color=FFD700\&labelColor=1a1a2e)](https://pypi.org/project/ragbucket/)
[![Python](https://img.shields.io/pypi/pyversions/ragbucket?style=for-the-badge\&color=4FC3F7\&labelColor=1a1a2e)](https://pypi.org/project/ragbucket/)
[![License: MIT](https://img.shields.io/badge/License-MIT-A8FF78?style=for-the-badge\&labelColor=1a1a2e)](LICENSE)

### 🌐 Website

https://ragbucket.vercel.app

### 📦 PyPI

https://pypi.org/project/ragbucket/

### 💻 GitHub

https://github.com/anikchand461/ragbucket

</div>

---

# ✦ What is RagBucket?

Traditional ML models are portable:

```text
model.pt
model.onnx
model.gguf
model.h5
```

RAG systems are not.

Most retrieval systems are tightly coupled with:

* vector databases
* embedding pipelines
* infrastructure
* chunking logic
* provider-specific code

RagBucket changes that.

It packages your entire retrieval system into a single portable:

```text
.rag
```

artifact.

A `.rag` artifact contains:

* vector embeddings
* FAISS index
* chunked knowledge
* retrieval configuration
* runtime metadata

Build it once.
Load it anywhere.

---

# ✦ The Core Idea

<div align="center">

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Index
    ↓
Packaged into:
demo.rag
```

Then later:

```text
demo.rag
    ↓
RagRuntime
    ↓
Any LLM Provider
    ↓
Generated Response
```

</div>

---

# ✦ Full Architecture

<div align="center">

```text
┌──────────────────── BUILD PIPELINE ────────────────────┐

Documents (.txt)
        ↓
Chunker
        ↓
Embedding Provider
(local / cohere / openai / gemini / voyage)
        ↓
FAISS Index
        ↓
Packager
        ↓
Portable .rag Artifact

└────────────────────────────────────────────────────────┘


┌──────────────────── RUNTIME PIPELINE ──────────────────┐

.rag Artifact
        ↓
RagLoader
        ↓
Retriever
        ↓
LLM Provider
(groq / openai / gemini / anthropic)
        ↓
Generated Response

└────────────────────────────────────────────────────────┘
```

</div>

---

# ✦ Installation

## Using uv (recommended)

```bash
uv add ragbucket
```

## Using pip

```bash
pip install ragbucket
```

---

# ⚡ Quickstart

# Step 1 — Build a `.rag` Artifact

```python
from ragbucket import RagBuilder
from ragbucket import RagConfig

import os
from dotenv import load_dotenv

load_dotenv()

config = RagConfig(

    # --------------------------------
    # EMBEDDING PROVIDER
    # --------------------------------
    embedding_provider="cohere",

    embedding_model="embed-english-v3.0",

    embedding_api_key=os.getenv(
        "COHERE_API_KEY"
    ),

    # --------------------------------
    # CHUNKING
    # --------------------------------
    chunk_size=512,

    chunk_overlap=50,

    # --------------------------------
    # RETRIEVAL
    # --------------------------------
    top_k=3
)

builder = RagBuilder(
    config=config
)

builder.build(
    doc_path="docs/",
    op_path="artifacts/demo.rag"
)
```

This generates:

```text
artifacts/demo.rag
```

---

# Step 2 — Query the Artifact

```python
from ragbucket import RagRuntime

import os
from dotenv import load_dotenv

load_dotenv()

system_prompt = """
You are a helpful assistant.
Keep answers short and crisp.
"""

rag = RagRuntime(

    # --------------------------------
    # RAG ARTIFACT
    # --------------------------------
    rag_path="artifacts/demo.rag",

    # --------------------------------
    # GENERATION PROVIDER
    # --------------------------------
    provider="groq",

    api_key=os.getenv(
        "GROQ_API_KEY"
    ),

    model="llama-3.1-8b-instant",

    # --------------------------------
    # EMBEDDING PROVIDER KEY
    # --------------------------------
    embedding_api_key=os.getenv(
        "COHERE_API_KEY"
    ),

    # --------------------------------
    # SYSTEM PROMPT
    # --------------------------------
    system_prompt=system_prompt
)

response = rag.ask(
    "What are Anik's AI/ML skills?"
)

print(response)
```

---

# ✦ Multi-Provider Runtime

RagBucket cleanly separates:

* retrieval embeddings
* generation providers

This enables modular AI pipelines.

## Supported Generation Providers

| Provider  | Example Model        |
| --------- | -------------------- |
| groq      | llama-3.1-8b-instant |
| openai    | gpt-4o-mini          |
| gemini    | gemini-1.5-flash     |
| anthropic | claude-3-haiku       |

---

# ✦ Modular Embedding Providers

| Provider | Example Model          |
| -------- | ---------------------- |
| local    | BAAI/bge-small-en-v1.5 |
| cohere   | embed-english-v3.0     |
| openai   | text-embedding-3-small |
| gemini   | models/embedding-001   |
| voyage   | voyage-large-2         |

Example:

```python
config = RagConfig(

    embedding_provider="openai",

    embedding_model="text-embedding-3-small",

    embedding_api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)
```

---

# ✦ Lightweight by Default

RagBucket no longer forces heavyweight local AI dependencies.

The core package stays lightweight.

Heavy embedding dependencies are only required when using:

```python
embedding_provider="local"
```

If local dependencies are missing, RagBucket automatically shows installation guidance like:

```text
Local embedding support requires:

pip install sentence-transformers

OR

uv add sentence-transformers
```

---

# ✦ What a `.rag` Artifact Contains

```text
demo.rag
│
├── vectors.faiss
├── chunks.json
└── manifest.json
```

The artifact stores:

* semantic vectors
* retrieval memory
* embedding configuration
* retrieval settings
* runtime metadata

---

# ✦ Project Structure

```text
ragbucket/
│
├── builder/
│   ├── builder.py
│   ├── chunker.py
│   ├── indexer.py
│   └── packager.py
│
├── runtime/
│   ├── runtime.py
│   ├── retriever.py
│   ├── loader.py
│   └── providers/
│
├── embeddings/
│   ├── factory.py
│   ├── local_embedder.py
│   ├── cohere_embedder.py
│   ├── openai_embedder.py
│   ├── gemini_embedder.py
│   └── voyage_embedder.py
│
├── schemas/
│
└── utils/
```

---

# ✦ Philosophy

RagBucket treats RAG systems as:

> portable executable retrieval intelligence

This separates:

* retrieval memory
* runtime inference
* generation providers
* deployment environments

The result:

* reusable retrieval systems
* portable semantic memory
* lightweight deployments
* modular AI infrastructure

---

# ✦ Roadmap

* Hybrid retrieval
* BM25 support
* Rerankers
* Streaming responses
* Multi-vector retrieval
* Cloud vector stores
* Metadata filtering
* Artifact versioning
* Distributed runtime execution

---

# ✦ License

MIT License

---

<div align="center">

### Built by Anik Chand

RagBucket — Portable Retrieval Infrastructure for AI Systems.

</div>
