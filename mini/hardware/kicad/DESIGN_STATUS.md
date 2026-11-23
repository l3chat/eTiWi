# eTiWi Mini V0.2 — actual schematic verification status

**Status (2026-11-23): KIcad 9.0.9 ERC passed — 0 errors, 0 warnings.**
The workflow run was successful: https://github.com/l3chat/eTiWi/actions/runs/45141843146

## Verified now

- Four native schematic pages in an editable KiCad 9 project (A2 controller, three A4):
  `eTiWi-mini.kicad_sch` overview, `01_controller_usb_power.kicad_sch`,
  `02_touch_pressure.kicad_sch`, and `03_audio_expansion.kicad_sch`.
- KiCad schematic PDF and netlist exported successfully by GitHub Actions.
- KiCad `sch erc`: **0 errors, 0 warnings**, checked against
  the full four-page hierarchy (2026-11-23).
- Independently compared **all 77 net membership groups / 255 pin
  connections** against the original single-sheet circuit. They match
  exactly. Only hierarchical net names changed as expected.
- Source symbols are now resolved from project-local `sym_local/` libraries;
  `sym-lib-table` and `fp-lib-table` are included.
- All electronics kept away from A4 borders and title blocks in the
  actual KiCad PDF. Touch electrode symbols are spaced in two columns;
  audio expansion J5 is not populated (through-hole pad field only,
  BOM-excluded, not DNP-crossed).
- Base RP2354A core USB/clock and power circuit adapted from jenschr/RP2354A
  (MIT). USB footprint adapted from jenschr/USB-C-Connectors (Unlicense).
  Original attribution/license files remain in this directory.

## IMPORTANT: Not yet ready to manufacture

An ERC pass checks electrical design rules. It does **not** verify actual
schematic function, USB hardware behavior, real supplier components,
mechanical orientation, or PCB routing.

1. **U3 LPS28DFWTR footprint** `eTiWi:LPS28DFW_CCLGA-7L_2.8x2.8mm_DRAFT`
   is provisional: validate pad geometry, pad7-to-lid orientation and
   pressure port clearance against current ST datasheets/land pattern.
2. Verify the exact HRO USB-C Type-C-31-M-14 pinout, connector geometry,
   shielding, USB data ESD protection and VBUS/current budget.
3. Check **L1 polarized Abracon** inductor pad1 marking/orientation,
   switch-mode regulator current loops and decoupling placement against
   current Raspberry Pi RP2350 reference designs.
4. Recheck MPR121 package/REXT reference, touch electrode size,
   pressure sensor moisture protection, and external audio module input.
5. Select and verify all JLCPCB LCSC parts, manufacturing footprints,
   assembly capabilities, and quote. BOM is still a draft.
6. No `.kicad_pcb`, routed traces, DRC, manufacturing Gerbers or CPL yet.

## PDF, netlist and ERC (tablet workflow)

