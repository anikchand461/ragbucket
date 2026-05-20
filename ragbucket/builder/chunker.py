# This file defines the chunking engine
# of the RAG pipeline.


# Import the recursive text chunking utility
# from LangChain.
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Chunker class responsible for splitting
# raw documents into retrieval-ready chunks.
class Chunker:

    def __init__(self, config):

        # Initialize the recursive text splitter
        # with predefined chunk settings.
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap
        )

    # Split input text into overlapping chunks.
    def chunk(self, text):

        return self.splitter.split_text(text)
