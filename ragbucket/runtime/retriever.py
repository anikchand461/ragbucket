# This file defines the semantic retrieval engine
# of the runtime pipeline.


# Import NumPy for vector conversion.
import numpy as np


# Import the globally cached embedding model.
from ragbucket.embeddings.factory import get_embedder


# Retriever class responsible for:
# - embedding user queries
# - performing semantic search
# - retrieving relevant chunks
class Retriever:

    def __init__(self, config: dict):
        self.config = config
        self.model = get_embedder(
            provider=config["embedding_provider"],
            model=config["embedding_model"],
            api_key=config.get("embedding_api_key")
        )

    # Retrieve the most relevant chunks
    # for a given user query.
    def retrieve(
        self,
        query: str,
        index,
        chunks,
        top_k = None
    ):

        if top_k is None:
            top_k = self.config["top_k"]

        # Convert the user query into
        # a semantic vector embedding.
        query_embedding = self.model.embed(
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
