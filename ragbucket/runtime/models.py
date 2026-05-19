from sentence_transformers import SentenceTransformer

from ragbucket.constants import EMBEDDING_MODEL


# Global cached embedding model
embedding_model = SentenceTransformer(
    EMBEDDING_MODEL
)
