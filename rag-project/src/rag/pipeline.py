"""Wires all pipeline stages together."""

from rag.chunking.text_chunker import chunk_text
from rag.embeddings.embedder import embed_texts
from rag.generation.llm import generate_answer
from rag.generation.prompt_builder import build_prompt
from rag.generation.prompt_chunker import chunk_prompt
from rag.ingestion.pdf_loader import load_pdf
from rag.retrieval.retriever import retrieve
from rag.vectorstore.store import add_chunks


def index_pdf(pdf_path: str) -> None:
    """Stages 1-4: PDF -> text -> chunks -> embeddings -> vector database."""
    text = load_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = embed_texts(chunks)
    add_chunks(chunks, embeddings)


def answer_question(question: str) -> str:
    """Stages 5-6: question -> retrieved chunks -> prompt -> prompt chunks -> answer."""
    context = retrieve(question)
    prompt = build_prompt(question, context)
    prompt_pieces = chunk_prompt(prompt)
    return generate_answer(prompt_pieces)


def run(pdf_path: str, question: str) -> str:
    """Index the PDF, then answer the question about it."""
    index_pdf(pdf_path)
    return answer_question(question)
