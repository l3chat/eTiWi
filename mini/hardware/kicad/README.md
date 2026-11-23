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
3. `03_audio_expansion`: GP5 raw PWM/PDM, R-C/R-C low-pass,
   series AC coupling, GP6 amplifier enable, GP10..12 I2S PIO pins,
   unpopulated 2x6 through-hole header. No on-board amplifier.

## Review checklist before Gerbers

- Obtain latest official RP2350 hardware design PDF and its BOM/layout;
  use **correct polarized core-regulator inductor** and crystal network.
- Cross-check every KiCad symbol pad number against the exact IC datasheet.
- Use manufacturer-recommended footprints, polarity/pin-1 silk details.
- Include **both USB-C Rd resistors**, USB D+/D- proper connector mapping,
  ESD and safe VBUS handling.
- Verify I2C addresses, pull-ups, sensor IRQ/strap and pressure port direction.
- Confirm analog filter values under actual module input loading;
  factory-assemble filter passives; keep header through-hole and optional.
- Confirm the external amplifier/DAC module does not overload USB power;
  do not connect a speaker to MCU GPIO or ground a bridge output.
- Silk-screen every header pin and voltage clearly, especially +5V vs +3V3.
- Run KiCad **ERC**, inspect netlist, then **DRC**, inspect Gerbers.
- Generate and independently inspect JLCPCB BOM (C numbers) + CPL/centroids.
- Recheck component availability and PCBA tier before purchasing.
