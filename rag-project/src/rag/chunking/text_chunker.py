"""Split document text into chunks for the vector database."""

from rag import config


def chunk_text(
    text: str,
    chunk_size: int = config.CHUNK_SIZE,
    overlap: int = config.CHUNK_OVERLAP,
) -> list[str]:
    """Split `text` into a list of chunks of about `chunk_size` characters,
    with `overlap` characters shared between neighbouring chunks.

    TODO (owner: ___): paste your document chunking code here.
    """
    raise NotImplementedError
