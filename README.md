# Prooflight

> An open-source evaluation runtime for autonomous language agents.

Prooflight is a modular infrastructure platform for evaluating autonomous language agents through reproducible experiments.

The goal is to make safety evaluation behave more like production engineering infrastructure rather than isolated research scripts.

Prooflight provides the foundations for:

- reproducible agent evaluations
- safety and capability measurement
- mitigation analysis
- regression detection
- experiment tracking
- research-grade reporting

The project is designed around modularity, observability, extensibility, and scientific reproducibility.

---

# Why Prooflight?

Autonomous language agents are becoming increasingly capable, but evaluating their behavior remains challenging.

Many existing evaluations are:

- one-off scripts
- difficult to reproduce
- tightly coupled to specific models
- missing detailed execution traces
- unable to measure mitigation effectiveness

For example:

A researcher evaluates an agent against prompt injection attacks.

A traditional workflow might look like:

```
run script
collect output
manually inspect results
write conclusions
```

This creates problems:

- Was the same configuration used?
- Did the model change?
- Did the mitigation help?
- Can another researcher reproduce the result?

Prooflight treats evaluation as infrastructure:

```
Experiment
    |
    ├── Agent
    |
    ├── Runtime
    |
    ├── Evaluation Tasks
    |
    ├── Mitigations
    |
    └── Telemetry
            |
            ▼
        Reproducible Results
```

---

# Current Status

Prooflight is currently in **Milestone 2: Execution Core**.

Implemented:

- modern Python package structure
- reproducible dependency management using `uv`
- strongly typed experiment definitions
- immutable experiment configuration
- validation using Pydantic
- automated testing
- static type checking
- linting and formatting
- CI-ready development workflow
- runtime abstraction
- execution context
- execution orchestration
- immutable execution events
- execution recorder
- lifecycle event tracking
- structured execution results

The current implementation establishes the core abstraction that future evaluation components will build upon:

**Experiment.**

---

# Core Concept: Experiments

Everything in Prooflight revolves around experiments.

An experiment represents a complete evaluation configuration.

Example:

```python
Experiment(
    name="baseline-agent-evaluation",
    runtime="transformers",
    agent="react",
    tasks=(
        "prompt_injection",
        "tool_misuse",
    ),
    mitigations=(
        "sandbox",
    ),
    seed=42,
    output_dir="./artifacts"
)
```

An experiment is:

- immutable
- validated
- reproducible
- serializable
- uniquely identifiable

This ensures that evaluation results always correspond to a specific configuration.

---

# Architecture Principles

## 1. Experiment-first design

Experiments are the primary abstraction.

Everything else exists to execute and analyze an experiment.

```
Experiment
      |
      ├── Runtime
      ├── Agent
      ├── Environment
      ├── Evaluation Tasks
      ├── Mitigations
      └── Telemetry
```

---

## 2. Modular architecture

Components should be replaceable.

Future implementations will support interchangeable:

- model runtimes
- agent frameworks
- tools
- environments
- mitigation strategies
- evaluation tasks

Prooflight should adapt to new research directions without requiring architectural rewrites.

---

## 3. Reproducibility by default

Every evaluation should answer:

- What model was tested?
- What configuration was used?
- What random seed was used?
- What mitigations were enabled?
- What happened during execution?

Reproducibility is treated as a first-class engineering requirement.

---

## 4. Observability

Prooflight treats execution history as a first-class artifact.

Current capabilities include:

- execution lifecycle events
- ordered event recording
- execution failure tracking
- structured execution outcomes

Future versions will extend this into:

- agent trajectories
- tool interactions
- resource consumption
- evaluation metrics
- replay systems

The goal is that every evaluation result can be reconstructed.

---

# Repository Structure

Current structure:

```
prooflight/

├── src/
│   └── prooflight/
│       ├── __init__.py
│       │
│       ├── domain/
│       │   ├── __init__.py
│       │   └── experiment.py
│       │
│       ├── events/
│       │   ├── __init__.py
│       │   └── event.py
│       │
│       ├── recorder/
│       │   ├── __init__.py
│       │   └── recorder.py
│       │
│       ├── execution/
│       │   ├── __init__.py
│       │   ├── context.py
│       │   ├── executor.py
│       │   └── result.py
│       │
│       └── runtime/
│           ├── __init__.py
│           └── runtime.py
│
├── tests/
│   ├── domain/
│   │   └── test_experiment.py
│   │
│   ├── events/
│   │   └── test_event.py
│   │
│   ├── recorder/
│   │   └── test_recorder.py
│   │
│   └── execution/
│       ├── test_context.py
│       ├── test_executor.py
│       └── test_result.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pyproject.toml
├── uv.lock
├── README.md
├── .gitignore
└── .pre-commit-config.yaml
```

---

# Development Setup

## Requirements

- Python >= 3.11
- uv

Install dependencies:

```bash
uv sync --extra dev
```

---

# Quality Checks

Run formatting:

```bash
uv run ruff format src tests
```

Run linting:

```bash
uv run ruff check src tests
```

Run type checking:

```bash
uv run mypy src tests
```

Run tests:

```bash
uv run pytest
```

Run all pre-commit checks:

```bash
pre-commit run --all-files
```

---

# Testing Philosophy

Prooflight follows the principle:

> Infrastructure should fail early and clearly.

Current tests verify:

- valid experiment creation
- invalid configuration rejection
- seed validation
- path normalization
- experiment immutability
- event validation
- recorder behaviour
- execution lifecycle
- execution result handling

Future tests will cover:

- benchmark execution
- telemetry
- replay
- mitigation effectiveness

---

# Roadmap

## Milestone 1: Foundation Layer ✅

Completed:

- project structure
- experiment domain model
- validation
- testing infrastructure
- development workflow

---

## Milestone 2: Execution Core ✅

Completed:

- runtime abstraction
- execution context
- executor orchestration
- immutable event model
- execution recorder
- lifecycle event tracking
- execution result model

### Execution Architecture

Milestone 2 establishes the execution foundation:

```text
Experiment
    |
    ▼
ExecutionContext
    |
    ▼
Executor
    |
    +----------------+
    |                |
    ▼                ▼
 Runtime          Recorder
                       |
                       ▼
                    Events

Executor returns:

ExecutionResult
```

The separation allows Prooflight to distinguish between:

**Execution history**

"What happened?"

Captured through events.

and:

**Execution outcome**

"What was the final result?"

Captured through `ExecutionResult`.

---

## Milestone 3: Evaluation Infrastructure

Planned:

- evaluation task registry
- benchmark adapters
- metric system
- experiment runner
- artifact storage
- reporting

---

## Milestone 4: Research Infrastructure

Planned:

- replayable trajectories
- statistical analysis
- confidence intervals
- ablation studies
- robustness testing
- continuous evaluation pipelines

---

# Contributing

Prooflight is currently an early-stage research infrastructure project.

Contributions should prioritize:

- clear abstractions
- minimal complexity
- reproducibility
- maintainable design
- strong documentation

Before adding functionality, consider:

1. Does this belong in the core abstraction?
2. Can this be implemented as a replaceable module?
3. Can another researcher reproduce the result?

---

# Design Philosophy

Prooflight follows a simple principle:

> Build evaluation infrastructure that researchers can trust.

A useful evaluation system is not only about producing a score.

It should explain:

- what was tested
- how it was tested
- what happened
- why the result should be trusted

---

# License

MIT License
