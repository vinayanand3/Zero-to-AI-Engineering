from pathlib import Path
import datetime as dt
import json
import re
import unicodedata


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "AI series"
DEST = ROOT / "src" / "content" / "posts"


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.replace("&", " and ")
    ascii_text = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-")
    return ascii_text.lower()


def yaml_string(value):
    return json.dumps(value, ensure_ascii=False)


def clean_text(value):
    value = value.replace("\u00a0", " ")
    value = value.replace(" ", " ")
    value = value.replace("—", "-")
    return value


def extract_title(filename_title, content):
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return filename_title


def description_from_body(body):
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block.startswith("#") or block == "---":
            continue
        block = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", block)
        block = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block)
        block = re.sub(r"[*_`>#-]", "", block)
        block = re.sub(r"\s+", " ", block).strip()
        if block:
            return block[:157].rstrip() + "..." if len(block) > 160 else block
    return ""


def remove_first_h1(content):
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[:index] + lines[index + 1 :]).lstrip() + "\n"
    return content


def season_for(order):
    return ((order - 1) // 12) + 1


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    converted = []

    for source_path in sorted(SOURCE.glob("*.md")):
        match = re.match(r"^(\d{2})\.\s+(.+)\.md$", source_path.name)
        if not match:
            continue

        order = int(match.group(1))
        filename_title = match.group(2).replace("_", ": ").strip()
        raw = clean_text(source_path.read_text(encoding="utf-8"))
        title = clean_text(extract_title(filename_title, raw))
        body = remove_first_h1(raw)
        slug = f"{order:02d}-{slugify(title)}"
        description = description_from_body(body)
        pub_date = (dt.date(2026, 1, 1) + dt.timedelta(days=order - 1)).isoformat()

        frontmatter = "\n".join(
            [
                "---",
                f"title: {yaml_string(title)}",
                f"description: {yaml_string(description)}",
                f"order: {order}",
                f"season: {season_for(order)}",
                f"slug: {yaml_string(slug)}",
                f"pubDate: {yaml_string(pub_date)}",
                "---",
                "",
            ]
        )

        dest_path = DEST / f"{slug}.md"
        dest_path.write_text(frontmatter + body, encoding="utf-8")
        converted.append(dest_path.name)

    print(f"Converted {len(converted)} posts into {DEST}")


if __name__ == "__main__":
    main()
