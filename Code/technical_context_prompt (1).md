# Technical Context — ABM Labour Displacement Project

> **Status: exploratory context, not a settled specification.**
> These ideas were synthesised from an earlier LLM discussion. Treat them as
> hypotheses, possibilities, and questions—not commitments.

## Purpose

Develop a scientifically serious toy model, extending Maria del Rio-Chanona and Penny Mealy's work, that can eventually support a useful AI-safety policy argument and a second EA Forum article.

The project is deliberately open-ended. There are currently no settled claims. The model may eventually study mechanisms, network structure, and robust policy under AI-related labour shocks, but those purposes still need development.

The immediate goal is to build the toy model well. Its usefulness argument can be developed later, in response to MATS feedback and the research context.

## Research orientation

- Primary anchor: Maria del Rio-Chanona and Penny Mealy's work on occupational mobility and automation.
- Intended audience: AI-safety researchers, economists, complexity researchers, thesis readers, and policy audiences.
- Method: an agent-based model informed by empirical occupational or skill data; the ABM is one component of a broader data-analysis and theory-building effort.
- Status: exploratory. No mechanism, dataset, outcome, or policy claim is yet adopted.

## Possible direction

One possible direction is to analyse how skills or occupations change around the release and adoption of AI agents, use that analysis to inform a transition network, and then use the network within a toy ABM to explore adaptation and policy. This is a research direction, not a specification.

Possible ingredients include O*NET or another occupational dataset, topic modelling (possibly BERTopic), UMAP, HDBSCAN, temporal transition analysis, a directed representation, an ABM, and exploratory policy analysis. None is currently required; each must earn its place by answering a research question.

The immediate empirical task is to inspect and visualise transition data before
deciding what the model should represent. A directed acyclic representation is
a working hypothesis because it may help organise transitions and compare
policies. It must remain provisional: real occupational mobility may contain
cycles, and acyclicity would need a defensible temporal, causal, or aggregation
justification.

The policy motivation is decision-making under deep uncertainty: simulate a
complex system, examine distributions of possible outcomes, and identify
policies that remain acceptable across relevant futures. Robustness criteria are
not yet defined.

## Questions about the possible method

- What data captures change over time and the arrival or adoption of AI agents?
- Are skills, tasks, occupations, or clusters the model's basic units?
- Does clustering answer a research question, or only create an attractive map?
- Are transitions directed? A transition graph need not be acyclic; a DAG needs a specific temporal or causal justification.
- If a DAG is imposed, what does its direction mean: time, skill acquisition,
  occupational progression, causal influence, or aggregation?
- Which distributions should be inspected: degree, in-degree, out-degree, path
  length, transition frequency, exposure, recovery, or policy outcomes?
- Does a heavy tail appear in the data, and under which representation and
  scale? Do not assume it before examining the network.
- How will inferred transitions be validated before informing the ABM?
- What does the ABM add beyond network analysis or a dynamical model?
- What data can support calibration rather than merely motivate parameters?

## Important conceptual distinction

An O*NET similarity graph is not automatically a preferential-attachment or homophily network. PA and homophily may be:

1. hypotheses about an observed network;
2. generative mechanisms for synthetic comparison networks; or
3. analytical assumptions for Sid's proposed distributional work.

They must not be presented as properties established by the O*NET construction.

An undirected graph has degree or weighted strength, not in-degree. A directed transition network requires a separate definition and evidence.

## Possible later model layers

### Exposure and shock

Use occupation-level AI exposure as an uncertain input, not as a displacement probability. Exposure, task impact, adoption, substitution, job loss, and transition demand are distinct variables.

Eloundou et al. (2023) measure potential task exposure to LLM capabilities; the paper explicitly does not predict adoption timing. Do not convert its scores directly into job losses.

### Agents and labour dynamics

The model must distinguish workers from occupations. A worker agent may have a current occupation, skills or transition costs, employment status, security or income, and adaptation, retraining, or search behaviour.

Occupations provide structure, vacancies, demand, and transition opportunities; they are not themselves workers. Labour demand, vacancies, matching, timing, and population counts remain unspecified.

### Policy experiments

