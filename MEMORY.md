# MEMORY

Stand: 2026-11-23

## Stable Project Intent

- eTiWi is a breath- and fingering-controlled electronic MIDI instrument.
- Original longer-term vision: onboard VS1053B synth, MIDI play-along,
  headphones/line-out/speaker and NiMH battery power.
- The original `hardware/` and `docs/` contain earlier design proposals;
  they should not be mistaken for finalized Mini circuit specifications.

## Active Prototype: eTiWi Mini V0.1

- Purpose: verify the playing interface and USB-MIDI before building the
  full autonomous instrument.
- RP2354A MCU with 2 MB in-package flash.
- 8 PCB copper capacitive electrodes via MPR121QR2 over I2C.
- LPS28DFWTR water-resistant digital pressure sensor on shared I2C.
- USB-C supplies 5 V and carries class-compliant USB-MIDI to host device.
- 3V3 supply for MCU/sensors; RP2354A own internal core regulator must be
  wired per official current Raspberry Pi reference (polarized inductor).
- External host synthesizer is the **first bring-up audio source**.
- Universal unpopulated 2x6 2.54mm through-hole audio pad field:
  GP5 raw PWM/PDM, GP5 two-stage RC+AC-coupled mono AUDIO_OUT,
  GP6 external AMP_EN, GP10-12 digital I2S, GND, 3V3, USB 5V.
- Tiny RC/filter passives should be factory-assembled by JLCPCB;
  manual soldering only for optional header/wires.
- **No speaker amp on the Mini PCB**; later attach a known analog-input
  amplifier or I2S DAC/amp module using a correctly wired cable.
  Review USB power budget before driving an 8-ohm speaker.
- No NiMH, VS1053B, OLED or battery charger in Mini V0.1.
- KiCad Mini V0.2 has a four-page editable schematic and clean ERC; no PCB or working firmware exists yet.
- Preliminary GPIO mapping and provisional JLCPCB catalog BOM in `mini/`.

## Remaining Design Decisions and Verification

- RP2354A specific clock/inductor/decoupling reference implementation.
- USB-C receptacle, ESD, complete passives, LDO and layout.
- Sensor port/mechanical moisture protection and pad geometry/latency.
- External audio module input pinout, header and RC filter validation,
  USB power budget; no onboard amplifier in Mini V0.1.
- Manufacturer footprints, assembly availability and electrical ERC/DRC.

## Codex Continuity

- Read `AGENTS.md`, `MEMORY.md` and `CHAT.md` at session start.
- **Refresh MEMORY.md and CHAT.md before every commit.**
- Do not copy WARBL GPL code or pretend a proposed KiCad file is validated.

## KiCad first draft (2026-11-23)

- Created `mini/hardware/kicad/eTiWi-mini.kicad_sch` as an editable
  KiCad 9 source based on jenschr/RP2354A (MIT), with original license.
- Added MPR121 with eight electrodes and recommended REXT/VREG components,
  LPS28DFW pressure interface and 2x6 audio/header/filter.
- Included custom solder-mask-covered electrode footprint.
- **KiCad ERC NOT RUN, U3 footprint not assigned, no PCB**.
  Manual electrical review and BOM recalc required before manufacturing.

- Post-schematic footprint audit (2026-11-23): J1 and USBDEV1 in
  base reference use unavailable private footprint library; L1 Abracon
  polarized inductor currently has resistor-0805 footprint (unsafe);
  U3 pressure sensor has no verified footprint. Block JLCPCB ordering
  until these are resolved.
- Rebuilt `mini/hardware/bom.csv` from actual schematic references
  (53 components incl J5 DNP) rather than earlier conceptual BOM.

- Added a provisional manufacturer-land-pattern footprint for L1 Abracon
  polarized 3.3uH inductor, with dot marking pin1; requires RP2350 SMPS
  layout orientation review (not yet ERC or PCB reviewed).

- Fixed a serious Mini schematic power connection naming mistake:
  sensor/pull-up labels +3V3 changed to reference rail +3.3V.
- Added USB-C local TYPE-C-31-M-14 footprint from jenschr/USB-C-Connectors
  (Unlicense), standardized C&K KMR2 button footprints, and tentative ST
  LPS28DFW CCLGA-7L pad geometry. Pressure footprint must be reviewed
  against ST TN0018 before manufacturing. Still no ERC/PCB.

- IMPORTANT CORRECTION: embedded `power:+3.3V` symbol has electrical
  pin name `+3V3`, so the correct Mini sensor labels are `+3V3`.
  A previous temporary relabeling to `+3.3V` was reverted after
  reading the actual embedded symbol pin; see DESIGN_STATUS.md.

- Configured GitHub Actions Mini KiCad PDF export + ERC report workflow
  on changes; when a PCB exists it will also attempt PCB PDF/DRC.
  Actual completed CI/ERC results remain unverified.
- Tablet preview currently uses a separate three-page functional vector
  PDF, not exact KiCad page export. No PCB preview until native PCB exists.

