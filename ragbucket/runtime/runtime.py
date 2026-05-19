from ragbucket.runtime.loader import RagLoader
from ragbucket.runtime.retriever import Retriever
from ragbucket.runtime.generator import Generator

class RagRuntime:

    def __init__(self, rag_path, api_key, model, system_prompt):

        loader = RagLoader()
        loaded = loader.load(rag_path)

        self.index = loaded["index"]
        self.chunks = loaded["chunks"]
        self.manifest = loaded["manifest"]

        self.retriever = Retriever()
        self.generator = Generator(api_key, model)
        self.system_prompt = system_prompt

    def ask(self, query):
        retrieved_chunks = self.retriever.retrieve(
            query = query,
            index = self.index,
            chunks = self.chunks
        )

        answer = self.generator.generate(
            query = query,
            context = retrieved_chunks,
            system_prompt = self.system_prompt
        )

        return answer
