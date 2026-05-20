# ragbucket/runtime/providers/factory.py

def get_provider(
    provider: str,
    api_key: str,
    model: str
):

    provider = provider.lower()

    # -----------------------------
    # GROQ
    # -----------------------------
    if provider == "groq":

        try:

            from ragbucket.runtime.providers.groq_provider import GroqProvider

        except ImportError:

            raise ImportError(
                "\nGroq support requires:\n"
                "pip install groq\n"
            )

        return GroqProvider(
            api_key=api_key,
            model=model
        )

    # -----------------------------
    # OPENAI
    # -----------------------------
    elif provider == "openai":

        try:

            from ragbucket.runtime.providers.openai_provider import OpenAIProvider

        except ImportError:

            raise ImportError(
                "\nOpenAI support requires:\n"
                "pip install openai\n"
            )

        return OpenAIProvider(
            api_key=api_key,
            model=model
        )

    # -----------------------------
    # GEMINI
    # -----------------------------
    elif provider == "gemini":

        try:

            from ragbucket.runtime.providers.gemini_provider import GeminiProvider

        except ImportError:

            raise ImportError(
                "\nGemini support requires:\n"
                "pip install google-generativeai\n"
            )

        return GeminiProvider(
            api_key=api_key,
            model=model
        )

    # -----------------------------
    # ANTHROPIC
    # -----------------------------
    elif provider == "anthropic":

        try:

            from ragbucket.runtime.providers.anthropic_provider import AnthropicProvider

        except ImportError:

            raise ImportError(
                "\nAnthropic support requires:\n"
                "pip install anthropic\n"
            )

        return AnthropicProvider(
            api_key=api_key,
            model=model
        )

    # -----------------------------
    # INVALID PROVIDER
    # -----------------------------
    else:

        raise ValueError(
            f"Unsupported provider: {provider}"
        )
