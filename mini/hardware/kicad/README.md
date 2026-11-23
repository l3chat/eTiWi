# eTiWi Mini V0.2 — KiCad 9 schematic

**Editable four-sheet schematic (A2 core + three A4), ERC 0 errors and 0 warnings.**
See [DESIGN_STATUS.md](DESIGN_STATUS.md) for current verified status,
non-validated physical details, and the most recent PDF/ERC workflow.

## Main entry

- [eTiWi-mini.kicad_sch](eTiWi-mini.kicad_sch) — hierarchical root.
- [01_controller_usb_power.kicad_sch](01_controller_usb_power.kicad_sch)
  — RP2354A, USB-C, 3.3 V, clock, SWD/debug.
- [02_touch_pressure.kicad_sch](02_touch_pressure.kicad_sch)
  — MPR121/8 electrodes and LPS28DFW.
- [03_audio_expansion.kicad_sch](03_audio_expansion.kicad_sch)
  — optional 2×6 module header, RC/PWM or digital I2S.
- [eTiWi-mini.kicad_pro](eTiWi-mini.kicad_pro) — KiCad project settings.

Reusable symbol and footprint libraries are included locally in
`sym_local/` and `eTiWi.pretty/`, registered in `sym-lib-table`
and `fp-lib-table`. Keep these files together with the schematic.

The core reference is based on the MIT-licensed
[jenschr/RP2354A](https://github.com/jenschr/RP2354A) reference,
whose license is included as `LICENSE_reference_RP2354A.txt`.
The USB-C footprint comes from the Unlicensed
[jenschr/USB-C-Connectors](https://github.com/jenschr/USB-C-Connectors);
its license copy is included too.

**Important:** ERC success is not proof that footprints, power or
manufacturing details are correct. No PCB or DRC exists yet.
