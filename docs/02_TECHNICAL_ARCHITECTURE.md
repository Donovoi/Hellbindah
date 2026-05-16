# Technical Architecture

## Current decision state

The repository starts with a minimal C++23/CMake skeleton so that agents have a native baseline. The final engine choice remains open until `ARCH-001` completes.

## Candidate paths

1. Custom C++23 + Direct3D 12 + GameInput + XAudio2/FMOD/Wwise.
2. Unreal Engine with custom arcade flight/gameplay systems.
3. Unity with DOTS/jobs where useful.

## Initial module boundaries

- Core: time, config, logging, crash reports, save paths.
- Platform: Windows 11 APIs, input backends, file IO, packaging.
- Rendering: D3D12 or engine renderer abstraction.
- Streaming: package manifests, DirectStorage experiment, fallback IO.
- Gameplay: ship controller, weapons, damage, objectives, pickups.
- AI: fighters, turrets, SAMs, bosses.
- Mission: objective graph, triggers, switches, doors, checkpoints.
- UI: HUD, compass, map, nav computer, settings, subtitles.
- Audio: event routing, callouts, music states.
- QA: smoke tests, validators, evaluator scoring.

## Non-negotiables

- Native Windows 11 compatibility.
- No admin rights required after install.
- Data-driven tasks and mission definitions.
- CI/evaluator gate for agentic changes.
- Fallback paths for experimental Windows features.
