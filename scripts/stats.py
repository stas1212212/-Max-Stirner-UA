#!/usr/bin/env python3
"""Local, reproducible translation statistics. Run: python scripts/stats.py"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
chapters = sorted((root / "translation").glob("*.md"))
for path in chapters:
    text = path.read_text(encoding="utf-8")
    words = re.findall(r"[\w’'-]+", text, flags=re.UNICODE)
    print(f"{path.name}: {len(words)} tokens (approx.), {len(text)} characters")
print(f"Files: {len(chapters)}")
print("Progress is editorial: word counts do NOT measure source coverage.")
