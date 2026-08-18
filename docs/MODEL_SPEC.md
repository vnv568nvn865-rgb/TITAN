# TITAN Model Specification

## Initial Direction

### Architecture

Decoder-only Transformer with an architecture that can later support Mixture-of-Experts scaling.

### Prototype Scale

Approximately 1B parameters for architecture and training experiments.

### First Serious Target

Approximately 7B parameters, subject to compute and data availability.

### Future Research

Potential scaling targets include 30B, 70B, and 100B+ parameters only if experiments justify the added cost.

### Context

Initial target: 32K tokens.

Next target: 128K tokens.

Longer contexts are a future research area.

### Tokenization

The tokenizer should be optimized for source code as well as natural language. It must handle identifiers, paths, punctuation, structured data, and common programming syntax efficiently.

## Training Progression

1. General language competence.
2. High-quality code and technical knowledge.
3. Debugging and repair.
4. Software engineering and architecture.
5. Tool use and agent trajectories.
6. Verified task completion.
7. Controlled self-improvement.

## Important

Parameter counts and context sizes are targets, not promises. They must be validated experimentally.
