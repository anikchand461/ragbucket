class VoyageEmbedder:

    def __init__(
        self,
        api_key,
        model
    ):

        try:

            import voyageai

        except ImportError:

            raise ImportError(
                "\n"
                "VoyageAI embedding support requires:\n\n"
                "pip install voyageai\n\n"
                "OR\n\n"
                "uv add voyageai\n"
            )

        self.client = voyageai.Client(
            api_key=api_key
        )

        self.model = model

    def embed(self, texts):

        response = self.client.embed(
            texts,
            model=self.model
        )

        return response.embeddings
