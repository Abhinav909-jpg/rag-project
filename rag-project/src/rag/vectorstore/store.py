"""Vector database wrapper (Chroma, FAISS, or whatever the project uses)."""


def add_chunks(chunks: list[str], embeddings: list[list[float]]) -> None:
    """Save chunks and their embeddings in the vector database.

    TODO (owner: ___): paste your vector database code here.
    """
    raise NotImplementedError


def search(query_embedding: list[float], top_k: int) -> list[str]:
    """Return the `top_k` stored chunks closest to `query_embedding`.

    TODO (owner: ___): paste your similarity search code here.
    """
    raise NotImplementedError
