# Architecture Summary

## Inputs

- 6-8 analog IR sensors for fingering detection, planned through RP2354B ADC
  channels (up to 8 ADC inputs available).
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

## Audio Path

- Headphones are the primary listening output.
- Line-out is provided for external active speakers/recording paths.
- On-board speaker is driven through an amplifier stage.
- Speaker auto-mute is controlled by jack-switch detection.

## System Intent

The V1 target is stable, low-latency playability with clear behavior from
breath and finger input through MIDI generation to onboard audio output.
