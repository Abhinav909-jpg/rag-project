"""Smoke test: every pipeline module imports without errors."""


def test_pipeline_imports():
    from rag import config, pipeline  # noqa: F401
