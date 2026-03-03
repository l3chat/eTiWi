# Hardware Notes (V1)

This folder contains V1 hardware planning notes for a compact VS1053B + MCU
board aimed at real-time MIDI playback and play-along use.

## V1 Decisions

- 2x NiMH, no on-board charging
- SYS_5V + low-noise SYS_3V3
- VS1053B on same PCB
- Headphones primary, line-out, speaker via amp, auto-mute with jack switch
- Play-along via MIDI backing tracks

## Document Index

- `power_v1.md`: power architecture for V1, including source selection, rail
  strategy, and layout grounding intent.
- `audio_plan.md`: output-path plan for headphones, line-out, and speaker
  amplification with jack-based speaker muting.
- `interfaces.md`: minimum VS1053B-to-MCU signal map and operating rules for
  clocking and SDI writes.
- `parts_candidates.md`: component-category shortlist criteria for power and
  audio blocks.
- `warbl_to_ours.md`: implementation ideas adapted from WARBL behavior, with
  a clean-room license reminder.
- `midi_sources.md`: external MIDI source references for accompaniment-focused
  play-along content.
- `kicad/README.md`: placement and routing constraints to guide future
  schematic/layout work.
- `todo.md`: tracked TODO and DONE items for V1 hardware decisions.
