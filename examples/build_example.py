from ragbucket import RagBuilder
from ragbucket import RagConfig

# import os
#
# from dotenv import load_dotenv
#
#
# load_dotenv()


# config = RagConfig(
#
#     embedding_provider="cohere",
#
#     embedding_model="embed-english-v3.0",
#
#     embedding_api_key="cohere_PsVPiWeKIo61TF3dBedeECxgJ2usdn63VKIvygMg0Ae7ue"
# )
#

builder = RagBuilder(
    # config=config
)


builder.build(
    doc_path="docs",
    op_path="artifacts/demo.rag"
)
