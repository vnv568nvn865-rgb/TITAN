# TITAN Project State

## Status

Phase 0 — Specification and repository knowledge base.

## Completed

- Core project vision defined.
- TITAN distinguished from external API wrappers.
- Initial model direction defined.
- Initial memory concept defined.
- Initial agent/execution concept defined.
- Self-improvement philosophy defined.
- Repository knowledge-base structure defined.

## Current Task

Design the training dataset and data-generation pipeline.

## Immediate Next Steps

1. Define dataset categories and schemas.
2. Define legal/licensing requirements for every data source.
3. Build cleaning, deduplication, filtering, and quality pipelines.
4. Define code execution and verification infrastructure.
5. Create initial benchmark suites.
6. Prepare a small experimental dataset.
7. Train and evaluate the first prototype.

## Important Constraints

- Do not replace TITAN with an external commercial model.
- Do not assume that a larger parameter count automatically means a better model.
- Do not train on data without establishing a permissible basis for use.
- Do not accept generated code as correct without appropriate verification when verification is possible.
- Do not allow self-modification to bypass evaluation.

## Handoff Rule

Any AI or developer joining the project should read this file and the files listed in `README.md` before making architectural changes.
