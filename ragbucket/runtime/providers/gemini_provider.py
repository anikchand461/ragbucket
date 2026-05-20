# ragbucket/runtime/providers/gemini_provider.py

import google.generativeai as genai


class GeminiProvider:

    def __init__(
        self,
        api_key: str,
        model: str
    ):

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            model
        )

    def generate(
        self,
        query: str,
        context: list[str],
        system_prompt: str | None = None
    ):

        joined_context = "\n\n".join(context)

        prompt = f"""
{system_prompt if system_prompt else ""}

Answer the question using the provided context.

Context:
{joined_context}

Question:
{query}
"""

        response = self.model.generate_content(
            prompt
        )

        return response.text
