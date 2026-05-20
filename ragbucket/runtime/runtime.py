from ragbucket.runtime.loader import RagLoader
from ragbucket.runtime.retriever import Retriever
from ragbucket.runtime.providers.factory import get_provider

class RagRuntime:

    def __init__(self, rag_path, provider, api_key, model, system_prompt=None):

        loader = RagLoader()
        loaded = loader.load(rag_path)

        self.index = loaded["index"]
        self.chunks = loaded["chunks"]
        self.manifest = loaded["manifest"]
        self.config = self.manifest["config"]

        self.retriever = Retriever(config=self.config)
        self.generator = get_provider(
            provider=provider,
            api_key=api_key,
            model=model
        )
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
