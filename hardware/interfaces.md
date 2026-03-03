# Interfaces - VS1053B and MCU

## Minimum Signals

- SPI: SCK, MOSI, MISO
- xCS (SCI), xDCS (SDI)
- DREQ, xRESET
- MCLK into XTALI (from MCU)

## Rules

- MCLK must be stable before releasing reset.
- SDI writes only when DREQ is high.
