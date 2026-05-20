from ragbucket import RagBuilder
from ragbucket import RagConfig

config = RagConfig(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2"
)

builder = RagBuilder(
    config=config
)

builder.build(
    doc_path="docs",
    op_path="artifacts/demo.rag"
)
