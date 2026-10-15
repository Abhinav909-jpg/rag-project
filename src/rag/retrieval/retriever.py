"""Question in, relevant chunks out."""

from rag import config


def retrieve(question: str, top_k: int = config.TOP_K) -> list[str]:
    """Embed `question`, search the vector database, return the best chunks.

    TODO (owner: ___): paste your retrieval code here (and any re-ranking).
    """
    raise NotImplementedError
