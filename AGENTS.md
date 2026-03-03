# AGENTS

Stand: 2026-03-03

## Project Scope

This repository covers the eTiWi electronic tin whistle:
- VS1053B-based General MIDI playback
- breath + fingering to real-time MIDI conversion
- play-along support with MIDI backing tracks

Current phase is architecture and documentation work for hardware/firmware
planning, not firmware implementation.

## Working Rules

- Keep documentation technically accurate and concise.
- Do not copy WARBL code; use clean-room ideas only.
- Prefer small, reviewable doc commits.
- Do not introduce firmware code unless explicitly requested.

## Source Documents

- Root overview: `README.md`
- Hardware index: `hardware/README.md`
- Hardware decisions/tasks: `hardware/todo.md`
- Architecture/roadmap: `docs/architecture.md`, `docs/roadmap.md`

## Session Persistence Workflow

1. Read `AGENTS.md`, `MEMORY.md`, and `CHAT.md`.
2. Execute the next scoped task with minimal, targeted changes.
3. Update `MEMORY.md` with stable decisions only.
4. Update `CHAT.md` with what changed this session and next actions.
5. Before every `git commit`, refresh `MEMORY.md` and `CHAT.md` so they match
   the staged changes.
