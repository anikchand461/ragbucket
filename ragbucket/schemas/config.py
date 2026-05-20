from dataclasses import dataclass

@dataclass
class RagConfig:

    # embedding model used for vector generation 
    embedding_model: str = "BAAI/bge-small-en-v1.5"

    # chunk size for document splitting 
    chunk_size: int = 512
    
    # overlap between consecutive chunks
    chunk_overlap: int = 50
    
    # number of retrieved chunks duting querying 
    top_k: int = 3


