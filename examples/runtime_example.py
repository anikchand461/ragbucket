from ragbucket import RagRuntime
import os 
from dotenv import load_dotenv

load_dotenv()

system_prompt = """you are Anik's personal chatbot. you know all things about anik.
If anyone asks about the resume of anik please share the details as required.
keep the answers super simple and very short and crisp
"""

rag = RagRuntime(
    rag_path = "artifacts/demo.rag",
    provider= "groq",
    api_key = os.getenv("GROQ_API_KEY"),
    model = "llama-3.1-8b-instant",
    system_prompt=system_prompt
)

response = rag.ask("tell me the best job profile for Anik? means which job ? which role?")

print(response)
