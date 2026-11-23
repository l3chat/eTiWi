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
- No KiCad schematic, fabricated PCB or working firmware exists yet.
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
