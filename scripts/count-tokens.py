#!/usr/bin/env python3
"""Token counter and validator for Elements of Style for Agents."""

import argparse
import sys
from pathlib import Path

DEFAULT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "claude/skills/elements-of-style/SKILL.md",
    "codex/skills/elements-of-style/SKILL.md",
]


def count_tokens(text: str, encoding_name: str = "o200k_base") -> int:
    import tiktoken

    enc = tiktoken.get_encoding(encoding_name)
    return len(enc.encode(text))


def main() -> int:
    parser = argparse.ArgumentParser(description="Count and validate tokens.")
    parser.add_argument("files", nargs="*", default=DEFAULT_FILES, help="Files to measure")
    parser.add_argument("--encoding", default="o200k_base", help="Tokenizer encoding (default: o200k_base)")
    parser.add_argument("--max-tokens", type=int, default=None, help="Fail if any skill or snippet exceeds limit")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    files_to_check = []
    for f in args.files:
        p = repo_root / f if not Path(f).is_absolute() else Path(f)
        if p.exists() and p.is_file():
            files_to_check.append(p)

    if not files_to_check:
        print("No files found to measure.", file=sys.stderr)
        return 1

    print(f"Tokenizer: {args.encoding}")
    print(f"{'File':<40} | {'Tokens':<8} | {'Words':<8} | {'Chars':<8}")
    print("-" * 72)

    failed = False
    for p in files_to_check:
        rel_path = p.relative_to(repo_root) if p.is_relative_to(repo_root) else p
        content = p.read_text(encoding="utf-8")
        tokens = count_tokens(content, args.encoding)
        words = len(content.split())
        chars = len(content)
        print(f"{str(rel_path):<40} | {tokens:<8} | {words:<8} | {chars:<8}")

        if args.max_tokens and tokens > args.max_tokens:
            print(f"ERROR: {rel_path} exceeded limit ({tokens} > {args.max_tokens})", file=sys.stderr)
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
