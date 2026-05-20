class LocalEmbedder:

    def __init__(self, model_name):

        try:

            from sentence_transformers import SentenceTransformer

        except ImportError:

            raise ImportError(
                "\n"
                "Local embedding support requires:\n\n"
                "pip install sentence-transformers\n\n"
                "OR\n\n"
                "uv add sentence-transformers\n"
            )

        self.model = SentenceTransformer(
            model_name
        )

    def embed(self, texts):

        return self.model.encode(
            texts,
            show_progress_bar=True
        )
