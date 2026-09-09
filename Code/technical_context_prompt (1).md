# Technical Context — ABM Labour Displacement Project

> **Status: exploratory context, not a specification.**
> This is working memory for developing the project. Do not treat candidate
> methods, datasets, mechanisms, or claims as settled.

## Purpose

Develop a scientifically serious toy model that extends Maria del Rio-Chanona and Penny Mealy's work on occupational mobility and automation.

The eventual purpose is to support:

- a useful contribution to AI-safety policy discussion;
- a second EA Forum policy article;
- strong scientific reasoning suitable for thesis and research audiences;
- a response to MATS feedback about producing work that is actually useful.

The immediate goal is simply to build and understand the toy model well. Usefulness claims come later.

## Research posture

The project is open-ended and data-led. We should read the relevant papers, inspect transition data, visualise its structure, and let the empirical object shape the model.

There are currently no settled claims about:

- the correct dataset;
- the unit of analysis;
- the transition mechanism;
- the role of AI exposure;
- the need for clustering;
- the form of the ABM;
- the policy outcome;
- what “robust” should mean.

The ABM is important, but it is one part of a broader process of data analysis, network construction, model development, and policy reasoning.

## Working direction

A candidate direction is:

1. obtain transition-related occupational or skill data;
2. construct and inspect a directed transition network;
3. investigate whether a directed acyclic representation is justified;
4. use the network to inform a toy ABM;
5. simulate policies across uncertain parameters and possible futures.

The DAG is a working hypothesis, not a constraint. Real occupational mobility may contain cycles. Acyclicity requires a defensible interpretation such as time ordering, skill acquisition, causal ordering, or aggregation.

The first coding task should therefore reproduce or implement a paper's network method in small, verifiable stages.

## Policy motivation

The possible policy framing is Decision Making Under Deep Uncertainty:

- represent a complex system with explicit mechanisms;
- generate a distribution of possible futures through parameters and stochasticity;
- compare policies across futures;
- investigate policies that perform acceptably across uncertainty.

This is not yet a defined robustness criterion. Do not assume known probabilities over futures or claim that simulated policies are empirically effective.

## Candidate methods

Possible ingredients include:

- O*NET or another occupational/skill dataset;
- observed transition data;
- temporal skill or occupational analysis;
- topic modelling, possibly BERTopic;
- dimensionality reduction, possibly UMAP;
- clustering, possibly HDBSCAN;
- directed transition networks;
- an agent-based model;
- exploratory policy analysis.

Each method must answer a research need. Avoid adding methods because they are fashionable or produce attractive visualisations.

## Required distinctions

Keep these concepts separate:

- skills, tasks, occupations, and workers;
- potential AI exposure, adoption, substitution, job loss, and transition demand;
- similarity networks and observed mobility networks;
- empirical observations, model assumptions, and synthetic mechanisms;
- model calibration, parameter motivation, and sensitivity analysis;
- policy robustness and prediction.

A worker agent may have an occupation, skills or transition costs, employment status, security or income, and adaptation or search behaviour. Occupations are not workers; they may provide structure, demand, vacancies, or transition opportunities.

## Methodological cautions

- An O*NET similarity graph is not automatically a mobility network.
- Preferential attachment and homophily are hypotheses or synthetic mechanisms, not established properties of an O*NET graph.
- An undirected graph has degree or weighted strength, not in-degree.
- A threshold such as cosine similarity > 0.7 requires sensitivity analysis.
- A log-log plot does not establish a power law.
- Heavy tails should be inspected in the data, not presumed.
- A standard Barabási–Albert graph may be a poor null model for a structured occupational network.
- Network degree observations are dependent; Sid's proposed GOF method needs a precise null model, statistic, resampling scheme, and validation.
- A DAG may impose direction that the data does not support.
- Exposure scores should not be converted directly into displacement probabilities.
- A toy model can clarify mechanisms without validating real-world forecasts.

## Proposed methodological contribution

Sid proposes:

1. an analytical distribution for networks involving preferential attachment and homophily;
2. a goodness-of-fit test for dependent, heavy-tailed, finite networks.

Treat both as proposed contributions requiring derivation, comparison, and validation. Do not make them assumptions of the labour-market model without evidence.

## Core reading

Start with:

1. [del Rio-Chanona et al. (2021), Occupational mobility and automation](https://doi.org/10.1098/rsif.2020.0898)
   — identify its data, network, worker transitions, automation shock, and calibration.
2. [Moro et al. (2021), Universal resilience patterns in labor markets](https://doi.org/10.1038/s41467-021-22086-3)
   — identify how connectivity, matching, shocks, and resilience are operationalised.
3. The papers most directly connected to Penny Mealy
   — identify the data, transition concept, and mechanism being extended.
4. RAND's Decision Making Under Deep Uncertainty framework
   — clarify robust-policy reasoning without assuming known probabilities.

For each paper, record only:

- data and unit of analysis;
- network or transition construction;
- assumptions and calibration;
- claims versus open questions.

Other candidate references:

- [Eloundou et al. (2023), GPTs are GPTs](https://arxiv.org/abs/2303.10130) — potential LLM task exposure, not realised displacement;
- Barabási & Albert (1999) — preferential-attachment foundations;
- Alabdulkareem et al. (2018) — occupational skill structure;
- Epstein & Axtell (1996) — ABM foundations;
- Gupta & Kumar (2026), [Agentic Task Exposure preprint](https://arxiv.org/abs/2604.00186) — emerging, unvalidated candidate input.

Teutloff et al. (2025), del Rio-Chanona et al. (2026), and Pangallo et al. (2024) need exact citations and a defined role before use.

## Candidate data

- O*NET 30.2: occupational skills and work activities;
- BLS OEWS: employment counts and wages;
- BLS QCEW: employment dynamics;
- JobHop: observed career transitions;
- Eloundou supplementary data: potential LLM task exposure;
- OLI Figshare data: online labour-demand trends.

For every dataset, record source, version/date, unit, occupation-code mapping, missing-data policy, and role in the model.

## Immediate workflow

1. Read the relevant paper.
2. Extract its network definition and assumptions.
3. Agree on the smallest faithful implementation.
4. Build one component.
5. Verify it against the paper.
6. Refactor the codebase before adding the next component.
7. Keep a short record of decisions, failures, and open questions.
8. Plan the next session only after reviewing the day's work.

