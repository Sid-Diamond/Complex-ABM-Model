# Context-Building Process

This document describes how Codex and the researcher gradually create useful
project context.

For each new idea or task, Codex should:

1. Understand what the researcher is trying to express.
2. Summarise it briefly.
3. Identify relevant ambiguities, edge cases, and missing concepts.
4. Ask questions where the answers would materially change the work. Group
   related questions and explain why they matter.
5. State low-risk assumptions instead of blocking on them.
6. Suggest the smallest useful Markdown document or section.
7. Wait for confirmation before treating a proposal as a decision.

The process is intentionally iterative. Do not design the complete
documentation system before understanding the project.

## Automatic versus lazy context

Automatically loaded context should contain only stable, high-value guidance:

- how Codex should behave;
- current project phase;
- safety and repository rules;
- where relevant documents are located.

Detailed scientific, architectural, experimental, and historical material
should be loaded lazily when a task requires it. This keeps sessions focused and
reduces conflicting or stale instructions.

## Tests and implementation

When implementation begins, planning should identify:

- expected behaviour;
- edge cases;
- tests to add or update;
- how the result will be verified;
- whether independent parallel review would help.

The quality loop is:

```text
inspect → plan → confirm when needed → change → verify → review → report
```

Every implementation plan should define a useful stopping condition. This may
be a test command, a reproducible experiment, a document review, or an explicit
reason why no automated check exists.

Commit and push decisions are separate from implementation. They require an
explicit request and a final review of tests, documentation, and changed files.

## MCP and other tools

MCP tasks should be introduced gradually. Before using an unfamiliar MCP tool,
Codex should explain:

- what the tool does;
- what context it needs;
- what it may change or access;
- how the researcher can review the result.

The researcher is learning the tools as well as the project, so explanations
should be practical and not assume prior MCP knowledge.

## Parallel agents

Parallel agents are a quality and speed tool, not a default requirement. Use
them when subtasks are independent, have clear outputs, and can be reconciled.
Suitable examples include separate reviews for tests, edge cases, scientific
assumptions, or documentation. The primary agent remains responsible for
integrating and checking the results.

## Context review

Review this process and the project instructions periodically. Keep automatic
context short and stable; move detailed or task-specific material into files
that can be loaded only when relevant.
