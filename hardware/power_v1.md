# Power Architecture – V1 (no on-board charging)

- Sources: USB-C 5V OR 2×NiMH (2S) via boost to 5V
- Rails: SYS_5V -> low-noise SYS_3V3 for MCU + VS1053B, AVDD filtered from SYS_3V3
- V1 power-path: Schottky OR-ing; V2: ideal diode/power mux
- Battery monitoring: divider to MCU ADC + firmware cutoff
- Layout: separate noisy power ground from analog audio ground, join at one point
