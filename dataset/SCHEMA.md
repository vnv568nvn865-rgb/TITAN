# TITAN Training Example Schema

Each training example represents a software-engineering task and, when applicable, the complete process used to solve it.

## Required Fields

### id
Unique identifier for the example.

### task
The original software-engineering task.

### context
Relevant project and environmental context.

### requirements
Explicit and implicit requirements that must be satisfied.

### analysis
Analysis of the problem and existing project state.

### plan
Ordered implementation plan.

### actions
Actions taken during implementation.

### result
The result of the actions.

### verification
Tests, execution results, or other evidence used to verify correctness.

### lessons
Important lessons extracted from the task.

## Optional Fields

### errors
Errors encountered during the process.

### diagnosis
Reasoning used to identify the cause of an error.

### repair
Changes made to correct the failure.

### tools
Tools used during the task.

### files_changed
Files created, modified, or deleted.

### difficulty
Estimated task difficulty.

### quality
Quality assessment of the final solution.

## Core Principle

Training examples should capture engineering behavior and problem-solving processes, not merely final answers or isolated code snippets.
