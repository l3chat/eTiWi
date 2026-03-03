# Layout & Placement Notes

Zones:
1) Digital (MCU/USB/SPI)
2) Analog audio (VS1053B outputs, AVDD filter, jacks)
3) Noisy power (boost, speaker amp, battery, SYS_5V bulk)

Ground:
- separate power return from analog ground
- join at one low-impedance point near power entry / SYS_5V bulk

Routing:
- keep boost switch node small and away from analog
- keep speaker outputs away from analog
- keep MCLK short; consider series resistor near MCU
