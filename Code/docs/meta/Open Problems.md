# Open Problems

This is a living register of unresolved scientific, data, and engineering
issues. An item is not complete merely because code exists for it.

## High priority / active exploration

### Explore what the IPUMS graph can reveal

- **Question:** What interesting graph structure, empirical regularity, or
  modelling opportunity is present in the monthly linked occupation data?
- **Possible approaches:** Degree and strength distributions, centrality,
  communities, selected subgraphs, transition matrices, clustered views,
  dimensionality reduction, and comparison with the target papers.
- **Status:** Open exploratory direction. The graph may be useful analytically
  even if a full network diagram is not useful as a figure.

### Validate CPSIDP linkage quality

- **Issue:** A repeated person ID does not by itself establish that the linked
  observations represent the same person reliably.
- **Needed:** Demographic consistency checks and, where appropriate, comparison
  with `CPSIDV` or other CPS linkage information.
- **Risk:** Spurious transitions or missed transitions could alter the network.
- **Priority:** Important eventual validation, but not currently a blocker for
  clearly labelled exploratory toy-model analysis.

### Establish the meaning of `OCC = 0000`

- **Issue:** The category is not an ordinary occupation and may combine
  unemployment, non-participation, missingness, or out-of-universe cases.
- **Needed:** Inspect the relevant CPS documentation and consider `EMPSTAT` and
  `LABFORCE`; determine whether external data are needed.
- **Status:** Keep both variants until this is resolved.
- **Priority:** Important interpretation question, but not currently a blocker
  for clearly labelled exploratory analysis.

### Keep representation choices open

- **Issue:** A graph with roughly 526–527 categories may be difficult to
  interpret, and a network may not be the most useful object for the eventual
  research question.
- **Needed:** Compare graph statistics, aggregate flows, transition matrices,
  clustered views, selected subgraphs, dimensionality reduction, and other
  representations where they reveal something scientifically interesting. A
  crowded diagram does not by itself invalidate graph analysis.

## Medium priority / return later

### Add survey weights

- **Issue:** Current counts are unweighted sample counts, not population
  estimates.
- **Needed:** Determine how weights should enter node sizes, transition counts,
  and probabilities without overstating precision.

### Check occupation-code comparability and missingness

- **Issue:** Codes and coverage may not be stable across the full period.
- **Needed:** Inspect code definitions, year coverage, missingness, and the
  October 2025 gap.
- **Priority:** Preserve explicitly, but do not require resolution before
  beginning useful exploratory analysis.

### Compare transition windows

- **Issue:** Adjacent-month links capture a different process from annual or
  variable-length transitions.
- **Needed:** Analyse alternative windows separately rather than mixing them into
  the initial monthly network.

### Add automated tests

- **Initial invariants:** node shares sum to one by month; transition
  probabilities sum to one by origin/month; missing months create no links;
  deduplication is idempotent; the two variants differ only through `0000`.
- **Status:** Not yet implemented.

## Deferred until direction is clearer

- Choose an ABM architecture.
- Add AI exposure or displacement mechanisms.
- Assume a DAG, preferential attachment, or homophily in the labour network.
- Calibrate policy effects or make forecasting claims.
- Build elaborate visualisations before confirming that the representation is
  useful. This does not defer graph-theoretic analysis merely because a full
  network diagram is crowded.

## Reference material

`scripts/Homophilic CA Simulation and Analysis.py` is reference code for
scientific methodology and the researcher’s technical background. It is not a
commitment to use homophily, preferential attachment, or cellular automata in
the current model.
