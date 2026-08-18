# TITAN Dataset

This directory contains the training and evaluation data for TITAN.

The dataset is designed to train TITAN as a software-engineering system, not merely as a code completion model.

## Core Capabilities

The dataset should teach TITAN to:

1. Understand software requirements.
2. Analyze existing codebases.
3. Build implementation plans.
4. Write and modify code.
5. Use tools correctly.
6. Run tests and inspect execution results.
7. Diagnose errors.
8. Repair failed implementations.
9. Review its own work.
10. Learn from successful and failed engineering attempts.
11. Maintain useful project context.
12. Improve its problem-solving strategies through evaluation.

## Training Philosophy

TITAN should learn from complete engineering processes rather than isolated question-answer pairs.

A high-quality example should contain, when applicable:

- Context
- Goal
- Repository state
- Requirements
- Analysis
- Plan
- Actions
- Tool results
- Errors
- Diagnosis
- Repair
- Verification
- Final result
- Lessons learned

## Dataset Categories

The dataset will eventually contain examples for:

- Requirements analysis
- Code generation
- Code modification
- Debugging
- Refactoring
- Testing
- Tool use
- Repository navigation
- Architecture
- Planning
- Code review
- Failure analysis
- Self-correction
- Long-horizon software tasks

## Quality Principle

Correctness is more important than dataset size.

A smaller dataset containing high-quality engineering trajectories is preferable to a large dataset containing shallow or incorrect answers.
