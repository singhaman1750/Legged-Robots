"""Build a minimal static site from README.md and topics/**/*.md into _site/."""
import html
import os
import re
import shutil
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
TEMPLATE = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
SITE_TITLE = "Legged Robots"


def clean(text: str, is_index: bool) -> str:
    out = []
    for line in text.splitlines():
        if "Back to Dashboard" in line:
            # drop only that link; keep any sibling links (e.g. "← Co-Design Papers")
            line = re.sub(r"\[← Back to Dashboard\]\([^)]*\)\s*·?\s*", "", line).strip()
            if not line:
                continue
        if is_index and line.startswith("[![") or (is_index and line.startswith("# ")):
            continue  # badges and H1 (the template shows the title)
        out.append(line)
    return "\n".join(out)


def rewrite_links(body: str) -> str:
    # internal .md links -> .html (leave external URLs alone)
    return re.sub(
        r'href="(?!https?:|mailto:|#)([^"#]*)\.md(#[^"]*)?"',
        lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"',
        body,
    )


def render(src: Path) -> None:
    rel = src.relative_to(ROOT)
    is_index = rel == Path("README.md")
    raw = src.read_text(encoding="utf-8")
    m = re.search(r"^# (.+)$", raw, re.M)
    title = m.group(1).strip() if m else src.stem
    body = markdown.markdown(
        clean(raw, is_index), extensions=["tables", "fenced_code", "sane_lists"]
    )
    body = rewrite_links(body)

    out = SITE / ("index.html" if is_index else rel.with_suffix(".html"))
    out.parent.mkdir(parents=True, exist_ok=True)
    depth = len(out.relative_to(SITE).parts) - 1
    root = "../" * depth
    page_title = SITE_TITLE if is_index else f"{title} · {SITE_TITLE}"
    heading = "" if is_index else f"<h1>{html.escape(title)}</h1>\n"
    out.write_text(
        TEMPLATE.replace("{{title}}", html.escape(page_title))
        .replace("{{site_title}}", SITE_TITLE)
        .replace("{{root}}", root)
        .replace("{{year}}", str(date.today().year))
        .replace("{{updated}}", date.today().strftime("%B %d, %Y"))
        .replace("{{content}}", body),
        encoding="utf-8",
    )


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    shutil.copy(ROOT / "site" / "style.css", SITE / "style.css")
    (SITE / ".nojekyll").touch()
    pages = [ROOT / "README.md", *sorted((ROOT / "topics").rglob("*.md"))]
    for p in pages:
        render(p)
    print(f"Built {len(pages)} pages into {SITE}")


if __name__ == "__main__":
    main()
