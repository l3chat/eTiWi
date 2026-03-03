# Parts Candidates (Selection Guide)

## Power Conversion

- Boost 2S NiMH to 5V: prefer synchronous, EN pin, >=1A peak at 5V.
- LDO 5V to 3.3V: low noise, good PSRR, 300-600 mA class.

## Audio Output

- Speaker amp: mono Class-D on 5V, analog input, EN/MUTE pin.

## Memory and Storage

- Non-volatile settings/presets/calibration: use FRAM (not EEPROM).
- MCU/storage direction to evaluate: RP2350B plus large external flash
  (QSPI-class), with capacity target based on firmware + asset needs.

## Source OR-ing

- V1: Schottky OR-ing.
- V2: ideal diode or power mux.
