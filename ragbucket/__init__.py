# Package-level abstraction

# Import the RagBuilder class from:
# ragbucket/builder/builder.py
from ragbucket.builder.builder import RagBuilder
from ragbucket.runtime.runtime import RagRuntime

# Expose RagBuilder as part of the public API.
#
# This allows users to write:
# from ragbucket import RagBuilder
#
# instead of:
# from ragbucket.builder.builder import RagBuilder
__all__ = [
    "RagBuilder",
    "RagRuntime"
]

