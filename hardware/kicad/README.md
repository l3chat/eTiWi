# Layout and Placement Notes

## Zones

1. Digital (MCU/USB/SPI)
2. Analog audio (VS1053B outputs, AVDD filter, jacks)
3. Noisy power (boost, speaker amp, battery, SYS_5V bulk)

## Ground

- Keep power return separate from analog ground.
- Join them at one low-impedance point near power entry or SYS_5V bulk.

## Routing

- Keep boost switch node small and away from analog.
- Keep speaker outputs away from analog.
- Keep MCLK short; consider a series resistor near MCU.
