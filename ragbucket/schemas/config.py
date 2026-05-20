from dataclasses import dataclass


@dataclass
class RagConfig:

    embedding_provider: str = "local"

    embedding_model: str = "BAAI/bge-small-en-v1.5"

    embedding_api_key: str | None = None

    chunk_size: int = 512

    chunk_overlap: int = 50

    top_k: int = 3
