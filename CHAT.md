# CHAT

## Current Status (2026-03-03)

- Repository documentation is in early design/planning stage.
- No firmware code has been introduced in this phase.

## Last Session Changes

- Reformatted root and hardware Markdown files for readability and consistency.
- Added `docs/README.md`, `docs/architecture.md`, and `docs/roadmap.md`.
- Expanded `hardware/todo.md` into concrete, measurable V1 checklist items.
- Verified required hardware documentation files are present.
- Verified Markdown files end with trailing newline.

## Session Persistence Setup

- Added `AGENTS.md` with project scope, rules, and persistence workflow.
- Added `MEMORY.md` with stable architectural/hardware decisions.
- Added `CHAT.md` for rolling session log and next-step continuity.

## Next Practical Steps

1. Resolve V1 open hardware choices listed in `hardware/todo.md`.
2. Convert selected choices into schematic-ready requirements (still docs-only).
3. Start KiCad capture only after open checklist items are sufficiently closed.

## Update (2026-03-03)

- Reflected new hardware direction/decisions in docs:
  - VS1053B clocking from MCU MCLK, no dedicated VS1053B quartz/crystal.
  - FRAM chosen instead of EEPROM for non-volatile settings/presets.
  - RP2350B + large external flash recorded as current evaluation direction.
  - V1 controls decided: power switch, rotary encoder with push, play/stop,
    back/function.
- Updated files: `hardware/interfaces.md`, `hardware/parts_candidates.md`,
  `docs/architecture.md`, `hardware/README.md`, `hardware/todo.md`,
  `MEMORY.md`, `CHAT.md`.

## Update (2026-03-03, Pre-Commit Rule)

- Added explicit rule in `AGENTS.md`: before every commit, refresh
  `MEMORY.md` and `CHAT.md` so they match staged changes.
