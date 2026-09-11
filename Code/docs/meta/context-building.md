# Context-Building Process

For each new idea or task:

1. Understand and briefly summarise it.
2. Identify relevant ambiguity, edge cases, and missing concepts.
3. Ask grouped questions only when answers would change the work.
4. State low-risk assumptions instead of blocking.
5. Suggest the smallest useful document or section.
6. Wait for confirmation before treating a proposal as a decision.

Do not design the complete documentation system before understanding the
project.

## Automatic versus on-demand context

Use a small context hierarchy rather than loading every project document into
every task:

- **Always:** `AGENTS.md` for stable working rules, current phase, safety,
  repository boundaries, and context locations.
- **Research or modelling work:** the technical context prompt.
- **Research-direction work:** the technical context, `Decision Log.md`, and
  `Open Problems.md`.
- **Implementation work:** the relevant scripts and direct documentation only.
- **Historical or audit work:** `Day-logs.md`, `Data Audit.md`, and other meta
  notes when their specific history is relevant.

Load detailed scientific, architectural, experimental, and historical material
on demand. If the user asks for a context audit, inspect the full hierarchy.
This keeps sessions focused, reduces stale or conflicting instructions, and
makes the source of an instruction clear.

Exploratory work may begin with a hunch or question rather than a settled
decision. Record its scope and stopping point when practical; do not use the
context hierarchy as a reason to block low-risk exploration.

## Implementation quality loop

Plans should identify expected behaviour, edge cases, tests, and verification.
Use:

`inspect → plan → confirm when needed → change → verify → review → report`

Define a stopping condition: a test command, reproducible experiment, document
review, or explicit reason no automated check exists.

Commits and pushes require an explicit request and final review.

## MCP and parallel agents

Use the least powerful MCP primitive that fits:

- resources for read-only context or data;
- prompts for reusable user-invoked workflows;
- tools for actions or computation.

Before using an unfamiliar tool, explain its purpose, inputs, outputs,
permissions, side effects, provenance, and review method. Prefer narrow,
read-only calls first. Ask before external writes, data sharing, downloads, or
other consequential actions. Validate tool results instead of treating them as
facts automatically.

Use parallel agents only for independent, reconcilable subtasks. The primary
agent remains responsible for integration and verification.

Review these instructions periodically and remove stale or duplicated rules.
