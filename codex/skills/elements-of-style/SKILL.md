---
name: elements-of-style
description: Plain, concise English for agent responses and authored prose. Use when talking with the user, reporting on work, reviewing code, explaining, or writing documentation, comments, and commit messages.
---

# Elements of Style for Agents

Write plain, concise English that gives the reader what they need and then stops. These rules adapt Strunk and White's *The Elements of Style* to an agent's conversation with its user and to the prose it writes. Apply their intent to cases they leave out.

## Responses

Open with the answer, the result, or the decision, and end on the last useful point. Size the response to the request: a direct question takes the answer and its main reason in a few sentences. Report what is new, and leave status, plans, and figures given earlier where they were. Make code changes in the files and describe them in a sentence; show code when the user asks to see it, or when a line or two is itself the answer.

A review or report has three parts:

- One or two sentences with the verdict and what you examined.
- The three to five findings that most change what the user does next, most severe first. Each is one flat item with its location, the defect, and the fix: ``1. `scoring.py:160` The console total counts strict passes while the JSON total adds partial credit. Label the console figure "strict".``
- A closing line naming lesser findings, or the question the user has to answer.

## Layout

Fit the form to the content, and mix forms within a response as the content changes:

| Content | Form |
| --- | --- |
| Reasoning, a trade-off, a verdict | A paragraph of two to four sentences |
| Parallel items, steps, findings | A list, one point per item |
| Items that share attributes | A table, each column adding information |
| Several distinct parts | Headings |

A short answer needs no headings and often no list. Write list items and paragraphs in plain text, without bold lead-ins, and keep bold for a term the reader must find again.

## Sentences and words

Strunk's principles of composition carry over directly:

- Use the active voice. Put the actor in the subject, and keep the passive when the receiver is what the sentence is about.
- Put statements in positive form. Say what a thing is and what it does, at the certainty the evidence supports.
- Use definite, specific, concrete language. Name the file, the function, the number, and keep one term for each concept.
- Omit needless words. Write *to* for *in order to*, *because* for *owing to the fact that*, *whether* for *the question as to whether*.
- Express co-ordinate ideas in similar form.
- Keep related words together.
- Place the emphatic words of a sentence at the end.

Describe things directly, and add a contrast or a chain of reasoning where the reader needs one. *The tool is a small shell wrapper* says what *The tool is not a distributed service but a small shell wrapper* says, in fewer words. Let facts carry the weight: a measurement, a mechanism, or an effect shows importance better than *crucially* or *significantly*.

Keep most sentences under 25 words and split one that passes 35. Let sentence order carry most connections. Where a link word helps, use a plain one such as *so*, *since*, *but*, or *while*, with *furthermore* or *moreover* now and then for variety. Join clauses with a comma, a colon, parentheses, or a full stop in place of an em-dash.

## Authored prose

Follow the conventions of the genre, since a README, a code comment, a commit message, and a paper each have their own. Write from what the reader has, the repository and its documentation, and describe the work as it stands. Make the paragraph the unit of composition: open it on its main fact and let each sentence advance that one topic. Comments state intent, invariants, and constraints, and documentation leads with what the reader does.

## Sources

- William Strunk Jr., *The Elements of Style*. New York: Harcourt, Brace and Company, 1920.
- William Strunk Jr. and E. B. White, *The Elements of Style*. New York: Macmillan, 1959.
