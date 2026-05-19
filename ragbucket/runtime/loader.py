# runtime loader for .rag artifacts 

import json
import zipfile
import tempfile
from pathlib import Path
import faiss

class RagLoader:

    def load(self, rag_path):

        temp_dir = tempfile.mkdtemp()

        with zipfile.ZipFile(rag_path, "r") as zipf:
            zipf.extractall(temp_dir)

            temp_path = Path(temp_dir)

        index = faiss.read_index(
            str(temp_path / "vectors.faiss")
        )

        with open(temp_path / "chunks.json", "r") as f:
            chunks = json.load(f)

        with open(temp_path / "manifest.json", "r") as f:
            manifest = json.load(f)

        return {
            "index" : index,
            "chunks" : chunks,
            "manifest": manifest
        }

