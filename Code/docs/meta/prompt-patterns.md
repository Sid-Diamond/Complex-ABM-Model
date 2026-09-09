# Useful Prompt Patterns

## Explore

“Help me think through this idea. Do not propose code yet.”

## Plan

“Inspect the relevant context first. Before changing anything, make a concise
plan and include: intended outcome, scope, files, assumptions, acceptance
criteria, risks, and verification. Ask grouped questions only where the answer
would materially change the result.”

## Focused task

“The outcome I want is: [outcome]. The reason is: [why]. Work only within:
[scope]. Do not change: [out of scope]. Done means: [acceptance criteria].
First inspect the relevant files and tell me your plan.”

## Structure

“Turn this discussion into a draft Markdown document. Mark uncertainties and
proposals clearly.”

## Critique

“Critique this idea against the stated goal. Identify edge cases, but do not
redesign it yet.”

## Decide

“Give me the main options and trade-offs. Ask any decision-relevant questions,
then recommend one.”

## Test

“Identify the expected behaviour, normal cases, failure modes, and edge cases.
Propose or update meaningful tests before changing the implementation. Run the
proportionate checks and report exactly what passed or remains uncertain.”

## Review

“Review the current diff for correctness, scope creep, missing edge cases,
scientific or security risks, and documentation drift. Do not edit anything;
give findings ordered by severity.”

## Record

“Update the relevant Markdown document with this decision and explain what
changed.”

## Commit or push

“Review the changed files, diff, tests, and documentation. Summarise what would
be committed or pushed, identify any remaining risks, and wait for my explicit
approval before doing it.”

## MCP learning

“Explain what this MCP task does, what information it needs, and how I can
review the result before using it.”
