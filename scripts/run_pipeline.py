"""Command line entry point.

Usage:
    python scripts/run_pipeline.py --pdf data/raw/yourfile.pdf --question "Your question"
"""

import argparse
import sys
from pathlib import Path

# Make `import rag` work when running this file directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from rag.pipeline import run  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a question about a PDF.")
    parser.add_argument("--pdf", required=True, help="path to the PDF file")
    parser.add_argument("--question", required=True, help="your question")
    args = parser.parse_args()
    print(run(args.pdf, args.question))


if __name__ == "__main__":
    main()
