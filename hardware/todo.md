# TODO / DONE

## TODO (V1)

- [ ] Measure speaker Rdc on selected candidate and record value in ohms.
- [ ] Select speaker amp class (mono Class-D at 5V) and decide whether an
  input potentiometer is required.
- [ ] Define boost target for 2S NiMH to 5V (including peak current
  requirement) and choose part category.
- [ ] Select a low-noise 3.3V LDO class with PSRR/current targets for MCU +
  VS1053B.
- [ ] Choose TRS headphone jack with switch and define required switch
  behavior for speaker auto-mute.
- [ ] Add battery ADC divider plan and define firmware cutoff thresholds.
- [ ] Add reverse-polarity protection approach for the battery path.
- [ ] Decide USB-C sink CC resistor values and ESD diode placement near
  connector entry.
- [ ] Define I2C bus plan and addresses for OLED + pressure sensor candidates.
- [ ] Decide pressure sensor candidate for V1 (LPS28DFWTR, LPS25HBTR, or
  LPS22HHTR) and confirm voltage/interface fit.
- [ ] Decide analog/power ground split regions and single-point tie location
  on PCB.

## DONE

- [x] V1: no on-board NiMH charging.
- [x] Battery: 2x NiMH.
- [x] USB-C: power + USB-MIDI.
- [x] SYS_5V + SYS_3V3 architecture.
- [x] Speaker uses dedicated amplifier.
