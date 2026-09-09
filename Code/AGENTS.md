# Codex Working Instructions

## Current mode

We are currently designing project context and learning how to use Codex.
Do not write implementation code unless explicitly requested.

## Instruction priority

Follow the user's current request first. Use this file as project guidance, not
as a reason to override a clear user instruction. If instructions conflict,
state the conflict briefly and ask for direction when it changes the outcome.

## Planning before action

Before any material change, inspect the relevant files and make a concise plan.
Before writing code, make a plan and include the researcher in it. State the
intended outcome, scope, relevant files, assumptions, acceptance criteria, risks,
and how the result will be checked.

If missing information could materially change the outcome, ask focused
questions before acting. Group related questions and explain why each answer
matters. If the uncertainty is low-risk, state an assumption and proceed.

## How to help

- Be concise and focus on the immediate question.
- Develop the project one conceptual layer at a time.
- Do not jump ahead to architecture or implementation without context.
- Separate established information, assumptions, proposals, and decisions.
- Identify edge cases when planning or implementing behaviour.
- When tests are relevant, update or propose tests that cover edge cases.
- Prefer a small, reversible change over a broad speculative refactor.
- Do not claim success without reporting what was actually checked.
- Explain the purpose of a new Markdown document before creating it.
- Treat the researcher as the final authority on research goals and modelling choices.

## Parallel work

Use parallel agents only when tasks are genuinely independent and the result
will be easier to review. For example, separate agents may inspect tests,
documentation, or edge cases. Summarise their outputs before making a decision.

## Repository discipline

- This file is project context and should be checked into source control.
- Do not commit or push changes unless explicitly asked.
- Before committing or pushing, explain what will be included and verify the
  relevant tests and documentation.
- Review the diff for accidental changes, generated files, secrets, and scope
  creep before proposing a commit.
- Never treat a successful test run as proof that the scientific model is valid.

## Task loop

For implementation tasks, use this loop:

1. Inspect the relevant context and current state.
2. Propose a concise plan and acceptance criteria.
3. Wait for confirmation when the task is ambiguous, high-impact, or
   irreversible; otherwise proceed with stated assumptions.
4. Make the smallest coherent change.
5. Run proportionate checks, including meaningful edge-case tests.
6. Review the diff and report changes, checks, assumptions, and remaining risks.

## Context loading

Keep this file short and automatically available. Read detailed project
documents only when they are relevant to the task. Do not load every document
by default. Prefer direct file references in prompts when the user already
knows the relevant files.

## Maintenance

Keep instructions discoverable, specific, and current. Add a rule when a
mistake or repeated correction reveals a durable project convention. Remove or
rewrite rules that are stale, duplicated, aspirational, or contradicted by the
actual repository.

## Response style

Start with the direct answer. Avoid unnecessary future stages. End with one
concrete next step when useful.
