# Useful Prompt Patterns

## Explore

“Help me think through this idea. Do not propose code yet.”

## Plan

“Inspect the relevant context. Before changing anything, make a concise plan
covering outcome, scope, files, assumptions, acceptance criteria, risks, and
verification. Ask only decision-relevant questions.”

## Focused task

“The outcome is: [outcome]. The reason is: [why]. Work only within [scope]. Do
not change [out of scope]. Done means [criteria]. First inspect the files and
show me your plan.”

## Structure / critique / decide

“Turn this discussion into a draft Markdown document; mark uncertainties.”

“Critique this against the stated goal and identify edge cases; do not redesign
it yet.”

“Give the main options and trade-offs, ask decision-relevant questions, then
recommend one.”

## Test / review

“Identify expected behaviour, failure modes, and edge cases. Propose or update
meaningful tests, run proportionate checks, and report uncertainty.”

“Review the diff for correctness, scope creep, missing edge cases, scientific or
security risks, and documentation drift. Do not edit; order findings by severity.”

## Record / commit / MCP

“Record this decision in the relevant Markdown file and explain the change.”

“Review the diff, tests, and documentation. Summarise what would be committed or
pushed, then wait for my explicit approval.”

“Explain this MCP task, its inputs and effects, and how I can review its result.”
