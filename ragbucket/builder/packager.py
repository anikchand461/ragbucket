"""
This file defines the packaging engine
of the RAG pipeline.

Its responsibility is:
- serializing RAG components
- saving vector memory
- storing metadata
- generating the final portable .rag artifact
"""

# Import JSON for storing chunks and metadata.
import json


# Import zipfile for packaging the final
# .rag artifact as a compressed archive.
import zipfile


# Import Path for clean filesystem path handling.
from pathlib import Path


# Import FAISS for serializing the vector index.
import faiss


# Packager class responsible for converting
# pipeline outputs into a portable .rag artifact.
class Packager:

    # Package all RAG components into a .rag file.
    def package(self, output_path, index, chunks, manifest):

        # Create a temporary staging directory
        # used for assembling artifact files.
        temp_dir = Path("temp_rag")

        # Create the directory if it does not exist.
        temp_dir.mkdir(exist_ok=True)

        # Save the FAISS vector index into the
        # temporary artifact directory.
        #
        # This stores the searchable semantic memory
        # of the RAG system.
        faiss.write_index(index, str(temp_dir / "vectors.faiss"))

        # Store all chunked document text
        # inside chunks.json
        with open(temp_dir / "chunks.json", "w") as f:
            json.dump(chunks, f, indent=2)

        # Store artifact metadata and configuration
        # inside manifest.json
        with open(temp_dir / "manifest.json", "w") as f:
            json.dump(manifest, f, indent=2)

        # Create the final .rag archive.
        #
        # ZIP_DEFLATED enables compression
        # to reduce artifact size.
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:

            # Iterate through all generated files
            # inside the temporary directory.
            for file in temp_dir.iterdir():

                # Add each file into the .rag archive.
                #
                # arcname=file.name ensures that only
                # clean filenames are stored inside
                # the artifact instead of full paths.
                zipf.write(file, arcname=file.name)

        # Display successful artifact creation message.
        print(f"\nCreated {output_path}")
