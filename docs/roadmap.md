# Roadmap

## V1 (Current Focus)

Goal: stable playing plus basic play-along using MIDI backing tracks.

- Finalize core hardware choices for power, audio path, interfaces, and
  sensors.
- Validate stable breath + fingering to MIDI behavior assumptions.
- Support live MIDI performance mixed with backing-track MIDI in the VS1053B
  path.
- Keep USB-MIDI output available as an optional external mode.

## V2 (Next Iteration)

Goal: improve power management and refine sensing robustness.

- Add NiMH charging support.
- Improve power mux/OR-ing behavior beyond the V1 Schottky approach.
- Refine sensor calibration and noise handling.
- Tune response curves/hysteresis/debounce for more consistent playability.
