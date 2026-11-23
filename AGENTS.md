# AGENTS

Stand: 2026-11-23

## Project Scope

This repository covers eTiWi, a breath-controlled MIDI instrument:
- Long-term: VS1053B-based General MIDI playback, play-along and battery power.
- **Immediate active prototype: [eTiWi Mini](mini/README.md)** — RP2354A,
  MPR121 (8 capacitive touch electrodes), LPS28DFW breath sensing,
  USB-C bus-powered USB-MIDI, with an optional universal audio header
  (filtered mono PWM/PDM analog or I2S to an external module).
- The older `hardware/` and `docs/` specifications describe the earlier
  full-instrument direction; **do not silently overwrite them** with Mini
  choices. Use the `mini/` subtree for Mini-specific changes.

## Working Rules

- Keep documentation technically accurate and concise. Explicitly label
  proposed GPIO maps, BOM candidates and unvalidated audio circuitry.
- Prefer official device datasheets and Raspberry Pi's latest RP2350
  hardware design/reference BOM for the RP2354A power and clock network.
- Do not copy WARBL code; use clean-room ideas only.
- Prefer small, reviewable commits.
- **Do not introduce firmware code or claim KiCad/ERC/DRC validation until
  explicitly requested and genuinely performed.**
- Do not drive an 8-ohm speaker from a GPIO. GP5 PWM/PDM is reserved
  for a raw test signal and an RC/AC-coupled analog output; 2x6 audio
  header also provides 3V3 I2S GP10..12, GP6 EN, USB 5V, 3V3, GND.
  External amp/DAC requires a wired adapter and USB current review.
- Keep Mini V0.1 on-board amplifier unpopulated: no small signal transistors
  or GPIO-powered speaker. Leave 2.54mm header pads easily hand-solderable.
- Treat JLCPCB availability, pricing, assembly class, symbol pin mapping,
  footprint and thermal/current constraints as unverified until checked.

## Source Documents

- Root overview: `README.md`
- Mini entry point: `mini/README.md`
- Mini architecture / tests: `mini/docs/`
- Mini BOM, audio connector and preliminary GPIO: `mini/hardware/`
- Legacy full hardware notes: `hardware/README.md`
- Legacy architecture/roadmap: `docs/architecture.md`, `docs/roadmap.md`

## Session Persistence Workflow

1. Read `AGENTS.md`, `MEMORY.md`, and `CHAT.md`.
2. Follow the active Mini scope or the explicitly requested legacy scope.
3. Execute next scoped task with minimal changes.
4. Update `MEMORY.md` with stable decisions, separating Mini vs full concept.
5. Update `CHAT.md` with actual changes and next actions.
6. **Before every git commit**, refresh `MEMORY.md` and `CHAT.md` to
   match the staged changes.
