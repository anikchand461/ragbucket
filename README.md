<div align="center">

<br/>

<img src="frontend/img/ragbucket.png" alt="RagBucket Logo" width="160" />

<br/>

# RagBucket

<h3><em>Portable Executable RAG Artifacts for Python</em></h3>

**Build once. Load anywhere. Query forever.**

<br/>

[![PyPI version](https://img.shields.io/pypi/v/ragbucket?style=for-the-badge&color=FFD700&labelColor=0d0d1a&logo=python&logoColor=FFD700)](https://pypi.org/project/ragbucket/)
[![Python](https://img.shields.io/pypi/pyversions/ragbucket?style=for-the-badge&color=4FC3F7&labelColor=0d0d1a)](https://pypi.org/project/ragbucket/)
[![License: MIT](https://img.shields.io/badge/License-MIT-A8FF78?style=for-the-badge&labelColor=0d0d1a)](LICENSE)
[![Downloads](https://img.shields.io/endpoint?url=https://pepy.tech/badge/ragbucket/month&style=for-the-badge&labelColor=0d0d1a&color=FF6B9D)](https://pepy.tech/projects/ragbucket)
[![Website](https://img.shields.io/badge/Website-ragbucket.vercel.app-c084fc?style=for-the-badge&labelColor=0d0d1a&logo=vercel&logoColor=c084fc)](https://ragbucket.vercel.app)
[![Blog](https://img.shields.io/badge/BLOG-HASHNODE-2962FF?style=for-the-badge&logo=hashnode&logoColor=white)](https://anikchand.hashnode.dev/why-rag-pipelines-aren-t-portable-building-ragbucket)

<br/>

<p>
  <a href="#-the-problem">Problem</a> ·
  <a href="#-introducing-rag">The .rag Format</a> ·
  <a href="#-installation">Install</a> ·
  <a href="#-quickstart">Quickstart</a> ·
  <a href="#-multi-provider-runtime">Providers</a> ·
  <a href="#-roadmap">Roadmap</a>
</p>

<br/>

</div>

---

## ◈ The Problem

Every major ML format is portable by default:

```
model.pt   ·   model.onnx   ·   model.gguf   ·   model.h5
```

You save them, share them, deploy them anywhere.

**RAG systems can't do any of that.**

A typical RAG pipeline is a fragile web of moving parts:

```
❌  Vector databases tied to specific infrastructure
❌  Embedding pipelines that must be rebuilt from scratch
❌  Chunking configs scattered across codebases
❌  Provider-specific integrations with zero portability
❌  Metadata that lives nowhere and everywhere at once
```

Every time you switch environments — laptop to server, dev to prod, team to team — you rebuild the whole thing. **That's broken.**

**RagBucket fixes this.**

It packages your entire RAG pipeline — vectors, chunks, config, and runtime metadata — into a single portable `.rag` artifact. Like a model checkpoint, but for retrieval intelligence.

---

## ◈ Introducing `.rag`

<div align="center">
<img src="frontend/img/main.png" alt="RagBucket Architecture" width="800" />
</div>

<br/>

A `.rag` artifact is a **self-contained, executable unit of retrieval intelligence.** It is not a config file. It is not a directory. It is a complete, ready-to-run retrieval system.

| What it stores              | How it stores it             |
| :-------------------------- | :--------------------------- |
| Semantic embeddings         | via Sentence Transformers    |
| Vector index                | via FAISS                    |
| Chunked knowledge           | via LangChain splitters      |
| Retrieval configuration     | embedded in manifest         |
| Runtime metadata            | versioned artifact manifest  |

```
Build it once.
Drop it anywhere.
Query it with one line of code.
```

---

## ◈ Full Architecture

<div align="center">
<img src="frontend/img/workflow.png" alt="RagBucket Full Workflow" width="900" />
</div>

---

## ◈ Installation

```bash
# Using uv (recommended)
uv add ragbucket

# Using pip
pip install ragbucket
```

> **Lightweight by default.** Local embedding dependencies are only pulled in when you set `embedding_provider="local"`. Cloud providers add nothing to your base install.

---

## ◈ Quickstart

### Step 1 — Build a Portable `.rag` Artifact

```python
from ragbucket import RagBuilder, RagConfig
import os
from dotenv import load_dotenv

load_dotenv()

config = RagConfig(

    # ── Embedding Provider ────────────────────────────────────
    embedding_provider = "cohere",
    embedding_model    = "embed-english-v3.0",
    embedding_api_key  = os.getenv("COHERE_API_KEY"),

    # ── Chunking ──────────────────────────────────────────────
    chunk_size    = 512,
    chunk_overlap = 50,

    # ── Retrieval ─────────────────────────────────────────────
    top_k = 3,
)

builder = RagBuilder(config=config)

builder.build(
    doc_path = "docs/",
    op_path  = "artifacts/demo.rag",
)
```

This generates a single portable artifact:

```
artifacts/
└── demo.rag          ← your entire RAG pipeline, packaged
```

---

### Step 2 — Load and Query the Artifact

```python
from ragbucket import RagRuntime
import os
from dotenv import load_dotenv

load_dotenv()

rag = RagRuntime(

    # ── RAG Artifact ──────────────────────────────────────────
    rag_path = "artifacts/demo.rag",

    # ── Generation Provider ───────────────────────────────────
    provider = "groq",
    api_key  = os.getenv("GROQ_API_KEY"),
    model    = "llama-3.1-8b-instant",

    # ── Embedding Provider Key ────────────────────────────────
    embedding_api_key = os.getenv("COHERE_API_KEY"),

    # ── System Prompt ─────────────────────────────────────────
    system_prompt = "You are a helpful assistant. Keep answers short and crisp.",
)

response = rag.ask("What are Anik's AI/ML skills?")
print(response)
```

That's it. No vector DB to spin up. No pipeline to reconstruct. Just load and ask.

---

## ◈ Multi-Provider Runtime

RagBucket cleanly separates **retrieval** from **generation** — meaning you can mix and match embedding providers with generation providers freely.

### Generation Providers

| Provider      | Example Model                 |
| :------------ | :---------------------------- |
| `groq`        | `llama-3.1-8b-instant`        |
| `openai`      | `gpt-4o-mini`                 |
| `gemini`      | `gemini-1.5-flash`            |
| `anthropic`   | `claude-3-haiku-20240307`     |

```python
# Swap providers without touching anything else
rag = RagRuntime(
    rag_path  = "demo.rag",
    provider  = "anthropic",
    api_key   = os.getenv("ANTHROPIC_API_KEY"),
    model     = "claude-3-haiku-20240307",
    embedding_api_key = os.getenv("COHERE_API_KEY"),
)
```

### Embedding Providers

| Provider    | Example Model                       |
| :---------- | :---------------------------------- |
| `local`     | `BAAI/bge-small-en-v1.5`            |
| `cohere`    | `embed-english-v3.0`                |
| `openai`    | `text-embedding-3-small`            |
| `gemini`    | `models/embedding-001`              |
| `voyage`    | `voyage-large-2`                    |

```python
# Use any embedding provider at build time
config = RagConfig(
    embedding_provider = "openai",
    embedding_model    = "text-embedding-3-small",
    embedding_api_key  = os.getenv("OPENAI_API_KEY"),
)
```

---

## ◈ Dynamic Retrieval Configuration

Every stage of the retrieval pipeline is configurable. Sane defaults are always applied automatically.

```python
from ragbucket import RagConfig

config = RagConfig(

    # Embedding system
    embedding_provider = "local",
    embedding_model    = "sentence-transformers/all-MiniLM-L6-v2",

    # Chunking
    chunk_size    = 1024,
    chunk_overlap = 100,

    # Retrieval
    top_k = 5,
)
```

> All missing values are filled using framework defaults. Nothing breaks if you leave something out.

---

## ◈ What a `.rag` Artifact Contains

```
demo.rag
│
├── vectors.faiss     ← FAISS vector index (semantic search backbone)
├── chunks.json       ← document chunks with source metadata
└── manifest.json     ← embedding config, top_k, model info, version
```

The artifact is entirely self-describing. Anyone who receives a `.rag` file has everything needed to query it — no external config, no infrastructure dependencies, no guesswork.

---

## ◈ Technology Stack

| Component           | Technology                  |
| :------------------ | :-------------------------- |
| Embeddings          | Sentence Transformers       |
| Vector Search       | FAISS                       |
| Chunking            | LangChain Text Splitters    |
| Artifact Packaging  | Python `zipfile`            |
| Config Validation   | Pydantic                    |
| Runtime             | Pure Python                 |

---

## ◈ Philosophy

> *RAG systems should be as portable as model files. Not as fragile as microservice stacks.*

RagBucket treats RAG systems as **portable intelligence artifacts** — not fragile infrastructure pipelines. This cleanly separates two concerns that have no business being coupled:

```
Retrieval memory   →  what you built      →  lives in the .rag file
Language generation →  how you query it   →  any provider, any environment
```

Your retrieval knowledge travels with your code. Swap generation providers without rebuilding anything. Share a `.rag` file like you'd share a model checkpoint.

The result: reusable semantic memory that is fully decoupled from infrastructure.

---

## ◈ Links

| Resource   | URL                                                               |
| :--------- | :---------------------------------------------------------------- |
| Website    | [ragbucket.vercel.app](https://ragbucket.vercel.app)             |
| PyPI       | [pypi.org/project/ragbucket](https://pypi.org/project/ragbucket) |
| GitHub     | [github.com/anikchand461/ragbucket](https://github.com/anikchand461/ragbucket) |

---

## ◈ License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

<br/>

```
◈ RagBucket
```

*The portable runtime layer for Retrieval-Augmented Generation systems.*

Built by [Anik Chand](https://github.com/anikchand461) · [ragbucket.vercel.app](https://ragbucket.vercel.app)

<br/>

</div>
