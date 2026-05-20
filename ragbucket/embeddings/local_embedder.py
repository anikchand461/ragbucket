_cached_models = {}


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

        # -----------------------------------
        # LOAD MODEL ONLY ONCE
        # -----------------------------------
        global _cached_models

        if model_name not in _cached_models:
            _cached_models[model_name] = SentenceTransformer(model_name)

        self.model = _cached_models[model_name]

    def embed(self, texts):

        return self.model.encode(texts, show_progress_bar=True)
