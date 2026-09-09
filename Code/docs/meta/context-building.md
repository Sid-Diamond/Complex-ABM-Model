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

## Automatic versus lazy context

Automatically loaded context should contain only stable, high-value rules:
behaviour, current phase, safety, repository rules, and document locations.

Load detailed scientific, architectural, experimental, and historical material
only when relevant. This keeps sessions focused and reduces stale or conflicting
instructions.

## Implementation quality loop

Plans should identify expected behaviour, edge cases, tests, and verification.
Use:

`inspect → plan → confirm when needed → change → verify → review → report`

Define a stopping condition: a test command, reproducible experiment, document
review, or explicit reason no automated check exists.

Commits and pushes require an explicit request and final review.

## MCP and parallel agents

Before using an unfamiliar MCP tool, explain what it does, what it needs, what
it may access or change, and how the researcher can review the result.

Use parallel agents only for independent, reconcilable subtasks. The primary
agent remains responsible for integration and verification.

Review these instructions periodically and remove stale or duplicated rules.
