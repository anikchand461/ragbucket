# ragbucket/embeddings/factory.py


def get_embedder(
    provider,
    model,
    api_key=None
):

    provider = provider.lower()

    # -----------------------------------
    # LOCAL EMBEDDINGS
    # -----------------------------------
    if provider == "local":

        from ragbucket.embeddings.local_embedder import LocalEmbedder

        return LocalEmbedder(
            model_name=model
        )

    # -----------------------------------
    # OPENAI EMBEDDINGS
    # -----------------------------------
    elif provider == "openai":

        from ragbucket.embeddings.openai_embedder import OpenAIEmbedder

        return OpenAIEmbedder(
            api_key=api_key,
            model=model
        )

    # -----------------------------------
    # GEMINI EMBEDDINGS
    # -----------------------------------
    elif provider == "gemini":

        from ragbucket.embeddings.gemini_embedder import GeminiEmbedder

        return GeminiEmbedder(
            api_key=api_key,
            model=model
        )

    # -----------------------------------
    # COHERE EMBEDDINGS
    # -----------------------------------
    elif provider == "cohere":

        from ragbucket.embeddings.cohere_embedder import CohereEmbedder

        return CohereEmbedder(
            api_key=api_key,
            model=model
        )

    # -----------------------------------
    # INVALID PROVIDER
    # -----------------------------------
    else:

        raise ValueError(
            f"Unsupported embedding provider: {provider}"
        )
