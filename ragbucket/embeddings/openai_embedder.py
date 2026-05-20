class OpenAIEmbedder:

    def __init__(
        self,
        api_key,
        model
    ):

        try:

            from openai import OpenAI

        except ImportError:

            raise ImportError(
                "\n"
                "OpenAI embedding support requires:\n\n"
                "pip install openai\n\n"
                "OR\n\n"
                "uv add openai\n"
            )

        self.client = OpenAI(
            api_key=api_key
        )

        self.model = model

    def embed(self, texts):

        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )

        return [
            item.embedding
            for item in response.data
        ]
