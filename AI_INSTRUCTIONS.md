# Instructions for AI Contributors

You are contributing to the TITAN project.

## Required Reading

Read, in order:

1. `README.md`
2. `PROJECT_STATE.md`
3. `docs/VISION.md`
4. `docs/MODEL_SPEC.md`
5. `docs/ARCHITECTURE.md`
6. `docs/ROADMAP.md`

Then inspect the relevant files for the task.

## Project Identity

TITAN is intended to become its own AI software-engineering system. Do not redefine the project as merely a frontend for Claude, GPT, Gemini, or another external model.

External models may be used as temporary research assistants, data-generation aids, baselines, or evaluation references when explicitly appropriate. They are not the TITAN model.

## Change Discipline

Before proposing a major architectural change:

- Identify the existing decision.
- Explain why the current design is insufficient.
- Propose the alternative.
- Define how it will be evaluated.
- Preserve a record of important decisions in `docs/decisions/`.

Do not silently invalidate previous project decisions.

## Self-Improvement

TITAN must improve through measurable experiments.

A new version should be evaluated against fixed benchmarks. A candidate that regresses materially should not automatically replace the previous version.

## Coding Work

When implementing software:

- Prefer tests.
- Run code when possible.
- Record failures.
- Do not claim a fix is verified when it has not been tested.
- Keep interfaces documented.
- Avoid unnecessary dependencies.

## Handoff

At the end of a meaningful task, update `PROJECT_STATE.md` so another AI can continue without relying on conversation history.
