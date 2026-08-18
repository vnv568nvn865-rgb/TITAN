# TITAN Self-Improvement

## Goal

Enable TITAN to improve using verified experience and controlled retraining.

## Loop

1. Run TITAN on tasks.
2. Collect tool observations and outcomes.
3. Identify successful and failed trajectories.
4. Analyze failure causes.
5. Select high-quality examples.
6. Construct training/evaluation data.
7. Train a candidate model.
8. Run fixed benchmarks.
9. Compare with the previous model.
10. Adopt only if the candidate meets predefined criteria.

## Anti-Regression Principle

A candidate model must not be accepted solely because it performs better on newly collected data.

Evaluation must include old and new benchmarks to detect regressions.

## No Blind Self-Modification

TITAN cannot declare itself improved. Improvement is determined by external evaluation criteria.
