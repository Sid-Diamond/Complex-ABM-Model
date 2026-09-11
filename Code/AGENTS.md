# Codex Working Instructions

## Current phase

The audited first empirical network step is implemented. Current work is
exploratory visualisation and measurement; do not implement an ABM or policy
model until the network definition and paper connection are agreed.

## Priorities

Follow the user's current request. If instructions conflict or missing
information could materially change the result, say so and ask. Otherwise make
the smallest reasonable assumption and proceed.

## Before acting

Inspect relevant files and make a concise plan. For code, include the outcome,
scope, files, assumptions, acceptance criteria, risks, and verification. Include
the researcher in the plan.

For every new script, announce its purpose, main methods, and expected runtime,
then invite the researcher to inspect it. For substantial implementation,
debugging, package installation, or data-processing work, announce the scope
and give a rough time estimate before starting. Send progress updates during
long-running work so the researcher can learn from and supervise the process.

## Working principles

- Be concise and focus on the immediate task.
- Separate facts, assumptions, proposals, and decisions.
- Do not jump ahead to architecture or implementation without context.
- Identify meaningful edge cases and test them when relevant.
- Prefer small, reversible changes.
- Explain the purpose of new Markdown files before creating them.
- Report what was actually checked; passing tests do not prove scientific validity.
- Optimise for both project progress and the researcher's understanding of the
  implementation. Do not silently turn a collaborative task into a long
  autonomous run.
- Before substantial implementation or debugging, briefly reconsider whether
  the method, representation, visualisation, and tool choice still fit the
  research question. Do not locally optimise a fundamentally poor approach.
- A package installation or dependency is justified when it materially improves
  scientific fitness; autonomy concerns alone are not a reason to implement an
  inferior substitute.

## Validation and stopping rules

- Use independent checks for important calculations, especially when the
  researcher cannot directly inspect the underlying data.
- Stop repeating equivalent checks once independent methods converge and no new
  information is emerging. Record the remaining uncertainty, limitations, and
  unresolved alternatives, then move on.
- Continue auditing when a check tests a different assumption, exposes new
  structure, or changes the interpretation. The purpose of auditing is not only
  to confirm numbers but to improve shared understanding of the data and model.
- Be explicit that validation of the workflow does not fully validate an
  inaccessible dataset, model, or scientific conclusion.

## Reference code and incomplete work

- Treat `scripts/Homophilic CA Simulation and Analysis.py` as deliberate
  reference code for scientific methodology and the researcher's technical
  background. It is not automatically a template or a component of the current
  empirical pipeline.
- Track known incomplete, scientifically unsatisfactory, or deferred work
  explicitly. Do not present exploratory code or a passing check as finished
  science.

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
For research-direction work, also consult `docs/meta/Decision Log.md` and
`docs/meta/Open Problems.md` before proposing implementation.

## Style

Start with the direct answer. Avoid unnecessary future stages. End with one
concrete next step when useful.

 ## Evidence standard

  For analytical claims, distinguish facts, calculations, assumptions,
  interpretations, and proposals. Report the source, variables, filters, and
  command behind numerical claims. Use executable invariants, reproducible
  reruns, and independent checks where practical. State what the data cannot
  establish and identify plausible alternative explanations.
