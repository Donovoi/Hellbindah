# Windows 11 Compatibility Plan

## Target

- Native 64-bit Windows 11 executable.
- Windows 10 x64 optional if it does not compromise Windows 11-first design.
- No reliance on Windows 95-era DirectDraw, DirectPlay, 16-bit installers, registry-only config, or CD-audio assumptions.

## Baseline requirements

- C++23 compiler on CI and dev machines.
- CMake 3.26+.
- Borderless fullscreen and windowed modes.
- User-writable save/config/log locations.
- Crash/log files without admin rights.
- Controller and keyboard/mouse support from first playable milestone.

## Experimental feature policy

Features such as DirectStorage 1.4 must have a fallback path and must not block the first vertical slice. STREAM-01 owns measurement and fallback design.

## Packaging policy

The first dev builds can be zip packages. Later builds should consider MSIX, Steam, or a conventional installer after the executable, config, logs, and asset paths stabilise.
