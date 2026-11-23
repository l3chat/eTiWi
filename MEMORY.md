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
