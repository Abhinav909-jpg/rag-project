# RAG Project

A Retrieval-Augmented Generation (RAG) pipeline built for a university project.
It splits PDFs into chunks, stores them in a vector database, retrieves the most
relevant chunks for a question, splits long prompts into chunks, and sends them to
a language model to produce an answer.

## Pipeline

```
PDF ──► load text ──► chunk ──► embed ──► vector DB
                                             │
question ──► embed ──► retrieve top-k chunks ┘
                           │
                           ▼
              build prompt ──► prompt chunking ──► LLM ──► answer
```

| Stage | Folder | What lives there |
|-------|--------|------------------|
| 1. Ingestion | `src/rag/ingestion/` | Reading PDFs and extracting text |
| 2. Chunking | `src/rag/chunking/` | Splitting document text into chunks |
| 3. Embeddings | `src/rag/embeddings/` | Turning chunks and questions into vectors |
| 4. Vector database | `src/rag/vectorstore/` | Storing and searching vectors |
| 5. Retrieval | `src/rag/retrieval/` | Finding the best chunks for a question |
| 6. Generation | `src/rag/generation/` | Prompt building, prompt chunking, calling the model |
| Orchestration | `src/rag/pipeline.py` | Wires all stages together |

## Project structure

```
rag-project/
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── .env.example
├── .gitignore
├── data/
│   ├── raw/            # input PDFs (not committed)
│   └── processed/      # chunks, cached embeddings (not committed)
├── docs/
│   └── architecture.md
├── notebooks/          # experiments
├── scripts/
│   └── run_pipeline.py # command line entry point
├── src/rag/
│   ├── config.py
│   ├── pipeline.py
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── retrieval/
│   └── generation/
└── tests/
```

## Setup

```bash
git clone <repo-url>
cd rag-project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env     # then fill in your values
```

## Usage

```bash
python scripts/run_pipeline.py --pdf data/raw/yourfile.pdf --question "Your question here"
```

## Team

| Name | Role |
|------|------|
| TODO | TODO |

## License

TODO: choose a license (ask your professor if one is required).
