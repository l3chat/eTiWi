# Architecture Summary

## Inputs

- 6-8 analog IR sensors for fingering detection, routed through MCU ADC-capable
  inputs.
- Digital pressure sensor for breath input.
- Pressure sensor candidates noted in current docs: LPS28DFWTR, LPS25HBTR,
  LPS22HHTR.

## Processing

- Breath processing: thresholding, scaling, and smoothing.
- Fingering processing: hysteresis/debounce and transient handling.
- Note generation: fingering-table mapping to note/events.
- Presets: stored behavior sets for fingering and response tuning.

## Outputs

- Primary path: generated MIDI stream sent to VS1053B for onboard synthesis.
- Optional external path: USB-MIDI out to host device.

## Controller and Storage Direction

- MCU direction under evaluation: RP2350B.
- Use large external flash for firmware/assets; exact capacity target to be
  fixed during V1 hardware closure.
- Use FRAM for non-volatile settings/presets/calibration instead of EEPROM.
- VS1053B clocking is provided by MCU MCLK output (no dedicated VS1053B
  crystal in V1).

## Audio Path

- Headphones are the primary listening output.
- Line-out is provided for external active speakers/recording paths.
- On-board speaker is driven through an amplifier stage.
- Speaker auto-mute is controlled by jack-switch detection.

## Control Elements (V1)

- Power switch
- Rotary encoder with push
- Play/Stop button
- Back/Function button

## System Intent

The V1 target is stable, low-latency playability with clear behavior from
breath and finger input through MIDI generation to onboard audio output.
