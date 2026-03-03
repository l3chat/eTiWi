# Interfaces – VS1053B <-> MCU

Minimum:
- SPI: SCK, MOSI, MISO
- xCS (SCI), xDCS (SDI)
- DREQ, xRESET
- MCLK into XTALI (from MCU)

Rules:
- MCLK stable before releasing reset
- SDI writes only when DREQ high
