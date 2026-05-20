# ragbucket/runtime/providers/groq_provider.py

from groq import Groq


class GroqProvider:

    def __init__(
        self,
        api_key: str,
        model: str
    ):

        self.client = Groq(
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
