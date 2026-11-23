# KiCad schematic: eTiWi Mini V0.1

[eTiWi-mini.kicad_sch](eTiWi-mini.kicad_sch) is an editable KiCad 9
electrical draft based on the MIT-licensed reference design by jenschr.
Read [DESIGN_STATUS.md](DESIGN_STATUS.md) before fabrication.

The referenced footprint library `eTiWi.pretty/` contains
mask-covered copper touch electrodes and is registered in `fp-lib-table`.
Original license: `LICENSE_reference_RP2354A.txt`.

**No ERC/DRC, manufacture-ready BOM, PCB, Gerbers or verified pressure
sensor footprint yet.** The schematic must be opened, visually audited,
assigned the exact chosen footprints and passed through ERC before layout.

The automatically generated [BOM](../bom.csv) is a *draft matching the schematic*,
not a JLCPCB order file; see the unresolved footprint blockers in DESIGN_STATUS.md.

Project-local Abracon polarized inductor footprint is included in
`eTiWi.pretty/`; orient marked pad1 according to Raspberry Pi reference
layout, not just the schematic symbol.

Updated local `eTiWi.pretty/` now also includes the TYPE-C-31-M-14
USB footprint (copied from jenschr's Unlicense footprint repo), and a
**draft-only** LPS28DFW CCLGA-7L footprint. Switches use standard KiCad
KMR2 footprints. All new sensor power nets use `+3.3V` consistently.

Note: the inherited KiCad power symbol with library ID `power:+3.3V`
has **pin net name `+3V3`**, so the sensor local labels intentionally
use `+3V3`. Do not rename them to +3.3V without changing the
underlying power symbol net definition.

## Preview PDFs without KiCad (tablet / phone)

A GitHub Actions workflow is defined in
[`mini-kicad-preview.yml`](../../../.github/workflows/mini-kicad-preview.yml).
It is configured to export a **native KiCad schematic PDF** and an ERC
report when KiCad project files change or when the workflow is run manually.
Navigate to **GitHub → Actions → eTiWi Mini KiCad PDF and ERC → run →
Artifacts → etiwi-mini-kicad-previews** to obtain PDFs/reports.

When an actual `eTiWi-mini.kicad_pcb` is added, the same workflow is
configured to export a PCB PDF and DRC report, too. **No PCB exists yet**,
and the CI workflow output has not yet been verified by a completed run.

An independently prepared, three-page vector **functional electrical
preview** is provided to the user through the ChatGPT conversation. It is
not an exact KiCad graphical export and is not manufacturing approval.

## Readable KiCad V0.2 schematic

The main `eTiWi-mini.kicad_sch` is now a four-page KiCad hierarchy (overview plus three A4 functional sheets): `01_controller_usb_power.kicad_sch`, `02_touch_pressure.kicad_sch`, `03_audio_expansion.kicad_sch`. Signals crossing sheets use global labels. Custom symbols are provided in the portable project-local `sym_local/` library with `sym-lib-table`; original source licensed under MIT. Source components shifted onto the 50-mil grid. KiCad ERC and netlist validation are required after migration; the previous warnings apply only to the old monolithic design.
