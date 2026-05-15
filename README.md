# Hellbindah

Hellbindah is a modern Windows 11-first arcade 3D flight-combat game: an ode to the 1990s Windows 95 sci-fi shooter era without copying protected names, assets, music, voice lines, mission text, logos, or proprietary content.

The target vertical slice is a 12-15 minute mission with arcade 6DOF flight, surface combat, tunnel infiltration, switch/door objectives, reactor destruction, hidden caches, timed escape, and jump-point extraction.

## Current repository contents

- `tasks/tasks.json` — machine-readable SMART task board.
- `tasks/KANBAN.md` — human-readable Kanban board with Todo, Doing, Done.
- `agents/` — team lead and worker-agent operating model.
- `docs/` — design, technical, Windows 11, research, and IP guardrail notes.
- `evolution/` — evaluator scaffold for self-improving agent workflows.
- `src/` — minimal C++23/CMake application skeleton.
- `.github/workflows/ci.yml` — Windows CI skeleton.

## Development model

The team lead agent owns task flow, dependency checks, WIP limits, and merge-readiness. Worker agents take SMART tasks from Todo to Doing to Done. QA/evaluator agents score candidate changes. PM-01 reviews the board weekly and can add, update, split, close, or delete tasks with rationale.

The methodology is inspired by evaluator-driven evolutionary coding systems: agents propose scoped changes, automated evaluators score them, regressions are rejected, good changes are retained, and the task board evolves based on evidence.

## Local build

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

## Windows 11 target

Hellbindah targets native 64-bit Windows 11. The research watchlist tracks Direct3D 12, DirectStorage 1.4, GameInput, PIX, modern packaging, CI, and asset streaming.

## IP guardrail

This project is an homage. Do not use original Hellbender/Microsoft/Terminal Reality assets, story text, voice lines, music, logos, executable content, or proprietary names without documented rights clearance.
