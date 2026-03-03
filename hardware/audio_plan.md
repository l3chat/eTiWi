# Audio Plan

## Outputs

- Headphones (primary): VS1053B outputs plus 22-47 ohm series resistors;
  volume via SCI_VOL.
- Line-out: coupling capacitors to connector, mostly fixed level.
- On-board speaker: mono Class-D amp on SYS_5V (L+R mixed via resistors),
  EN/MUTE controlled by MCU.
- Auto-mute speaker: TRS jack with switch to amp mute and MCU GPIO.

## Layout Notes

- Keep the VS1053B analog zone away from boost and speaker power zones.
- Use a single-point ground tie.
