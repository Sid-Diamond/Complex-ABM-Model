# Decision Log

This records consequential project decisions, the alternatives considered, the
evidence used, and what would cause us to revisit them. It is a decision record,
not a list of implementation tasks. Exploratory questions and hunches belong
here too; not every investigation must be backchained from a settled theory of
change.

## 2026-09-11 — Use a decision- and exploration-aware workflow

- **Decision:** Every substantial task should state either the decision it
  informs or the exploratory question/hunch it investigates, together with the
  evidence that could change our direction and a stopping condition where
  practical.
- **Reason:** Prevent open-ended validation and local optimisation of an
  unsuitable method without suppressing mathematical exploration, unexpected
  empirical findings, or changes in scientific direction.
- **Revisit if:** The structure becomes burdensome or fails to improve project
  direction.

## 2026-09-11 — Separate validation from scientific adequacy

- **Decision:** Use independent computational checks for important calculations,
  but stop when genuinely independent checks converge or stop producing new
  information. Record residual uncertainty instead of repeating equivalent
  checks.
- **Reason:** The researcher cannot directly inspect all source data, but the
  project’s goal is a defensible model rather than exhaustive auditing of the
  coding agent.
- **Residual uncertainty:** A validated workflow does not establish that the
  inaccessible dataset or modelling assumptions are scientifically adequate.

## 2026-09-10 — Use linked IPUMS-CPS observations for a first empirical network

- **Decision:** Treat linked monthly IPUMS-CPS observations as a candidate source
  for an observed occupation-transition network.
- **Alternatives considered:** O*NET similarity data and JobHop/resume-derived
  transitions.
- **Reason:** IPUMS-CPS provides survey-based observations, person linkages, and
  survey weights, while the alternatives do not directly provide the same
  observed worker-transition basis.
- **Status:** Provisional. Linkage quality, occupation-code comparability,
  survey design, and weighting remain unresolved.
- **Revisit if:** These checks show that monthly transitions are not interpretable
  or useful for the intended toy-model question.

## 2026-09-10 — Define the initial transition unit as adjacent calendar months

- **Decision:** Link the same `CPSIDP` only when observations occur in exactly
  consecutive calendar months. Missing months do not create a link.
- **Reason:** This is a transparent first definition and avoids silently mixing
  variable-length gaps with monthly transitions.
- **Status:** Provisional and unweighted.
- **Revisit if:** Linkage validation or a comparison with the target papers shows
  that this unit is unsuitable.

## 2026-09-10 — Keep two network variants

- **Decision:** Maintain an occupation-only variant excluding `OCC = 0000` and a
  state-inclusive variant retaining `0000` as a labelled state.
- **Reason:** The `0000` category may encode meaningful labour-force or
  out-of-universe states rather than ordinary occupations. Removing it too early
  would hide that modelling question.
- **Status:** Descriptive comparison, not a settled substantive interpretation.

## 2026-09-10 — Keep visual thresholds out of exported data

- **Decision:** Export complete monthly node and edge tables; apply thresholds
  only when visualising.
- **Reason:** This preserves the source data for sensitivity analysis.
- **Status:** Provisional visualisation convention. The full-category network may
  not be the most informative representation for roughly 526–527 categories.

## 2026-09-11 — Pause before choosing the ABM architecture

- **Decision:** Do high-level pen-and-paper work before implementing an ABM, then
  compare modelling recipes from relevant Mealy and del Rio-Chanona papers.
- **Reason:** The project should choose a research question and mechanism before
  choosing a model architecture.
- **Next evidence:** A written statement of the target phenomenon, unit of
  analysis, mechanism, outcome, calibration requirements, and acceptable
  simplifications.

## 2026-09-11 — Keep graph analysis distinct from graph visualisation

- **Decision:** Do not infer that a crowded network diagram makes network science
  unsuitable. Continue to consider graph statistics, communities, selected
  subgraphs, clustered views, dimensionality reduction, and other analyses.
- **Reason:** The scientific interest may lie in linkages and graph structure,
  while a full graph figure may simply be a poor communication device.
- **Status:** Open exploratory direction; methods should be chosen for the
  question and the pattern they can reveal.
