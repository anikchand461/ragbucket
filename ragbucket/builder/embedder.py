# This file defines the embedding engine
# of the RAG pipeline.


# Import the SentenceTransformer wrapper
# used for generating semantic embeddings.
from sentence_transformers import SentenceTransformer


# Import the embedding model configuration
# from the global constants file.
from ragbucket.constants import EMBEDDING_MODEL


# Embedder class responsible for converting
# text chunks into semantic vector embeddings.
class Embedder:

    def __init__(self):

        # Load the embedding model specified
        # in constants.py
        self.model = SentenceTransformer(
            EMBEDDING_MODEL
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
