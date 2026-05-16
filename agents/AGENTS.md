# Hellbindah Agent Roster

## WIP policy

- TL-01 controls the board and assignment flow.
- Each worker agent can hold at most two `Doing` tasks unless TL-01 records an override.
- Every task must have: ID, status, assigned agent, area, sprint, start date, due date, dependency list, and SMART fields.
- Every PR must update `tasks/tasks.json` and `tasks/KANBAN.md` when task status changes.

## Agents

| Agent | Name | Mission |
|---|---|---|
| TL-01 | Team Lead Agent | Own task flow, dependency checks, WIP, blockers, handoffs, and merge readiness. |
| PM-01 | Task Curator Agent | Review, add, update, split, close, and delete tasks weekly. |
| RESEARCH-01 | Research Agent | Track current Windows game technology and design research. |
| ARCH-01 | Architecture Agent | Own engine ADRs, module boundaries, and interfaces. |
| RENDER-01 | Rendering Agent | Own D3D12 renderer, terrain, tunnels, frame timing, and visual readability. |
| STREAM-01 | Asset Streaming Agent | Own DirectStorage, packaging, compression, benchmarks, and fallbacks. |
| INPUT-01 | Input Agent | Own keyboard, mouse, controller, HOTAS, rebinding, and accessibility input. |
| FLIGHT-01 | Flight Feel Agent | Own arcade 6DOF movement, collision, assist, camera, and motion comfort. |
| WEAPON-01 | Weapons Agent | Own weapon data, projectiles, lock-on, damage tags, and hidden caches. |
| AI-01 | Enemy AI Agent | Own fighters, turrets, SAMs, bosses, and AI tests. |
| MISSION-01 | Mission Agent | Own objective graphs, triggers, switches, doors, checkpoints, and mission runtime. |
| UX-01 | UX/HUD Agent | Own HUD, compass, nav computer, map, subtitles, and settings. |
| AUDIO-01 | Audio Agent | Own callouts, weapon sounds, music states, subtitles, and mix. |
| BUILD-01 | Build/CI Agent | Own CMake, CI, packaging, crash logs, and compatibility. |
| QA-01 | QA/Evaluator Agent | Own tests, benchmarks, evaluator scoring, and playtest instrumentation. |
| ART-01 | Art Direction Agent | Own visual style, asset briefs, and readability rules. |

## Assignment lifecycle

1. TL-01 selects dependency-ready work from `Todo`.
2. TL-01 assigns it to a worker and changes status to `Doing`.
3. Worker opens a PR with implementation evidence.
4. QA-01/evaluators score the change.
5. TL-01 reviews merge readiness.
6. PM-01 updates, splits, closes, or deletes tasks during the weekly review.
