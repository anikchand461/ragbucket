from numpy.distutils.lib2def import output_def
import json 

from ragbucket.builder.chunker import Chunker
from ragbucket.builder.indexer import Indexer
from ragbucket.builder.embedder import Embedder
from ragbucket.builder.packager import Packager

from ragbucket.constants import ARTIFACT_VERSION, CHUNK_SIZE, EMBEDDING_MODEL
from ragbucket.utils.file_utils import get_text_files

class RagBuilder:

    def __init__(self):

        self.chunker = Chunker()
        self.embedder = Embedder()
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
            "artifact_version" : ARTIFACT_VERSION,
            "embedding_model" : EMBEDDING_MODEL,
            "chunk_size" : CHUNK_SIZE,
            "vector_store" : "faiss",
            "created_by" : "ragbucket"
        }

        self.packager.package(
            output_path=op_path,
            chunks=all_chunks,
            index=index,
            manifest=manifest
        )

