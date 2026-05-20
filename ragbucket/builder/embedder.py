# This file defines the embedding engine
# of the RAG pipeline.


# Import the SentenceTransformer wrapper
# used for generating semantic embeddings.
from sentence_transformers import SentenceTransformer
from ragbucket.runtime.models import get_embedding_model


# Import the embedding model configuration
# from the global constants file.
# from ragbucket.constants import EMBEDDING_MODEL


# Embedder class responsible for converting
# text chunks into semantic vector embeddings.
class Embedder:

    def __init__(self, config):

        # Load the embedding model specified
        # in constants.py
        self.model = get_embedding_model(
            config.embedding_model
        )

    # Generate embeddings for the given chunks.
    def embed(self, chunks):

        return self.model.encode(

            # Input text chunks
            chunks,

            # Show progress bar during embedding generation
            # for better developer feedback.
            show_progress_bar=True
        )
