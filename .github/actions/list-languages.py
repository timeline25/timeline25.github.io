#!/usr/bin/env python3
"""Fetch supported languages from kreier/timeline and generate a markdown language table.

Reads supported_languages.csv from kreier/timeline to find languages with dictionaries,
then fetches each dictionary_XX.csv to extract the version (from the 'version' key row)
and last updated date (from the 'notes' column of the 'pdf_title' row).

Outputs a markdown table to .github/state/timeline25.md and inserts it into README.md
between the defined markers.
"""

import csv
import io
import urllib.request
import sys
import os


REPO_DB = "kreier/timeline"
BRANCH = "main"
LANG_CODES_FILE = "supported_languages.csv"
BASE_URL = f"https://raw.githubusercontent.com/{REPO_DB}/{BRANCH}/db"
SITE_URL = "https://timeline25.github.io"

# README markers (HTML comments — invisible when rendered)
MARKER_START = "<!-- start marker table translations -->"
MARKER_END = "<!-- end marker table translations -->"

STATE_DIR = ".github/state"
STATE_FILE = os.path.join(STATE_DIR, "timeline25.md")


def fetch_raw(url):
    """Fetch raw text content from a URL."""
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        print(f"  Warning: failed to fetch {url}: {e}", file=sys.stderr)
        return None


def fetch_csv(path):
    """Fetch and parse a CSV file from the repo."""
    url = f"{BASE_URL}/{path}"
    content = fetch_raw(url)
    if content is None:
        return None
    reader = csv.reader(io.StringIO(content))
    return list(reader)


def build_table(languages):
    """Build the markdown table rows from a list of (key, lang, language_str) tuples."""
    rows = []
    for key, lang, language_str in languages:
        version = "—"
        last_updated = "—"

        dict_rows = fetch_csv(f"dictionary_{key}.csv")
        if dict_rows:
            for row in dict_rows:
                if len(row) >= 2 and row[0].strip() == "version":
                    version = row[1].strip()
                    break
            for row in dict_rows:
                if len(row) >= 4 and row[0].strip() == "pdf_title" and row[3].strip():
                    last_updated = row[3].strip()
                    break

        lang_link = f"[{language_str}]({SITE_URL}/timeline_{key}.pdf)"
        print_link = f"[link]({SITE_URL}/timeline_{key}_print.pdf)"
        rows.append(f"| {lang_link:<40} | {print_link:<40} | {version:^7} | {last_updated:^12} |")

    rows.sort(key=lambda r: r.split("|")[1].strip().lower())

    header = (
        "| language | print | version | last updated |\n"
        "|----------|:-----:|:-------:|:------------:|\n"
    )
    return header + "\n".join(rows) + "\n"


def update_readme(new_table):
    """Replace the table in README.md between the defined markers."""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("README.md not found, skipping update.", file=sys.stderr)
        return

    lines = content.split("\n")
    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == MARKER_START:
            start_idx = i
        elif stripped == MARKER_END:
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        print("Could not find README markers. Skipping README update.", file=sys.stderr)
        return

    new_lines = lines[:start_idx + 1] + ["", new_table] + lines[end_idx:]
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
    print("README.md updated.")


def main():
    print("Fetching supported languages...")
    rows = fetch_csv(LANG_CODES_FILE)
    if not rows:
        print("Error: Could not fetch supported_languages.csv", file=sys.stderr)
        sys.exit(1)

    # Filter to languages with dictionary (dict=TRUE)
    languages = []
    for row in rows:
        if len(row) >= 3 and row[2].strip().upper() == "TRUE":
            languages.append((row[0].strip(), row[1].strip(), row[14].strip()))

    print(f"Found {len(languages)} languages with dictionaries.")

    print("Generating table...")
    table = build_table(languages)

    os.makedirs(STATE_DIR, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        f.write(table)
    print(f"Table written to {STATE_FILE}")

    update_readme(table)


if __name__ == "__main__":
    main()