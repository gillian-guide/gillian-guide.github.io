import re
from pathlib import Path

for lang in ("", "ru/"):
    h = Path(f"site/{lang}companion-mods/index.html").read_text(encoding="utf-8")
    i = h.find("Trilogy Characters Fixes</a>")
    seg = re.sub(r"<[^>]+>", " ", h[i:i + 1600])
    text = re.sub(r"\s+", " ", seg)
    print((lang or "en")[-2:], "|", text[-260:])
    print()
