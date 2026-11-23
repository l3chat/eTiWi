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
