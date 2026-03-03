# Audio Plan

Outputs:
- Headphones (primary): VS1053B outputs + 22–47Ω series resistors, volume via SCI_VOL
- Line-out: coupling caps to connector, mostly fixed-level
- On-board speaker: mono Class-D amp on SYS_5V (L+R mixed via resistors), EN/MUTE controlled by MCU
- Auto-mute speaker: TRS jack with switch -> amp mute + MCU GPIO

Layout: keep VS1053B analog zone away from boost + speaker power zone; single-point ground tie.
