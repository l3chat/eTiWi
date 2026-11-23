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

- Added custom provisional L1 Abracon footprint from datasheet pad dimensions;
  corrected schematic, BOM, and schematic status accordingly.

## 2026-11-23: footprint / supply net corrections

- Corrected eight +3V3 net aliases to +3.3V so sensors receive power.
- Copied HRO TYPE-C-31-M-14 footprint from the original author's
  Unlicense repository with shield-pad renumbering for KiCad J1 symbol.
- Replaced inaccessible switch library references with standard KiCad KMR2.
- Added a clearly tentative U3 pressure footprint and synchronized BOM.
- STILL pending native KiCad ERC / board layout.

- Corrected supply net to +3V3 after directly inspecting KiCad
  embedded `power:+3.3V` symbol pin name; previous +3.3V relabel
  was incorrect and has been superseded.

## 2026-11-23: tablet preview / KiCad CI

- Configured workflow `.github/workflows/mini-kicad-preview.yml` using
  official KiCad 9 container; it attempts a native schematic PDF, netlist,
  ERC report and later conditional PCB PDF/DRC, uploading results as artifact.
- Created separate 3-page functional vector PDF for tablet in conversation.
- Corrected +3V3 net name based on actual power symbol net pin.
- No verified KiCad ERC pass and no PCB layout as of this entry.

## 2026-11-23: Fix GitHub Actions EACCES at checkout

- User supplied job log: `actions/checkout@v4` fails with `EACCES` writing `/__w/_temp/_runner_file_commands/save_state_*` inside `ghcr.io/kicad/kicad:9.0`.
- Updated workflow container options to `--user 0`; this is a standard workaround for GitHub Actions job containers with non-root default users.
- No verified outcome for the new workflow run; inspect the run artifacts, PDF export, and ERC report next.

## 2026-11-23: KiCad PDF/ERC diagnostics

- User reported native KiCad PDF is poorly laid out; confirmed schematic parts outside A3 and title block overlap.
- ERC findings: 96 endpoint_off_grid, 88 lib_symbol_issues, 11 footprint_link_issues (195 warnings, not 0 valid issues).
- Added native editable schematic snapshot to GitHub artifact and KiCad library environment logging for local analysis before substantive layout restructure.

## 2026-11-23: schematic refactoring for readable native PDF

- Original PDF showed components outside A3 and audio filter overlaying title block. Created KiCad V0.2 hierarchy with three A4 functional schematic sheets plus overview, moved all 88 original component instances and 255 wires, split into functional areas and snapped to 1.27mm grid.
- Added local symbol libraries derived from embedded symbol definitions, `sym-lib-table` and the source reference KiCad project settings.
- Requires new GitHub Actions KiCad ERC and PDF inspection. Do not call manufacturing ready before review.
