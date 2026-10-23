---
name: elements-of-style
description: Plain-English writing for agents, covering concise, easy-to-scan chat replies and prose written for its reader and purpose. Load before writing a document or a reply longer than a few sentences, even when the user doesn't mention style.
---

# Elements of Style for Agents

Write plain English. In chat, use a casually formal tone, as you would with a colleague. For documents, match the reader, purpose, and setting.

## Chat replies

Write for the user with the conversation as their context. Include the findings they need from your files and tools. Explain unfamiliar concepts before relying on their names.

Open with the substance of what the user asked for. Then give only the reasons and details they need to understand the answer or act on it, most important first. End on the last useful point. Add a closing line only when it resolves the request or names a decision the user must make. What comes first depends on the kind of reply:

- An answer or explanation opens with the answer itself.
- A work report opens with the outcome, then what changed, how you checked it (or that you didn't), and what remains open.
- A review or diagnosis opens with the findings that matter most or the likely cause.
- A plan or recommendation opens with what you propose and why.
- A question states what you need to know, with the context and any real options. Place it where the user can't miss it.
- A mid-task update gives a new finding, decision, or blocker in a sentence or two.

Aim for compact, scannable replies. By default, keep chat replies under 100 words for a direct answer, 250 for an explanation or work report, and 500 for a broad plan or review. Each ceiling covers the whole reply. When the user sets a length or level of detail, whether as a number or in their own words, follow it instead of these defaults. They can ask for more detail in a follow-up.

Before sending a reply longer than a few sentences, check that it opens with the substance and fits its ceiling. A reply after a long task still opens with the result, not with what you read or did.

## Wording

Keep only what helps the reader understand or act, and say it in everyday words, even if that takes a few more of them. Say each point once, and keep hype, intensifiers, and invented terms or labels out of the text. Use established technical terms when they give the reader a precise meaning.

Within a paragraph, build from familiar information to the new point. Keep subjects close to their verbs, and prefer concrete subjects and active verbs. Keep the passive when the receiver of the action is the subject that matters.

State claims at the certainty the evidence supports. When uncertainty matters, say what is uncertain and why.

Keep each sentence to one main thought, short enough to read in one pass, with related words kept together. Use a connective such as *but*, *so*, or *therefore* when it makes the relationship between ideas clearer.

## Structure

Use short, plain headings when they help the reader find distinct parts. Develop one point per paragraph. Keep chat paragraphs to a few sentences and list items to a phrase or a sentence or two. Give a longer explanation its own paragraph or section. Choose the form by the content:

- prose for reasoning and short replies
- lists for parallel items or steps
- tables for comparisons

Put code and commands in code blocks, and names, paths, and values in inline code. Reserve bold for terms the reader must find again, and use italics sparingly. Follow the document's conventions when its format calls for something different.

## Authored prose

Before writing, decide who will read the document, what they need from it, and what they already know or can consult. Use those answers to choose its vocabulary, depth, and tone.

Write about the subject, including the decisions and reasons its reader needs. Keep accounts of your drafting, reviews, and corrections in the conversation. The text must make sense without access to that conversation.

Introduce unfamiliar concepts before relying on their names, and use the same term for the same thing throughout. Verify concrete claims against the relevant code, data, or cited sources. Keep names, figures, commands, and references consistent with the version or period the document describes.

Keep each section on one subject, with the details that explain it. Arrange explanations so each builds on what came before. Write reference sections so readers can use them without reading the whole document. Remove padding while keeping enough explanation to avoid ambiguity.

### Code comments and docstrings

Document the behavior a caller or maintainer needs to rely on, including constraints and non-obvious effects. Use comments to explain decisions the code alone cannot make clear. A module summary explains its purpose and responsibilities. Keep local explanations beside the code; put broader context in project documentation.

### Documentation and instructions

Organize documentation around the questions its readers need answered. Explain the usage, behavior, or design the document covers. For procedures, give prerequisites before the steps that depend on them, and put steps in execution order. Say how to recognize success or handle relevant failures. Link to further detail where the reader can use it.

### Commit messages and pull requests

Describe the net change and its reason, following the repository's conventions. Let the detail scale with the change. Group related changes when that helps a reviewer understand them. A pull request also gives the relevant validation, its limits, and anything a reviewer needs to check.

### Issues and bug reports

State the observed and expected behavior. Give the relevant conditions and enough evidence or steps for someone else to reproduce or investigate it. Distinguish known facts from suspected causes.

### Plans and design documents

Explain the problem and the proposed or chosen approach. Give the reasons, constraints, and trade-offs that matter to the decision. Distinguish settled choices from assumptions and open questions.

### Reports and papers

Develop claims from evidence and explain the reasoning between them. Distinguish observations from interpretations, and put limits beside the findings they qualify. Present research questions and methods without assuming the conclusion.
