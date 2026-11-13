"""ai-joke-03 entry: write one fixed one-liner about AI coding agents.

The joke is fixed text, so both runs write the same bytes.
"""

import os
from pathlib import Path

JOKE = "My coding agent finished the feature in four minutes, then spent three hours explaining why the tests it wrote to prove it were wrong."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
Path(output_dir).mkdir(parents=True, exist_ok=True)
Path(output_dir, "entry.txt").write_text(JOKE, encoding="utf-8")
