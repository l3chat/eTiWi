# KiCad project scaffold

This folder is reserved for a real editable KiCad project. **No fabricated
or empty .kicad_sch / .kicad_pcb files are committed as if validated.**

Create these files in KiCad during schematic capture:

- `eTiWi-mini.kicad_pro` — native project settings.
- `eTiWi-mini.kicad_sch` — electrically connected schematic.
- `eTiWi-mini.kicad_pcb` — routed PCB only after schematic review.

## Recommended schematic sheets

1. `01_usb_power_mcu`: USB-C, ESD, 3V3, RP2354A core regulator,
   reference inductor, 12 MHz reference, reset, BOOTSEL, SWD.
2. `02_touch_pressure`: MPR121, 8 PCB electrodes, LPS28DFW, I2C.
3. `03_audio_optional`: reserved MCU PWM/PDM output; designed filter,
   analog-input mono amp, speaker connector; mark do-not-populate by default.

## Review checklist before Gerbers

- Obtain latest official RP2350 hardware design PDF and its BOM/layout;
  use **correct polarized core-regulator inductor** and crystal network.
- Cross-check every KiCad symbol pad number against the exact IC datasheet.
- Use manufacturer-recommended footprints, polarity/pin-1 silk details.
- Include **both USB-C Rd resistors**, USB D+/D- proper connector mapping,
  ESD and safe VBUS handling.
- Verify I2C addresses, pull-ups, sensor IRQ/strap and pressure port direction.
- Confirm analog/audio filter and the amplifier do not overload USB power.
- Run KiCad **ERC**, inspect netlist, then **DRC**, inspect Gerbers.
- Generate and independently inspect JLCPCB BOM (C numbers) + CPL/centroids.
- Recheck component availability and PCBA tier before purchasing.
