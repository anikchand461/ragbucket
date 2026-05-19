# This file defines the vector indexing engine
# of the RAG pipeline.

# Import FAISS for vector similarity indexing and retrieval
import faiss

# Import NumPy for numerical array conversion.
import numpy as np


# Indexer class responsible for converting embeddings into a searchable FAISS index.
class Indexer:

    # Build a FAISS vector index from embeddings.
    def build_index(self, embedding):

        # Convert embeddings into a NumPy float32 array,
        # which is required by FAISS.
        embeddings = np.array(
            embedding,
            dtype="float32"
        )

        # Extract embedding dimensionality.
        #
        # Example:
        # embeddings.shape = (100, 384)
        #
        # meaning:
        # 100 vectors
        # each vector has 384 dimensions
        dimension = embeddings.shape[1]

        # Create a flat L2 distance index.
        #
        # L2 = Euclidean distance similarity search.
        index = faiss.IndexFlatL2(dimension)
        # an empty database table created 

        # Add embeddings into the FAISS index.
        index.add(embeddings)
        # the embeddings are inserted in the database table 

        # Return the searchable vector index.
        return index
