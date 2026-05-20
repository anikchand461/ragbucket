# ragbucket/runtime/providers/anthropic_provider.py

import anthropic


class AnthropicProvider:

    def __init__(
        self,
        api_key: str,
        model: str
    ):

        self.client = anthropic.Anthropic(
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

        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,

            system=system_prompt if system_prompt else "",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return message.content[0].text
