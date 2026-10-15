# Contributing

## Workflow

1. Never push directly to `main`.
2. Create a branch for your piece of work: `git checkout -b feature/<short-name>`
   (examples: `feature/pdf-loader`, `feature/prompt-chunking`).
3. Commit small and often with clear messages.
4. Push your branch and open a Pull Request.
5. At least one teammate reviews before merging.

## Who works where

Each pipeline stage lives in its own folder under `src/rag/`, so teammates can work
on different stages without editing the same files. Agree on who owns which stage
and write it in the README team table.

## Rules

- Do not commit `.env`, API keys, PDFs, or vector database files.
- Add a test in `tests/` for any logic you write.
- Keep functions small, with a docstring saying what goes in and what comes out.
