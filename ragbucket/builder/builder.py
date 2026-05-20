from numpy.distutils.lib2def import output_def
import json 

from ragbucket.builder.chunker import Chunker
from ragbucket.builder.indexer import Indexer
from ragbucket.builder.packager import Packager

from ragbucket.constants import ARTIFACT_VERSION
from ragbucket.utils.file_utils import get_text_files
from ragbucket.schemas.config import RagConfig
from ragbucket.embeddings.factory import get_embedder


class RagBuilder:

    def __init__(self, config: RagConfig | None = None):

        if config is None:
            config = RagConfig()

        self.config = config
        self.chunker = Chunker(config)
        self.embedder = get_embedder(
            provider=config.embedding_provider,
            model=config.embedding_model,
            api_key=config.embedding_api_key
        )
        self.indexer = Indexer()
        self.packager = Packager()

    def build(self, doc_path, op_path):
        
        print("\nloading documents ...\n")
        files = get_text_files(doc_path)

        all_chunks = []

        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()

            chunks = self.chunker.chunk(text)
            all_chunks.extend(chunks)

        print(f"Generated {len(all_chunks)} chunks")

        embeddings = self.embedder.embed(all_chunks)

        print("embeddings generated")

        index = self.indexer.build_index(embeddings)

        manifest = {

            "artifact_version": ARTIFACT_VERSION,

            "vector_store": "faiss",

            "created_by": "ragbucket",

            "config": {

                # --------------------------------
                # EMBEDDING CONFIG
                # --------------------------------
                "embedding_provider": self.config.embedding_provider,

                "embedding_model": self.config.embedding_model,

                # --------------------------------
                # CHUNKING CONFIG
                # --------------------------------
                "chunk_size": self.config.chunk_size,

                "chunk_overlap": self.config.chunk_overlap,

                # --------------------------------
                # RETRIEVAL CONFIG
                # --------------------------------
                "top_k": self.config.top_k
            }
        }

        self.packager.package(
            output_path=op_path,
            chunks=all_chunks,
            index=index,
            manifest=manifest
        )

