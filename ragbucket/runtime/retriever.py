# This file defines the semantic retrieval engine
# of the runtime pipeline.


# Import NumPy for vector conversion.
import numpy as np


# Import the globally cached embedding model.
from ragbucket.runtime.models import embedding_model


# Retriever class responsible for:
# - embedding user queries
# - performing semantic search
# - retrieving relevant chunks
class Retriever:

    # Retrieve the most relevant chunks
    # for a given user query.
    def retrieve(
        self,
        query: str,
        index,
        chunks,
        top_k: int = 3
    ):

        # Convert the user query into
        # a semantic vector embedding.
        query_embedding = embedding_model.encode(
            [query]
        )

        # Convert embeddings into float32 format
        # required by FAISS.
        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        # Perform semantic similarity search.
        #
        # Returns:
        # - distances
        # - matching indices
        distances, indices = index.search(
            query_embedding,
            top_k
        )

        # Retrieve matching chunks using
        # the returned indices.
        retrieved_chunks = [
            chunks[i]
            for i in indices[0]
        ]

        return retrieved_chunks
