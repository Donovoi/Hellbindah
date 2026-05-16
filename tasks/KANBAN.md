# Hellbindah Kanban Board

Source of truth: `tasks/tasks.json`. Regenerate with `python scripts/render_kanban.py`.

## Board policy

- `Todo`: approved but not actively being worked.
- `Doing`: active work; max two active tasks per agent unless TL-01 overrides with a note.
- `Done`: acceptance criteria met and reviewed.
- PM-01 runs a weekly task review that can add, update, split, close, or delete tasks with rationale.
- TL-01 is the team leader agent and owns assignment, blockers, dependencies, and merge readiness.

## Doing

| ID | Task | Assigned | Sprint | Due | SMART measurement | Dependencies |
|---|---|---|---|---|---|---|
| TL-001 | Stand up the agent operating model | TL-01 | Sprint 0 | 2026-05-18 | agents/AGENTS.md and agents/TEAM_LEAD_AGENT.md exist and are linked from README; WIP limit is documented. | None |
| PM-001 | Create recurring task review process | PM-01 | Sprint 0 | 2026-05-18 | PM-002 exists as a recurring task and tasks/KANBAN.md documents task-change rules. | TL-001 |

## Todo

| ID | Task | Assigned | Sprint | Due | SMART measurement | Dependencies |
|---|---|---|---|---|---|---|
| IP-001 | Define homage and IP guardrails | TL-01 | Sprint 0 | 2026-05-19 | docs/IP_AND_BRAND_GUARDRAILS.md lists prohibited reuse, allowed homage patterns, review checklist, and naming policy. | None |
| ARCH-001 | Write engine architecture ADR | ARCH-01 | Sprint 0 | 2026-05-22 | ADR scores at least 3 options against DirectStorage, renderer control, speed, tooling, staffing, and Windows 11 compatibility, then selects one. | RESEARCH-001 |
| DESIGN-001 | Convert concept into vertical-slice GDD | MISSION-01 | Sprint 0 | 2026-05-23 | docs/01_GAME_DESIGN_BRIEF.md includes a mission beat table with at least 12 beats and 10 acceptance criteria. | IP-001 |
| BUILD-002 | Set up GitHub Actions CI for Windows builds | BUILD-01 | Sprint 1 | 2026-05-27 | A PR shows passing CI on windows-latest and ubuntu-latest. | BUILD-001 |
| INPUT-001 | Prototype input abstraction | INPUT-01 | Sprint 1 | 2026-05-30 | Sample logs thrust, pitch, yaw, roll, fire, turbo, weapon-next, map, and pause actions from at least two input families. | ARCH-001 |
| FLIGHT-001 | Implement arcade 6DOF flight prototype | FLIGHT-01 | Sprint 1 | 2026-06-05 | Manual test scene can fly through 10 gates in under 90 seconds with keyboard and controller; movement tests pass. | INPUT-001 |
| RENDER-001 | Create D3D12 renderer spike | RENDER-01 | Sprint 1 | 2026-06-07 | Spike hits 1080p/60 on a Windows 11 dev machine or produces an ADR rejecting D3D12 for v0.1. | ARCH-001, BUILD-002 |
| STREAM-001 | Benchmark DirectStorage 1.4 feasibility | STREAM-01 | Sprint 1 | 2026-06-07 | Report includes load times, CPU cost, GPU decompression viability, Zstd/GDeflate notes, packaging constraints, and recommendation for v0.1/v1.0. | RESEARCH-001, ARCH-001 |
| WEAPON-001 | Define weapon data schema | WEAPON-01 | Sprint 1 | 2026-05-31 | Schema validates 10 weapon definitions and rejects malformed configs with useful errors. | DESIGN-001 |
| MISSION-001 | Define mission objective graph schema | MISSION-01 | Sprint 1 | 2026-06-01 | A vertical-slice mission file validates and renders as a dependency graph with at least 12 nodes. | DESIGN-001 |
| UX-001 | Prototype compass and objective HUD | UX-01 | Sprint 2 | 2026-06-12 | In a test mission, 90% of testers reach the next objective within 60 seconds without external instructions. | MISSION-001, FLIGHT-001 |
| AI-001 | Prototype fighter, turret, and SAM AI | AI-01 | Sprint 2 | 2026-06-14 | Fighter reaches engagement range within 10 seconds, fires, can be destroyed, and SAM lock warning appears. | FLIGHT-001, WEAPON-001, UX-001 |
| MISSION-002 | Build vertical-slice mission blockout | MISSION-01 | Sprint 3 | 2026-07-05 | A tester can complete the full mission loop from start to extraction with placeholder art and logged metrics. | MISSION-001, AI-001, UX-001, RENDER-001 |
| QA-001 | Create evaluator scorecard for agentic development | QA-01 | Sprint 1 | 2026-06-02 | evolution/evaluator.py returns 0-100, hard-fails unsafe changes, and has at least 5 sample inputs with expected scores. | PM-001 |
| EVO-001 | Enable self-improving scoped-code loop | QA-01 | Sprint 4 | 2026-07-17 | Demo generates at least 5 candidate changes, accepts improvements, rejects regressions, and records score history. | QA-001, MISSION-002 |
| PM-002 | Review, add, update, split, close, and delete tasks | PM-01 | Recurring weekly | 2026-05-22 | Each review considers at least one add, update, split, close, and delete action and logs rationale. | PM-001 |
| TL-002 | Assign next sprint tasks based on dependencies and capacity | TL-01 | Recurring weekly | 2026-05-22 | Weekly assignment note lists each agent, active tasks, blockers, and next handoff; no Doing task lacks owner or due date. | TL-001, PM-002 |

## Done

| ID | Task | Assigned | Sprint | Due | SMART measurement | Dependencies |
|---|---|---|---|---|---|---|
| RESEARCH-001 | Create Windows 11 game-tech research watchlist | RESEARCH-01 | Sprint 0 | 2026-05-16 | docs/00_RESEARCH_NOTES.md contains actionable research items and source links. | None |
| BUILD-001 | Create minimal CMake Windows application skeleton | BUILD-01 | Sprint 0 | 2026-05-16 | cmake configure, build, and ctest run against hellbindah_boot. | None |