- CI fix 2026-11-23: GitHub Actions KiCad 9 container needs `options: --user 0` because the non-root default user cannot write GitHub runner's `/__w/_temp/_runner_file_commands/save_state_*` during `actions/checkout@v4` (EACCES). This is a checkout environment problem, not a KiCad/ERC error. Results from the retriggered run are not yet verified.

- Workflow debug 2026-11-23: added snapshot of KiCad source schematic to CI artifact and library-environment log to diagnose 96 endpoint_off_grid, 88 lib_symbol_issues, 11 footprint_link_issues; preparing readable multi-sheet source.

- Refactored monolithic KiCad Mini draft into 4-page A4 hierarchy: overview plus MCU/USB/power, sensors, audio sheets. Added project-local embedded symbol library tables and grid alignment; next confirm with KiCad 9 ERC and PDF. Source reference history preserved in git.

- Visual PDF QA 2026-11-23: shrunk/relocated root hierarchy boxes away from A4 title block, shifted pressure U3/C103 group and attached nets upward 25.4mm, changed J5 from DNP-red-X to BOM-excluded fitted electrical symbol (PCB through-hole pads still provided, no header factory installed). KiCad ERC recheck pending for this cleanup.

## Current verified KiCad status (supersedes historical draft notes)

- As of 2026-11-23: GitHub Actions run https://github.com/l3chat/eTiWi/actions/runs/45141843146 exported a 4-page A4 PDF from actual hierarchical KiCad 9.0.9 schematics; ERC report: **0 errors, 0 warnings**.
- Cross-checked 77 electrical net groups and 255 component pin connections against the original pre-refactor netlist; all memberships identical.
- Human-reviewed rendered four-page PDF, refined layout away from border/title; audio J5 BOM-excluded with no DNP marker.
- Still NOT manufacturing-ready: provisional U3 pressure footprint, USB-C and RP2354A polarized regulator layout/ESD/current review, supplier BOM, and actual routed PCB/DRC remain unfinished.

- 2026-11-23: schematic readability: controller/USB/power core transformed to A2, with 2x graphical distances between schematic symbols/pins/wires. Project-local `_Diagram2x` schematic symbol variants added; footprints physically unchanged. Verify ERC/netlist and PDF visually.

- 2026-11-23 footprint/PDF audit: ST LPS28DFW 7L library had physically wrong pad orientation (not visible to ERC); corrected 1 top, 4 bottom, side pads and central lid per ST DS13317/TN0018, still engineering review for assembly. MPR121 custom symbol pin numbering matches NXP. Added manufacturer footprint audit report. Improved cap C39, GPIO labels, TP1–TP8 annotation and analog audio filter layout in native KiCad sheets; ERC and PDF rerun required.

- 2026-11-23 footprint check: ST LPS28DFW CCLGA corrected top/bottom pad dimensions (0.55 -> 1.00 mm on pads 2/3/5/6) per ST DS13317 Fig19 and TN0018. Pad numbering follows PCB TOP-VIEW mirrored relative ST bottom-view; lid pad7 GND, solder. Still mechanical/assembly verification required. See FOOTPRINT_AUDIT.md.

- 2026-11-23 PDF cosmetic fix after concurrent A2 controller refactor: moved C39 ref/value fields to scaled sheet coordinates, increased controller text 1.27→1.50 mm and hid redundant FINGER# labels on electrodes. Electrical connections unchanged. Await KiCad PDF/ERC verification.

- 2026-11-23 ERC recovery: controller text enlargement changed embedded library symbols and caused 60 lib_symbol_mismatch warnings. Restored original embedded `lib_symbols` block from prior A2 commit while preserving instance field positions/font updates. ERC must be rechecked.

- Latest layout 2026-11-23: KiCad diagram-only 2x pin spacing on A2 controller made text legible, ERC 0 errors/warnings. 77 nets and 255 pin connections identical to prior pre-layout export. Final QSPI_SS label font reduced to prevent border contact; final workflow recheck pending. JLC candidates: HRO M14 C223907, Abracon inductor C42411119.

- Final schematic typography: added pin_names offset 5.08 mm on MCU _Diagram2x only; expected to move long labels (notably QSPI_SS) inside boundary, PCB footprints/nets unchanged. Pending KiCad export QA.

- Final 2026-11-23: verified GitHub Actions KiCad PDF ERC **0/0** at run
  45173445728, 77 named nets/255 exact member-pin pairs match V0.2
  baseline. Controller A2, 3 other A4 pages; visually reviewed.
  Added FOOTPRINT_AUDIT.md into future CI artifact for tablet viewing.
  U3 pressure footprint, L1 inductor orientation and USB-C land/cutout
  remain assembly verification gates; no PCB created.

- 2026-11-23 regulator audit: found AP2112K U4 VIN had zero local input bypass; C2 VOUT only 100nF. Changed C2 to 1uF X5R 10V 0603 and added C201 1uF VBUS/GND (JLC C26413). Future PCB must place both immediately by U4. Updated CI to ERC --exit-code-violations, pending actual post-commit validation.
