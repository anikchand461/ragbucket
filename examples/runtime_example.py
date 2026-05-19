from ragbucket import RagRuntime

system_prompt = """you are Anik's personal chatbot. you know all things about anik.
If anyone asks about the resume of anik please share the details as required.
keep the answers super simple and very short and crisp
"""

rag = RagRuntime(
    rag_path = "artifacts/demo.rag",
    api_key = "groq_api_key",
    model = "llama-3.1-8b-instant",
    system_prompt=system_prompt
)

response = rag.ask("percentage of anik???")

print(response)
