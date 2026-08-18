# TITAN

## Vision

TITAN is a research project to build an AI system specialized in software engineering.

TITAN is **not** intended to be a wrapper around Claude, GPT, Gemini, or another external model. External models may be used during research, tooling, evaluation, or development when useful, but they are not TITAN.

### Final Goal

Build a system that can:

- Understand software requirements and large codebases.
- Plan software changes.
- Write and modify code.
- Navigate multi-file projects.
- Run compilers, tests, and development tools in a sandbox.
- Diagnose failures from real execution results.
- Repair its own implementations.
- Remember useful project and engineering experience.
- Improve through measured training and evaluation cycles.

The long-term target is an autonomous software-engineering system rather than a simple code generator.

## Current Phase

**Phase 0 — Project specification and knowledge base**

The next major engineering phase is the design and construction of TITAN's training dataset.

## Core Principles

1. TITAN must be its own model/system.
2. External APIs must not define TITAN's intelligence.
3. Real execution and testing should be preferred over unsupported claims of correctness.
4. Self-improvement must be measured and reversible.
5. New model versions must prove improvement on fixed evaluation suites before adoption.
6. Training data must be legally usable and quality-controlled.
7. Project knowledge must live in the repository so another AI can continue the work without requiring a verbal handoff.

## Read First

1. `README.md`
2. `PROJECT_STATE.md`
3. `docs/VISION.md`
4. `docs/MODEL_SPEC.md`
5. `docs/ARCHITECTURE.md`
6. `docs/ROADMAP.md`

## Current Model Direction

Initial research direction:

- Decoder-only Transformer.
- Architecture designed to support future MoE scaling.
- Prototype target: approximately 1B parameters.
- First serious model target: approximately 7B parameters.
- Future scaling may explore 30B, 70B, 100B+ parameter systems if justified by experiments.
- Initial context target: 32K tokens, with a path toward 128K and beyond.
- Code-aware tokenizer.
- Training progression: general language → code → debugging → software engineering → agent/tool use → verified improvement.

These numbers are research targets, not immutable commitments.
