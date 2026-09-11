# Technical Context — ABM Labour Displacement Project

> **Exploratory working memory, not a specification.** Candidate methods,
> datasets, mechanisms, and claims remain provisional.

## Aim

Develop a scientifically serious toy model designed to answer similar questions to Maria del Rio-Chanona and Penny Mealy's work on occupational mobility and how ai automation will impact jobs.

The eventual output is a technical follow-up to the article in `article.md`, intended to support useful AI-safety policy discussion and a second EA Forum article. The immediate goal is to build and understand the toy model. Do not claim real-world forecasting or policy effectiveness.

## Research posture

Work data-first and paper-first:

1. read the relevant paper;
2. extract its data, network, assumptions, and calibration;
3. inspect and visualise the relevant transition data;
4. implement the smallest faithful step;
5. verify it against the paper;
6. refactor before extending it.

There are no settled choices yet about the dataset, unit, transition mechanism, AI exposure, ABM structure, policy outcome, or robustness criterion.

The project is also a collaboration and learning process. The researcher wants
visibility into how code is built, not only the final files. Announce new
scripts, explain their purpose and main methods, invite inspection, and give a
rough duration before substantial implementation, debugging, package
installation, or data processing. Provide progress updates during long runs.
Optimise for learning and scientific defensibility as well as speed.

Use independent validation for important calculations, particularly when the
researcher cannot directly inspect the source data. The stopping rule is
convergence across genuinely independent checks, or a clear explanation of why
convergence cannot be established. Do not repeat equivalent checks indefinitely:
record residual uncertainty and move on. Continue checking when a test probes a
different assumption or reveals new information about the data or modelling
problem. A validated workflow is not the same as a fully validated dataset,
model, or conclusion.

Before substantial implementation or debugging, pause for a short methodology
review: does the representation, visualisation, dependency choice, and tool
selection still fit the research question? Avoid becoming highly effective at
improving an unsuitable local approach. A reasonable package installation is
allowed when it is scientifically preferable to a quick inferior substitute.

## Candidate direction

A possible sequence is:

1. construct a directed transition network from occupational or skill data;
2. test whether a DAG representation is justified;
3. use the network to inform a toy ABM;
4. compare policies across uncertain parameters and stochastic futures.

The DAG is a hypothesis. Occupational mobility may contain cycles. Acyclicity requires a defensible temporal, causal, skill-acquisition, or aggregation interpretation.

The policy motivation is Decision Making Under Deep Uncertainty: explore distributions of outcomes across plausible futures rather than assume known probabilities or produce a single forecast.

## Candidate methods

Possible, not required:

- O*NET or other occupational/skill data;
- observed transition data;
- temporal analysis;
- BERTopic, UMAP, or HDBSCAN;
- directed transition networks;
- agent-based modelling;
- exploratory robustness analysis.

Each method must answer a research question. Do not add methods for novelty or visual appeal.

## Keep distinct

- skills, tasks, occupations, and workers;
- exposure, adoption, substitution, displacement, and transition demand;
- similarity networks and observed mobility networks;
- data, assumptions, synthetic mechanisms, and conclusions;
- parameter motivation, calibration, sensitivity, and validation;
- robustness analysis and prediction.

## Current data reality

The local IPUMS-CPS extract contains 6,194,406 person-month records across 56
months (2020-2026), with current occupation (`OCC`) and linked person IDs
(`CPSIDP`). It does not contain a direct previous-year occupation variable.
Linked monthly observations can therefore support an observed month-to-month
transition network, subject to linkage and sampling limitations.

Initial profiling found 1,643,075 valid adjacent-month observations, 124,097
occupation changes, 37,163 distinct changed-occupation edge types, and 526
occupation codes after removing exact duplicate person-month observations.
These are preliminary diagnostics, not validated population estimates.
Validate duplicate handling, CPSIDP linkages, occupation codes, sample
coverage, and survey weights before making substantive claims.

Raw data and local intermediates are under `Data/` and are excluded from Git.

## Current code workflow

`scripts/inspect_ipums.py` audits the extract and creates the local SQLite
probe. `scripts/build_dynamic_networks.py` creates monthly node and edge CSVs.
`scripts/main.py` is the visualisation entry point; edit its `CONFIG` only:
`save=False` opens an interactive Matplotlib slider, while `save=True` writes
one PDF per month without displaying figures. `scripts/network_visualisation.py`
contains the reusable NetworkX and Matplotlib functions. The current layout is
a seeded, weighted aggregate `spring_layout`; monthly edges and node sizes
change while node positions remain fixed.

`scripts/Homophilic CA Simulation and Analysis.py` is retained as deliberate
reference code for scientific methodology and for understanding the researcher's
technical background. It is not evidence that homophily, preferential
attachment, or the cellular-automaton model belongs in the current empirical
pipeline.

Known incompleteness should remain visible: the current network is unweighted,
linkage and occupation-code validity remain to be checked, the visualisation
may not be an appropriate representation for roughly 526--527 categories, and
automated tests are still to be added. These are tracked limitations, not
completed scientific results.

## Cautions

- An O*NET similarity graph is not automatically a mobility network.
- PA and homophily are hypotheses or synthetic mechanisms, not established graph properties.
- Undirected graphs have degree/strength, not in-degree.
- Thresholds require sensitivity analysis.
- Log-log plots do not establish power laws; inspect alternative distributions and finite-sample effects.
- A standard BA graph may be an inappropriate null model.
- Network observations are dependent; any GOF method needs a precise null, statistic, resampling scheme, and validation.
- Exposure scores are not displacement probabilities.
- A complex model is not automatically more useful or predictive.
- Do not assume a DAG because neural networks are often represented as DAGs.

## Proposed methodological contributions

Sid proposes:

1. an analytical distribution for networks involving PA and homophily;
2. a GOF test for dependent, heavy-tailed, finite networks.

Treat these as contributions to derive and validate, not assumptions of the labour-market model.

## Reading and data

Start with:

- [del Rio-Chanona et al. (2021)](https://doi.org/10.1098/rsif.2020.0898): data, mobility network, worker transitions, shock, calibration;
- [Moro et al. (2021)](https://doi.org/10.1038/s41467-021-22086-3): connectivity, matching, shocks, resilience;
- papers most connected to Penny Mealy: data, transition concept, mechanism;
- RAND DMU/DMDU work: robust policy without known probabilities;
- [Eloundou et al. (2023)](https://arxiv.org/abs/2303.10130): potential LLM task exposure, not realised displacement.

Candidate data include O*NET, BLS employment/wage data, observed transition data, and exposure datasets. For any dataset, record source/version, unit, code mapping, missing-data policy, and role.

For each paper, record only: data/unit, network construction, assumptions/calibration, and claims/open questions.

## Next decision

The next task is to validate the linked IPUMS panel and decide whether its
observed transitions are adequate for a first network. Do not choose the full
research question, network threshold, or modelling pipeline before that check.
