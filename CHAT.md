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

## Update (2026-11-23, universal audio interface)

- Decision: Mini V0.1 should not include an onboard speaker amplifier.
- Documented unpopulated **2x6 2.54mm through-hole audio expansion**:
  ground, USB 5V, 3V3, PWM/PDM_RAW (GP5), filtered AC-coupled mono AUDIO_OUT,
  AMP_EN (GP6), I2S BCLK/LRCLK/DOUT (GP10–GP12).
- Added `mini/hardware/audio_interface.md` including pinout, safe connection,
  provisional filter values, assembly options, power-budget caveats.
- Updated Mini architecture, BOM, pin plan, KiCad conventions, firmware plan
  and root/agent memory to reflect use of *external* amplifier/DAC modules.
- Did not produce a validated KiCad electrical schematic or PCB. Next action:
  capture proper schematic in KiCad and verify ERC/DRC.

## Update (2026-11-23): KiCad schematic draft

- New native KiCad 9 schematic committed under mini/hardware/kicad.
- MCU core/USB based on credited MIT RP2354A development board reference.
- Added genuine sensor symbols, electrode symbols, I2C and pullup network,
  pressure supply, RC audio filter, 2x6 external audio header.
- Added touch footprint and reference source license.
- Lexical s-expression and unique UUID checks only.
- Next: open KiCad, inspect every net/pin, correct any ERC failures,
  fix pressure sensor footprint, adjust full BOM then PCB layout.

## Post-commit BOM audit (2026-11-23)

- Generated current Mini BOM directly from KiCad component references.
- Connectivity label-to-wire audit passed for sensor/I2C/audio labels.
- Highlighted blocking incomplete/incorrect footprints: J1, USBDEV1,
  L1 polarised Abracon inductor, U3 LPS28DFW. KiCad ERC still NOT RUN.
