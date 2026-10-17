# The Elements of Style for Agents

A concise writing and communication standard for AI coding agents, adapted from William Strunk Jr. and E. B. White's classic *The Elements of Style*. It translates their foundational principles (active voice, positive form, paragraphs as units of composition, omitting needless words) into an opinionated guide that can be used for sustained dialogue in conversations and authored prose. For quick, or small requests, the rules in `AGENTS.md` or `CLAUDE.md` provide a compact snippet you can copy into your project's root instructions without loading the full skill.

## Token Footprint

Each file is small enough to keep in context permanently. Counts use the `o200k_base` tokenizer:

| File | Role | Tokens | Words |
| --- | --- | --- | --- |
| `AGENTS.md` | Standalone snippet | 373 | 305 |
| `SKILL.md` | Full skill | 921 | 715 |

CI checks every file against a ceiling of 2,000 tokens with `scripts/count-tokens.py`.

## Installation

Marketplace plugins install the full skill (`elements-of-style`) for Claude Code and Codex:

### Claude Code

```bash
claude plugin marketplace add sdi2200262/elements-of-style-for-agents
claude plugin install elements-of-style@elements-of-style-for-agents
```

### Codex

```bash
codex plugin marketplace add sdi2200262/elements-of-style-for-agents
codex plugin add elements-of-style@elements-of-style-for-agents
```

### Standalone Snippet

Marketplace plugins do not modify your project's root instructions. If you prefer persistent rules without installing or invoking the skill, copy the contents of [`AGENTS.md`](AGENTS.md) or [`CLAUDE.md`](CLAUDE.md) directly into your repository's root instructions.

## Sources and Adaptation

This work draws on:

- William Strunk Jr., *The Elements of Style*. New York: Harcourt, Brace and Company, 1920.
- William Strunk Jr. and E. B. White, *The Elements of Style*. New York: Macmillan, 1959.

This independent adaptation applies their principles to agent-written communication and prose. The cited books remain separate works.

## License

Dedicated to the public domain under [CC0 1.0 Universal](LICENSE).
