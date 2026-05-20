class CohereEmbedder:

    def __init__(
        self,
        api_key,
        model
    ):

        try:

            import cohere

        except ImportError:

            raise ImportError(
                "\n"
                "Cohere embedding support requires:\n\n"
                "pip install cohere\n\n"
                "OR\n\n"
                "uv add cohere\n"
            )

        self.client = cohere.Client(
            api_key
        )

        self.model = model

    def embed(self, texts):

        response = self.client.embed(
            texts=texts,
            model=self.model,
            input_type="search_document"
        )

        return response.embeddings
