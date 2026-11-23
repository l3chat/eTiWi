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

## 2026-11-23: final schematic PDF layout cleanups

- Root: moved and shrunk three hierarchical sheet rectangles to remove collision with A4 title block.
- Sensors: shifted connected U3 LPS28DFW and C103 decoupling group up by 25.4mm to clear title block, preserving net positions together.
- Audio: J5 through-hole-only optional connector removed from BOM and its KiCad DNP red X removed; no factory-fitted header expected.
- Re-run native KiCad PDF/ERC before declaring final.

## 2026-11-23: KiCad V0.2 ERC and PDF verified

- Final after layout polish: GitHub Actions successful https://github.com/l3chat/eTiWi/actions/runs/45141843146.
- KiCad 9.0.9 ERC 0 errors, 0 warnings. Four-page native A4 PDF reviewed and borders/titles clear.
- Independently compared all 77 net groups and 255 ref/pin memberships to original monolithic netlist; equal.
- Refreshed design status and README files to remove stale 'no schematic/no ERC' claims.
- Next hardware stage: validate provisional U3 CCLGA footprint and manufacturer parts, then PCB layout and DRC. No PCB preview exists yet.

## 2026-11-23: enlarged schematic symbols and circuit spacing

- On 01_controller_usb_power, scaled schematic-only pins/symbol geometry and absolute connection coordinates by exactly 2; changed paper A4 -> A2.
- Added `_Diagram2x` variants under sym_local (no physical changes to footprints). ERC/PDF inspection required before signoff.

## 2026-11-23: production footprint and PDF readability review

- Inspected four-page native KiCad PDF: C38/C39 overlapping value text,
  crowded GPIO labels near U1/J3/J4, electrode labels inside tiny boxes,
  AUDIO_PWM_RAW too close to R110.
- Found and corrected U3 LPS28DFW draft footprint rotation and land sizes
  using official ST DS13317 Figure 19 and TN0018; stencil and top-view
  orientation still to verify for fabrication.
- Compared U2 MPR121 symbol against official 20-pad NXP pinout;
  other critical footprints summarized in FOOTPRINT_AUDIT.md.
- Applied annotation-only PDF readability changes and connected longer
  AUDIO_PWM_RAW label lead; awaiting GitHub Actions ERC/netlist/PDF review.

## 2026-11-23: footprint drawing audit

- Compared MCU QFN60, NXP QFN-COL20, ST LPS28DFW CCLGA-7, Abracon polarized inductor, KMR2, crystal, USB-C and header footprint definitions against available manufacturer drawings.
- Fixed U3 top/bottom land length (0.55 to 1.00 mm), standard ST mask margin 0.05 mm, and central lid pad; retained clearly marked DRAFT status for factory validation.
- Aligned BOM U3 footprint/MPN/notes; added FOOTPRINT_AUDIT.md with risk table, ST dimensions and manufacturing blockers. No PCB yet.

## 2026-11-23: schematic text cleanup, A2 revision

- Reconciled with latest A2 controller source: corrected C39 field positions
  to scaled coordinates, made small text more legible.
- Hidden 8 extra FINGER value fields from touch-pad symbols; TP references remain.
- No intended wiring change. New GitHub Actions export/ERC to verify.

## 2026-11-23: resolve KiCad embedded symbol mismatch warnings

- Preview visually clearer, but ERC reported 60 library definition mismatches after changing font sizes globally.
- Restored embedded library block from previous known clean A2 schematic, retaining only human-visible instance annotation changes and corrected C39 coordinates.
- Await GitHub Actions ERC and PDF to verify warning count returns to zero.
