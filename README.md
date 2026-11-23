# eTiWi

eTiWi is an electronic tin whistle with a built-in VS1053B General MIDI
synth. It generates real-time MIDI from breath and fingering, and supports
MIDI play-along by mixing live performance with backing-track MIDI inside the
same synth engine.

## Overview

- Features: real-time whistle-style control, MIDI play-along inside the
  onboard synth, and USB-MIDI device mode for computer/tablet use.
- Hardware: VS1053B synth plus MCU, with audio outputs for headphones
  (primary), line-out, and an on-board speaker via amplifier.
- Power: designed around a 2x NiMH battery path and USB-C powered operation.
- Status: early design and documentation stage.

## eTiWi Mini — first prototype

The immediate milestone is [eTiWi Mini](mini/README.md): an RP2354A USB-MIDI
controller with eight MPR121 capacitive electrodes and an LPS28DFW breath
sensor, powered from USB-C. The first tests use an **external MIDI synth**;
a PWM/PDM speaker-output stage is reserved as an optional later experiment.
The original VS1053B, battery-powered design remains a longer-term goal.

## Project Status

The project is currently in early hardware and firmware planning.
Architecture notes, power/audio/interface decisions, and parts candidates are
being consolidated before schematic capture, PCB work, and firmware
implementation.