Open [GitHub Actions — eTiWi Mini KiCad PDF and ERC](https://github.com/l3chat/eTiWi/actions/workflows/mini-kicad-preview.yml).
Select a successful run, download **Artifacts → etiwi-mini-kicad-previews**.

The archive contains:
- `eTiWi-mini-schematic.pdf`: 4-page native KiCad PDF (A2 core, three A4 pages)
- `eTiWi-mini-erc.txt`: KiCad ERC result
- `erc-summary.txt`: ERC process exit code
- `eTiWi-mini.net`: KiCad electrical netlist
- `eTiWi-mini-source.kicad_sch`: root schematic only
- `pcb-status.txt`: status of PCB export availability

When an actual `eTiWi-mini.kicad_pcb` exists, the workflow will
also attempt PCB PDF and DRC exports.

**Next:** manufacturing-level footprint/parts verification, then KiCad
PCB layout and DRC. Do not submit schematic-only draft for PCB assembly.

## Readability revision (2026-11-23)

- Controller/USB/power page uses A2 and `_Diagram2x` schematic-only symbols with 2x electrical drawing coordinates to reduce overlapping text. Physical component footprints are **unchanged**. Pending KiCad ERC and visual PDF review.

## 2026-11-23: footprint audit and PDF readability pass

- Added [FOOTPRINT_AUDIT.md](FOOTPRINT_AUDIT.md) with manufacturer-specific
  package/land-pattern comparison and explicit manufacturing blockers.
- Discovered physical orientation error in previously draft U3 ST LPS28DFW
  footprint; corrected physical pad arrangement and land dimensions to match
  ST datasheet Figure 19 and TN0018. **PCB orientation/stencil still require
  review; KiCad ERC cannot catch a rotated pad pattern.**
- Repositioned controller C39 reference/value, reduced crowded GPIO label
  font while keeping electrical anchors, moved TP label fields outside tiny
  symbol outlines, separated audio R110/111 fields and extended the input
  PWM label wire for clearer PDF. Netlist/ERC recheck pending.

## Footprint comparison 2026-11-23

See [FOOTPRINT_AUDIT.md](FOOTPRINT_AUDIT.md). U3 LPS28DFW local footprint copper dimensions corrected to ST nominal drawing + TN0018 margin. Still *NOT manufacturing signed off*: requires verification of solder paste/stencil and assembly rotation, along with U1/QFN ground vias, U2 QFN-COL, USB-C exact MPN and L1 orientation.

## PDF layout polish (2026-11-23, controller A2)

- Preserved the newer **A2 controller sheet** with physically doubled
  symbol/pin spacing introduced in commit 1965a899; this is deliberate
  rather than collapsing the page back to crowded A4.
- Repositioned capacitor C39 label/value to match the **doubled
  coordinates** on this sheet. Enlarged visible controller text modestly
  (1.27mm to 1.50mm). This affects presentation only.
- Hidden redundant FINGER# values on TP1–TP8; the TP# references and
  ELE0–ELE7 net labels remain visible.
- New KiCad PDF/ERC visual review and netlist comparison required.

## ERC caution and resolution

- Post-layout KiCad run temporarily reported 60 `lib_symbol_mismatch` warnings
  due to automated resizing of embedded `lib_symbols` text. These warnings
  are unrelated to footprint copper and are not an approved final status.
- Reinstated the authoritative embedded symbol definitions from the previous
  A2 schematic, keeping only instance annotations. Recheck ERC before release.

## Final PDF geometry / netlist recheck, 2026-11-23

- Core A2 diagram uses schematic-only 2x-spaced pin graphics; all
  package footprints remain physically unchanged.
- The latest saved PDF before this small font refinement had **no measured
  text-to-text collisions** on core/sensor/audio pages aside from a
  negligible built-in KiCad title block `Rev:/Id:` extraction artifact.
  One long QSPI_SS pin-name glyph crossed a device outline by a few pixels;
  its font was reduced from 1.27mm to 0.85mm.
- KiCad ERC check after the 2x transformation: **0 errors and 0 warnings**.
- Compared GitHub Actions exported netlist against pre-refactor netlist:
  all **77 net name/member groups** and **255 pins** match.
- Run KiCad export/ERC again after QSPI glyph change. Font only; no
  electrical net or footprint changed by this last visual refinement.

## Final verification of the current PDF revision (2026-11-23)

- Latest checked GitHub Actions run:
  https://github.com/l3chat/eTiWi/actions/runs/45173445728
- Native KiCad 9.0.9 PDF inspected visually: controller on A2 to provide
  more symbol clearance; overview/sensors/audio on A4. C39 annotation
  returned to its actual symbol location; redundant FINGER labels hidden
  on touch pad symbols; QSPI text spacing refined.
- **KiCad ERC: 0 errors / 0 warnings** (rechecked after embedded
  symbol-library definitions were restored).
- Exact netlist comparison to the known-good V0.2 export:
  **77 identical net names and pin memberships, 255 pin connections**.
- This result supersedes the intermediate 60 warning report (which
  reflected a temporary mismatch of schematic-embedded library glyph
  text before the rollback); no such warnings remain.
- Physical footprint audit is in `FOOTPRINT_AUDIT.md`; the CI artifact
  now also includes a copy of that report for tablet access.
- No PCB has yet been created; U3 orientation/paste, USB-C mechanical
  cutout, RP2354A polarized switching inductor and supplier BOM must
  be approved at PCB design / assembly review.

## 2026-11-23 — AP2112K regulator schematic gate

Manufacturing review uncovered missing local U4 input capacitor and undersized
C2 output bypass. Updated U4 local decoupling to C201 1uF VBUS/GND and
C2 1uF +3V3/GND, Samsung CL10A105KP8NNNC 0603, JLCPCB C26413.
The KiCad ERC is now invoked with `--exit-code-violations` so warnings/errors
make GitHub Actions red while reports are still uploaded. Actual CI/netlist
pass must be checked after this commit. See `FOOTPRINT_AUDIT.md`.
