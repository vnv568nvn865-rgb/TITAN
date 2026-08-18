# TITAN Dataset Design

This document defines the intended dataset before collection begins.

## Categories

### 1. Programming Knowledge

Languages, algorithms, data structures, operating systems, networking, databases, tooling, build systems, and software architecture.

### 2. Complete Projects

Legally usable repositories and project artifacts that provide multi-file context.

### 3. Debugging

Buggy code, error output, diagnosis, patch, and verification result.

### 4. Software Engineering

Requirements, architecture decisions, implementation, testing, refactoring, and maintenance.

### 5. Reasoning

Programming problems and tasks requiring analysis before implementation.

### 6. Agent Trajectories

Task → plan → tool actions → observations → corrections → verified result.

## Quality Pipeline

```text
Source
  |
  v
License / Usage Review
  |
  v
Parsing
  |
  v
Deduplication
  |
  v
Quality Filtering
  |
  v
Security Filtering
  |
  v
Language / Task Classification
  |
  v
Verification where possible
  |
  v
Dataset
```

## Core Rule

Data must not be collected simply because it is available. Each source needs an appropriate legal and technical basis for inclusion.
