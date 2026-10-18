# The Elements of Style for Agents

A writing and communication standard for AI coding agents, adapted from William Strunk Jr. and E. B. White's *The Elements of Style*. It draws on research by [Chandler and Sweller (1991)](https://doi.org/10.1207/s1532690xci0804_2) on avoiding redundancy and [Kalyuga et al. (2003)](https://doi.org/10.1207/s15326985ep3801_4) on adapting explanation to prior knowledge, aiming for concise, direct, compact responses that are easy to scan.

The same principles guide authored prose, adapted to its audience, purpose, genre, and the user's requirements. The standalone snippet in `AGENTS.md` or `CLAUDE.md` handles short exchanges. The full skill develops the guidance for substantial responses and documents.

## Install

Install the plugin in each assistant you use. Each install adds the
`elements-of-style` skill from the same marketplace.

<details>
<summary><strong>Claude Code</strong></summary>

Run in Claude Code and choose user-wide or project scope when installing:

```text
/plugin marketplace add sdi2200262/elements-of-style-for-agents
/plugin install elements-of-style@elements-of-style-for-agents
```

</details>

<details>
<summary><strong>Codex</strong></summary>

Run in a terminal:

```sh
codex plugin marketplace add sdi2200262/elements-of-style-for-agents
codex plugin add elements-of-style@elements-of-style-for-agents
```

</details>

<details>
<summary><strong>Standalone instructions</strong></summary>

Copy [AGENTS.md](AGENTS.md) or [CLAUDE.md](CLAUDE.md) into your project's
root instructions. The snippet works on its own and asks the agent to load
the full skill, when installed, for substantial responses and documents.
Plugin installation does not change your root instructions.

</details>

## Configure

The word budgets used here are arbitrary defaults. Adjust them to your needs in the
copied snippet or installed skill, or give your preferred length in the conversation.

Plugin updates can replace edits to bundled files. Keep lasting preferences
in your project instructions.

# Token Footprint

The skill and snippet are kept short to save tokens. Counts use the `o200k_base`
tokenizer:

| File | Role | Tokens | Words |
| --- | --- | --- | --- |
| `AGENTS.md` | Standalone snippet | 551 | 454 |
| `SKILL.md` | Full skill | 590 | 486 |

## License

Dedicated to the public domain under [CC0 1.0 Universal](LICENSE).
