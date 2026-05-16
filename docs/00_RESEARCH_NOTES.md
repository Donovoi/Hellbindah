# Research Notes

Updated: 2026-05-16 Australia/Sydney

## Windows 11 game technology watchlist

### DirectStorage 1.4 and asset streaming

Track DirectStorage 1.4 preview, Zstandard support, GDeflate, GPU decompression, and the Game Asset Conditioning Library. Hellbindah should not assume DirectStorage is required for v0.1; STREAM-001 must benchmark it against fallback file IO and make a recommendation.

Engineering task: `STREAM-001`.

### Direct3D 12 renderer

A custom engine path should validate Direct3D 12 early with a small renderer spike before committing to a full renderer. If D3D12 is too slow for the team, ARCH-001 must recommend Unreal or Unity instead.

Engineering task: `RENDER-001` and `ARCH-001`.

### GameInput / controller / HOTAS

Hellbindah needs keyboard/mouse, controller, and likely flight stick/HOTAS input. Research indicates GameInput can represent controllers, flight sticks, racing wheels, keyboard, mouse, and raw devices. INPUT-001 must still include a fallback abstraction so the game is not locked to one input backend.

Engineering task: `INPUT-001`.

### PIX

PIX is the preferred Microsoft tool for DirectX 12 GPU captures, timing captures, memory analysis, and file IO captures. RENDER-001 and STREAM-001 should produce PIX captures or explain why that was not possible.

Engineering task: `RENDER-001`, `STREAM-001`, `PERF` follow-up.

## Agentic / evolutionary development research

Hellbindah should not let agents rewrite arbitrary production code unsafely. The self-improving loop should be limited to scoped tasks and evaluator-safe files until the evaluator is mature.

Initial loop:

1. Candidate change proposed by worker agent.
2. Static checks and CI run.
3. Evaluator scores build, tests, performance, task hygiene, IP safety, and regression risk.
4. TL-01 accepts/rejects based on evidence.
5. PM-01 updates the task board based on results.

Engineering task: `QA-001`, then `EVO-001`.

## Sources to monitor

- Microsoft DirectStorage and DirectX developer blog.
- Microsoft Game Development Kit GameInput docs.
- PIX on Windows documentation.
- OpenEvolve repository and related evaluator-driven coding papers.
- Unreal/Unity release notes if ARCH-001 considers engine alternatives.
