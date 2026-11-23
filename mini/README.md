# eTiWi Mini — V0.1 USB-MIDI prototype

eTiWi Mini is the **first, intentionally simplified hardware prototype** of
[eTiWi](../README.md): a breath- and fingering-controlled USB-MIDI instrument.

## V0.1 scope

- **RP2354A** (QFN-60, in-package 2 MB flash): MCU and USB-MIDI device.
- **MPR121QR2**: 8 copper capacitive-touch electrodes (12 available channels).
- **LPS28DFWTR**: digital, water-resistant pressure sensor for breath input.
- **USB-C**: 5 V bus power plus native USB 2.0 MIDI data to a host.
- **Universal audio expansion**: unpopulated 2x6, 2.54 mm through-hole header,
  raw PWM/PDM, factory-assembled filtered/AC-coupled mono analog audio,
  I2S digital audio signals, enable GPIO and power/ground. Bring your own
  tested amplifier/DAC module; no SMD amplifier is mounted in Mini V0.1.
  See [audio interface](hardware/audio_interface.md).

A computer, tablet or phone with USB host capability supplies the synth/audio
output for the **first bring-up**. Verify host support and USB power budget.

**Out of scope V0.1:** NiMH cells/charging, OLED, external MIDI backing-track
storage, VS1053B, headphone/line-out stages and autonomous play-along. These
remain part of the broader eTiWi vision; see `../hardware/`.

## Status

Architecture, pin plan, preliminary BOM and verification plan are documented.
**KiCad V0.3 includes an editable four-sheet schematic (A2 controller + three A4 sheets). ERC passed with 0 errors and 0 warnings in GitHub Actions (2026-11-23). PCB layout and firmware remain pending.**
This documentation is not manufacturing-ready.

## Files

- [Architecture](docs/architecture.md): signal and power flow.
- [Bring-up tests](docs/bringup.md): measurable first-board checks.
- [Hardware overview](hardware/README.md).
- [Pin allocation](hardware/pin_plan.md): provisional GPIO/I2C/USB plan.
- [Draft schematic BOM](hardware/bom.csv): catalog references
  and clearly marked unresolved parts.
- [Universal audio connector](hardware/audio_interface.md): safe module
  interface, hand-soldering options and provisional RC filter.
- [KiCad schematic and status](hardware/kicad/README.md).
- [Firmware plan](firmware/README.md): Pico SDK / TinyUSB; **no source yet**.

## Steps

1. Verify all part pinouts, RP2354A power/clock reference design, packages,
   speaker path and supply budget from current manufacturer datasheets.
2. **Completed:** create four-page KiCad schematic, resolve symbol libraries and run a clean ERC.
3. **Next:** verify manufacturer footprints and parts, route PCB, run DRC, prepare Gerbers/BOM/CPL.
4. Bring up USB, sensors and first MIDI note events (without audio amplifier).
5. Assemble/test PWM/PDM mono audio via an external appropriately rated
   amplifier, or I2S via an external DAC, using the audio header.

## Primary references

- [Raspberry Pi: Hardware design with RP2350](https://pip.raspberrypi.com/categories/1214-rp2350)
- [Raspberry Pi: RP2350 family datasheet](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf)
- [NXP: MPR121 datasheet](https://www.nxp.com/docs/en/data-sheet/MPR121.pdf)
- [ST: LPS28DFW datasheet](https://www.st.com/resource/en/datasheet/lps28dfw.pdf)
- [JLCPCB parts catalog](https://jlcpcb.com/parts)
