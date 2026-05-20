# ragbucket/runtime/providers/openai_provider.py

from openai import OpenAI


class OpenAIProvider:

    def __init__(
        self,
        api_key: str,
        model: str
    ):

        self.client = OpenAI(
            api_key=api_key
        )

        self.model = model

    def generate(
        self,
        query: str,
        context: list[str],
        system_prompt: str | None = None
    ):

        joined_context = "\n\n".join(context)

        prompt = f"""
Answer the question using the provided context.

Context:
{joined_context}

Question:
{query}
"""

        messages = []

        if system_prompt:

            messages.append({
                "role": "system",
                "content": system_prompt
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return completion.choices[0].message.content
