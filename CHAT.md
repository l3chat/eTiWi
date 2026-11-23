# CHAT

## Current Status (2026-11-23)

- Active work: **eTiWi Mini V0.1** architecture/docs repository scaffold.
- Repository still has **no firmware, actual KiCad schematic or fabricated
  PCB**. Original full-instrument planning notes remain in `hardware/` and
  `docs/`.
- Old status/log through 2026-03-03 is superseded for active scope by
  the Mini decision; earlier details remain accessible in git history.

## Change Set: 2026-11-23

- Created `mini/README.md`.
- Created `mini/docs/architecture.md` and `mini/docs/bringup.md`.
- Created `mini/hardware/README.md`, `mini/hardware/pin_plan.md`,
  `mini/hardware/bom.csv`, `mini/hardware/kicad/README.md`.
- Created `mini/firmware/README.md` (plan only, no firmware code).
- Added `mini/` pointer to root README and updated root `AGENTS.md`.
- Refreshed `MEMORY.md` and `CHAT.md` before committing.

## Next Actions

1. Review latest official RP2350 reference schematic/BOM for RP2354A
   crystal, integrated core regulator and polarized inductor.
2. Lock complete USB-C/3V3 component selection, USB current budget, and
   sensor pin mapping/land patterns; refresh JLCPCB stock/part numbers.
3. Create **actual** KiCad project and electrical schematic.
4. Run ERC, then create PCB/pad geometry, DRC, export Gerbers/BOM/CPL.
5. Begin a small Pico SDK/TinyUSB USB-MIDI firmware after explicit request;
   measure sensing and MIDI latency before adding optional audio.

## Session Rule

Keep `MEMORY.md` and `CHAT.md` consistent with the files being committed.
