<div align="center">

<img src="frontend/img/ragbucket.png" alt="RagBucket Logo" width="140" />

# RagBucket

### Portable Executable RAG Artifacts for Python

**Build once. Load anywhere.**

[![PyPI version](https://img.shields.io/pypi/v/ragbucket?style=for-the-badge&color=FFD700&labelColor=1a1a2e)](https://pypi.org/project/ragbucket/)
[![Python](https://img.shields.io/pypi/pyversions/ragbucket?style=for-the-badge&color=4FC3F7&labelColor=1a1a2e)](https://pypi.org/project/ragbucket/)
[![License: MIT](https://img.shields.io/badge/License-MIT-A8FF78?style=for-the-badge&labelColor=1a1a2e)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/ragbucket?style=for-the-badge&color=FF6B9D&labelColor=1a1a2e)](https://pypi.org/project/ragbucket/)

<p>
  <a href="#-installation">Installation</a> •
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-what-is-ragbucket">What is RagBucket?</a> •
  <a href="#-multi-provider-runtime">Providers</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

</div>

---

## The Problem

Traditional ML models are portable by default:

```
model.pt   model.onnx   model.gguf   model.h5
```

They can be saved, shared, and deployed anywhere. **RAG systems can't.**

A typical RAG pipeline is a fragile web of:

- vector databases tied to infrastructure
- embedding pipelines that must be re-run
- chunking configs scattered across codebases
- provider-specific integrations with no portability
- metadata that lives nowhere and everywhere

**RagBucket solves this.** It packages your entire RAG pipeline — vectors, chunks, config, and runtime metadata — into a single portable `.rag` artifact.

---

## Introducing `.rag`

<div align="center">
<img src="frontend/img/main.png" alt="RagBucket Architecture" width="800" />
</div>

A `.rag` artifact is a **self-contained, executable unit of retrieval intelligence**. It packages:

| What                    | How                         |
| ----------------------- | --------------------------- |
| Semantic embeddings     | via Sentence Transformers   |
| Vector index            | via FAISS                   |
| Chunked knowledge       | via LangChain splitters     |
| Retrieval configuration | embedded in manifest        |
| Runtime metadata        | versioned artifact manifest |

**Build it once. Drop it anywhere. Query it with one line of code.**

---

## Full Architecture

<div align="center">
<img src="frontend/img/workflow.png" alt="RagBucket Full Workflow" width="900" />
</div>

---

## ✦ Installation

```bash
# Using uv (recommended)
uv add ragbucket

# Using pip
pip install ragbucket
```

---

````md id="tk5rxv"
## ⚡ Quickstart

### Step 1 — Build a Portable `.rag` Artifact

```python
from ragbucket import RagBuilder
from ragbucket import RagConfig

import os

from dotenv import load_dotenv


load_dotenv()


config = RagConfig(

    # ------------------------------------
    # EMBEDDING PROVIDER
    # ------------------------------------
    embedding_provider="cohere",

    embedding_model="embed-english-v3.0",

    embedding_api_key=os.getenv("COHERE_API_KEY"),

    # ------------------------------------
    # CHUNKING
    # ------------------------------------
    chunk_size=512,

    chunk_overlap=50,

    # ------------------------------------
    # RETRIEVAL
    # ------------------------------------
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

The `.rag` artifact contains:

- vector embeddings
- FAISS index
- document chunks
- retrieval configuration
- artifact metadata

Build once. Query anywhere.

---

### Step 2 — Load and Query the Artifact

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

    # ------------------------------------
    # RAG ARTIFACT
    # ------------------------------------
    rag_path="artifacts/demo.rag",

    # ------------------------------------
    # GENERATION PROVIDER
    # ------------------------------------
    provider="groq",

    api_key=os.getenv("GROQ_API_KEY"),

    model="llama-3.1-8b-instant",

    # ------------------------------------
    # EMBEDDING PROVIDER KEY
    # ------------------------------------
    embedding_api_key=os.getenv("COHERE_API_KEY"),

    # ------------------------------------
    # SYSTEM PROMPT
    # ------------------------------------
    system_prompt=system_prompt
)


response = rag.ask(
    "What are Anik's AI/ML skills?"
)

print(response)
```

---

## 🔌 Multi-Provider Runtime

RagBucket separates:

- retrieval embeddings
- response generation

This allows fully modular AI pipelines.

---

### Supported Generation Providers

| Provider    | Example Model             |
| ----------- | ------------------------- |
| `groq`      | `llama-3.1-8b-instant`    |
| `openai`    | `gpt-4o-mini`             |
| `gemini`    | `gemini-1.5-flash`        |
| `anthropic` | `claude-3-haiku-20240307` |

Example:

```python
rag = RagRuntime(

    rag_path="demo.rag",

    provider="openai",

    api_key=os.getenv("OPENAI_API_KEY"),

    model="gpt-4o-mini",

    embedding_api_key=os.getenv("COHERE_API_KEY")
)
```

---

## 🧠 Modular Embedding Providers

RagBucket supports multiple embedding systems.

| Provider | Example Model            |
| -------- | ------------------------ |
| `local`  | `BAAI/bge-small-en-v1.5` |
| `cohere` | `embed-english-v3.0`     |
| `openai` | `text-embedding-3-small` |
| `gemini` | `models/embedding-001`   |
| `voyage` | `voyage-large-2`         |

Example:

```python
config = RagConfig(

    embedding_provider="openai",

    embedding_model="text-embedding-3-small",

    embedding_api_key=os.getenv("OPENAI_API_KEY")
)
```

---

## ⚙️ Dynamic Retrieval Configuration

Customize every stage of the retrieval pipeline:

```python
from ragbucket import RagConfig


config = RagConfig(

    # Embedding system
    embedding_provider="local",

    embedding_model="sentence-transformers/all-MiniLM-L6-v2",

    # Chunking
    chunk_size=1024,

    chunk_overlap=100,

    # Retrieval
    top_k=5
)
```

All missing values are automatically filled using framework defaults.

---

## 🪶 Lightweight by Default

RagBucket no longer forces heavyweight local AI dependencies.

The core package remains lightweight.

Local embedding dependencies are only required when using:

```python
embedding_provider="local"
```

This enables:

- lightweight installations
- faster deployments
- cloud/serverless compatibility
- provider-based embedding pipelines

---

## 📦 What a `.rag` Artifact Contains

```text
demo.rag
│
├── vectors.faiss
├── chunks.json
├── manifest.json
```

The artifact stores:

- semantic vectors
- retrieval memory
- embedding configuration
- retrieval settings
- runtime metadata

making the retrieval system:

- portable
- reusable
- executable
- shareable
````

---

## 🏗️ Project Structure

```
ragbucket/
├── builder/
│   ├── builder.py      ← RagBuilder orchestrator
│   ├── chunker.py      ← LangChain recursive splitter
│   ├── embedder.py     ← Sentence Transformers encoder
│   ├── indexer.py      ← FAISS index builder
│   └── packager.py     ← .rag artifact packaging
├── runtime/
│   ├── runtime.py      ← RagRuntime orchestrator
│   ├── loader.py       ← .rag artifact loader
│   ├── retriever.py    ← Semantic vector retrieval
│   ├── models.py       ← Cached embedding model singleton
│   └── providers/      ← Groq / OpenAI / Gemini / Anthropic
├── schemas/
│   ├── config.py       ← RagConfig Pydantic model
│   └── manifest.py     ← Artifact manifest schema
└── utils/
    ├── file_utils.py   ← Document loading helpers
    └── hashing.py      ← Artifact integrity utilities
```

---

## 🧰 Technology Stack

| Component          | Technology               |
| ------------------ | ------------------------ |
| Embeddings         | Sentence Transformers    |
| Vector Search      | FAISS                    |
| Chunking           | LangChain Text Splitters |
| Artifact Packaging | Python `zipfile`         |
| Config Validation  | Pydantic                 |
| Runtime            | Pure Python              |

---

## ✦ Philosophy

RagBucket treats RAG systems as **portable intelligence artifacts** — not fragile infrastructure pipelines.

This cleanly separates:

- **Retrieval memory** (what you built) → lives in the `.rag` file
- **Language generation** (how you query it) → any provider, any environment

The result: reusable semantic memory that travels with your code.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**RagBucket** · Built by [Anik Chand](https://github.com/anikchand461)

_The portable runtime layer for Retrieval-Augmented Generation systems._

</div>
