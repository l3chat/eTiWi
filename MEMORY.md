# MEMORY

Stand: 2026-03-03

## Stable Decisions

- Device concept: electronic tin whistle with onboard VS1053B GM synthesis.
- MIDI generation is driven by breath + fingering in real time.
- V1 supports MIDI play-along by mixing live performance with backing-track
  MIDI in the same synth path.
- USB-MIDI out remains an optional external output mode.
- Session workflow rule: before every commit, refresh `MEMORY.md` and
  `CHAT.md` to match staged changes.

## V1 Hardware Decisions

- Battery: 2x NiMH.
- V1 has no on-board NiMH charging.
- Power rails: SYS_5V + low-noise SYS_3V3.
- VS1053B is on the same PCB as MCU.
- VS1053B clocking: MCU MCLK output to XTALI, no dedicated VS1053B
  quartz/crystal in V1.
- Non-volatile settings/presets storage: FRAM, not EEPROM.
- Audio path priority: headphones primary, line-out available, on-board
  speaker through dedicated amp.
- Speaker auto-mute is driven by a jack switch.
- V1 controls: power switch, rotary encoder with push, play/stop button,
  back/function button.

## Architecture Snapshot

- Inputs: 6-8 analog IR sensors + digital pressure sensor candidate family
  (LPS28DFWTR / LPS25HBTR / LPS22HHTR).
- Processing intent: threshold/hysteresis/debounce + fingering tables + presets.
- Outputs: MIDI stream to VS1053B, optional USB-MIDI out.
- MCU/storage direction under evaluation: RP2350B + large external flash.

## Open Hardware Choices (V1)

- Speaker amp class and pot/no-pot decision.
- Boost converter peak-current target and part category.
- USB-C sink CC resistors and ESD placement.
- I2C bus/address plan for OLED + pressure sensor.
- RP2350B I/O fit and external flash size/interface finalization.
- Ground split and single-point tie placement.
