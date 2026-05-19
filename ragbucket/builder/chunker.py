# This file defines the chunking engine
# of the RAG pipeline.


# Import the recursive text chunking utility
# from LangChain.
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Import global chunking configurations
# used by the RecursiveCharacterTextSplitter.
from ragbucket.constants import (
    CHUNK_OVERLAP,
    CHUNK_SIZE
)


# Chunker class responsible for splitting
# raw documents into retrieval-ready chunks.
class Chunker:

    def __init__(self):

        # Initialize the recursive text splitter
        # with predefined chunk settings.
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    # Split input text into overlapping chunks.
    def chunk(self, text):

        return self.splitter.split_text(text)
