# Agentic Development Model

Hellbindah uses a task-board-first agent workflow inspired by evolutionary coding systems, but with strict safety and review gates.

## Core loop

1. TL-01 assigns a SMART task to one worker agent.
2. Worker creates a scoped candidate change.
3. CI validates build/test/task JSON.
4. QA-01 runs evaluator scoring.
5. TL-01 reviews evidence and merge readiness.
6. PM-01 updates, splits, closes, deletes, or adds tasks based on results.

## Evolution constraints

The self-improving loop is initially restricted to:

- tuning files;
- validation scripts;
- benchmark configs;
- mission/weapon JSON;
- small isolated prototypes.

It must not automatically rewrite broad engine code, security-sensitive scripts, or IP-sensitive content until the evaluator is mature.

## Evaluator dimensions

- Build result.
- Unit/smoke tests.
- Performance budget.
- Code readability.
- Task hygiene.
- IP safety.
- Regression risk.
- Reproducibility.

## Human/team-lead checkpoint

Automation can propose and score changes. TL-01 remains the merge gate. Unsafe or unclear improvements become new tasks rather than direct merges.
