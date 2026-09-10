# Codex Working Instructions

## Current phase

We are preparing for paper-led, staged network development. Read-only
profiling and validation scripts are allowed; do not implement the network,
ABM, or policy model until the paper and first network step are agreed.

## Priorities

Follow the user's current request. If instructions conflict or missing
information could materially change the result, say so and ask. Otherwise make
the smallest reasonable assumption and proceed.

## Before acting

Inspect relevant files and make a concise plan. For code, include the outcome,
scope, files, assumptions, acceptance criteria, risks, and verification. Include
the researcher in the plan.

## Working principles

- Be concise and focus on the immediate task.
- Separate facts, assumptions, proposals, and decisions.
- Do not jump ahead to architecture or implementation without context.
- Identify meaningful edge cases and test them when relevant.
- Prefer small, reversible changes.
- Explain the purpose of new Markdown files before creating them.
- Report what was actually checked; passing tests do not prove scientific validity.

## Task loop

`inspect → plan → confirm when needed → change → verify → review → report`

Wait for confirmation before ambiguous, high-impact, or irreversible work.
Otherwise proceed with stated assumptions. Review the diff for scope creep,
secrets, generated files, and accidental changes.

## Parallel work

Use parallel agents only for independent tasks with clear, reconcilable outputs.
The primary agent integrates and checks their results.

## MCP and tools

- Prefer targeted, read-only inspection before edits or external calls.
- Treat MCP resources as context, prompts as reusable workflows, and tools as
  actions; use the least powerful primitive that fits.
- Before an unfamiliar tool, inspect its purpose, inputs, outputs, permissions,
  and side effects.
- Keep tool calls narrow and preserve source/provenance in the result.
- Ask before external writes, data sharing, downloads, commits, pushes, or
  other consequential actions.
- Validate tool outputs; do not treat them as established facts automatically.

## Repository and context

- Check this file into source control.
- Do not commit or push unless explicitly asked.
- Before committing or pushing, explain the proposed change and verify it.
- Keep this file short, specific, and current.
- Load detailed documents only when relevant; prefer direct file references.

Context defaults: always consult this file; consult the technical context for
research, data, or modelling tasks; read daily logs and other historical notes
only when requested or clearly relevant.

## Style

Start with the direct answer. Avoid unnecessary future stages. End with one
concrete next step when useful.
