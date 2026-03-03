# Interfaces - VS1053B and MCU

## Minimum Signals

- SPI: SCK, MOSI, MISO
- xCS (SCI), xDCS (SDI)
- DREQ, xRESET
- MCLK into XTALI (from MCU)

## Clocking Decision (V1)

- VS1053B XTALI is driven from an MCU clock output (MCLK).
- No dedicated quartz/crystal resonator is planned for VS1053B in V1.

## Rules

- MCLK must be stable before releasing reset.
- SDI writes only when DREQ is high.
