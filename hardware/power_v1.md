# Power Architecture - V1 (No On-Board Charging)

## Sources

- USB-C 5V
- 2x NiMH (2S), boosted to 5V

## Rails

- SYS_5V
- Low-noise SYS_3V3 for MCU + VS1053B
- AVDD filtered from SYS_3V3

## Power Path

- V1: Schottky OR-ing
- V2: ideal diode/power mux

## Monitoring and Layout Notes

- Battery monitoring via divider to MCU ADC, with firmware cutoff.
- Keep noisy power ground separate from analog audio ground and join at one
  point.