Policies may eventually be evaluated over parameter uncertainty and stochastic runs. Before implementation, define baseline and intervention scenarios, uncertain parameters, outcomes, replication, sensitivity analysis, and what “robust” means.

The current “better than baseline in 80% of parameter combinations” rule is a placeholder, not a decision criterion.

## Methodological risks to resolve

- A similarity threshold such as 0.7 is arbitrary until sensitivity is shown.
- Log-log histograms do not establish a power law.
- Power-law fitting requires justified support, alternatives, and finite-sample checks.
- A standard BA graph is not automatically an appropriate null model for an O*NET network with fixed attributes and correlations.
- Degree observations in a network are dependent; Sid's proposed GOF method needs a precise null model, statistic, resampling scheme, and validation.
- A skill-similarity graph is not automatically an observed worker-transition network.
- A DAG representation of changing skills may impose directionality that the data does not support.

## Literature to verify and read

1. [del Rio-Chanona et al. (2021), Occupational mobility and automation](https://doi.org/10.1098/rsif.2020.0898) — primary methodological anchor; establish how the mobility network, worker flows, and automation shock are defined.
2. [Moro et al. (2021), Universal resilience patterns in labor markets](https://doi.org/10.1038/s41467-021-22086-3) — distinguish its urban matching model from this project's possible model.
3. [Eloundou et al. (2023), GPTs are GPTs](https://arxiv.org/abs/2303.10130) — exposure measurement; do not interpret exposure as realised displacement.
4. Barabási & Albert (1999) — determine whether PA is an empirical claim, synthetic benchmark, or part of Sid's theory.
5. Alabdulkareem et al. (2018) — assess relevance to the chosen O*NET representation.
6. Epstein & Axtell (1996) — ABM foundations, not labour-market validation.
7. Gupta & Kumar (2026), [Agentic Task Exposure preprint](https://arxiv.org/abs/2604.00186) — emerging input candidate; assess its assumptions and data before use.

Teutloff et al. (2025), del Rio-Chanona et al. (2026), and Pangallo et al. (2024) still need exact citations and a defined role.

## Sid's proposed contribution

Sid proposes:

1. an analytical distribution for networks involving PA and homophily;
2. a goodness-of-fit test for dependent, heavy-tailed, finite networks.

These are proposed contributions to document and validate, not facts the model should assume. Record their derivations, null models, assumptions, comparison methods, and validation results separately.

## Data candidates

- O*NET 30.2: occupational skills and work activities.
- BLS OEWS: employment counts and wages.
- BLS QCEW: employment dynamics, subject to time and geography alignment.
- JobHop: observed career transitions, subject to access and coverage checks.
- Eloundou supplementary data: potential LLM task exposure.
- OLI Figshare data: online labour-demand trends; verify coverage and endpoint.

Every dataset needs a source, version/date, occupation-code mapping, missing-data policy, and documented role.

## Immediate questions

1. What exactly is the toy model meant to demonstrate?
2. What aspect of Maria and Penny's work do you most want to extend?
3. What would make the model useful to an AI-safety researcher rather than merely interesting?
4. What is the first phenomenon or mechanism you want to make visible?
5. What should be the model's basic unit: worker, occupation, task, skill, or something else?
6. What evidence would make you abandon the BERTopic/UMAP/HDBSCAN direction?
7. What would calibration mean for this toy model?
8. What would count as a successful first paper or EA Forum article?
9. Please add the MATS feedback email and any relevant Maria/Penny papers before we commit to a research question.

## Researcher homework

Read the core papers and make brief notes under four headings:

1. Data and unit of analysis.
2. Transition or network construction.
3. Model assumptions and calibration.
4. What the authors claim versus leave open.

Start with:

- del Rio-Chanona et al. (2021): what is directed, empirical, and modelled?
- Moro et al. (2021): how are connectivity, matching, shocks, and resilience
  operationalised?
- The papers most connected to Penny Mealy's work: what data, transitions, and
  mechanisms do they use?
- RAND's Decision Making Under Deep Uncertainty framework: what could
  “robust policy” mean here without assuming known probabilities over futures?

Do not try to settle the research question while reading. Identify candidate
mechanisms and empirical objects for the first data audit.
