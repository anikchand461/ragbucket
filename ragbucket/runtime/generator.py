from groq import Groq

class Generator:

    def __init__(self, api_key, model):

        self.client = Groq(
            api_key = api_key
        )

        self.model = model

    def generate(self, query, context, system_prompt):

        joined_context = "\n\n".join(context)

        prompt = f"""
            {system_prompt}

            Answer the question using the provided context.

            Context:
            {joined_context}
            Question:
            {query}
        """
        completion = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {
                    "role" : "user",
                    "content" : prompt
                }
            ]
        )

        return completion.choices[0].message.content



