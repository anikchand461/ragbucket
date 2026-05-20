class GeminiEmbedder:

    def __init__(
        self,
        api_key,
        model
    ):

        try:

            import google.generativeai as genai

        except ImportError:

            raise ImportError(
                "\n"
                "Gemini embedding support requires:\n\n"
                "pip install google-generativeai\n\n"
                "OR\n\n"
                "uv add google-generativeai\n"
            )

        genai.configure(
            api_key=api_key
        )

        self.genai = genai

        self.model = model

    def embed(self, texts):

        embeddings = []

        for text in texts:

            result = self.genai.embed_content(
                model=self.model,
                content=text
            )

            embeddings.append(
                result["embedding"]
            )

        return embeddings
