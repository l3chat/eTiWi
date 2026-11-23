# eTiWi Mini firmware — planned (no code yet)

## Proposed stack

- C/C++ with official **Pico SDK** for RP2354A.
- **TinyUSB** USB device, class-compliant USB-MIDI implementation.
- I2C0 for MPR121 and LPS28DFW drivers.
- Simple note-state machine for fingering and breath response.
- Optional later: software oscillator/synthesis engine, PWM/PDM using
  hardware PWM or PIO + DMA and the onboard RC/AC-coupled analog output
  to an **external** analog amplifier, or PIO I2S to an external DAC/amp.
  A sample/clock/I2S stream must be implemented in firmware; reserved
  header pins alone do not generate audio.
- Do not copy third-party WARBL firmware; evaluate library license before
  adding external code.

## Logical modules once firmware work is explicitly authorized

- `board`: clock/IO/init, diagnostics and panic handlers.
- `touch`: electrode baseline, touch/release, adjacent-pad interference.
- `pressure`: reference pressure, filtering, threshold, hysteresis.
- `fingering`: 8-bit finger mask to note.
- `midi`: bounded-rate MIDI Note On/Off and optional CC2 over USB.
- `synth` (optional): low CPU-cost audio engine.

## Firmware bring-up sequence

1. Boot a minimal program and report status via debug.
2. Enumerate as **USB-MIDI** device and send test notes.
3. Scan I2C, read MPR121 touch bitmask.
4. Read pressure and display calibrated delta through debug.
5. Map pressure + fingers to live MIDI; prevent stuck notes.
6. Only then experiment with synthesis and an **external amp or I2S DAC**,
   checking USB power budget; start quiet with the 8-ohm speaker.

Record toolchain and SDK versions when implementation begins.
