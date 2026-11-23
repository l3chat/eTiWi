# eTiWi Mini architecture — V0.1

## Functional diagram

```text
USB-C host: 5 V VBUS + USB D+/D-
       |                    |
       v                    v
  3.3 V LDO             RP2354A USB
       |                    |
       +---- 3V3 -----------+---- RP2354A core supply infrastructure
       |                    |      (internal regulator + reference inductor)
       +---- MPR121         |
       +---- LPS28DFW       |
                            +---- I2C0 SDA/SCL --> MPR121 / LPS28DFW
                            +---- GPIO/IRQ <----- MPR121 IRQ
                            +---- GPIO (optional) <- pressure DRDY
                            +---- USB-MIDI ------> external sound engine
                            +---- reserved PWM/PDM -> filter -> amplifier
```

MCU 2 MB in-package flash suffices for initial firmware and small settings;
no additional program flash or FRAM required in Mini V0.1.

## Signal interpretation

- Copper electrodes -> 8 independently detectable finger states; use
  MPR121 autoconfiguration plus debouncing / release hysteresis.
- LPS28DFW -> pressure relative to a baseline measured in idle state.
- Idle-to-blow transition: Note On, velocity from pressure/musical mapping.
- Fingering change: terminate old note and start the mapped new note; handle
  legato carefully to avoid stuck notes.
- Falling below release threshold: Note Off.
- Optional expression: MIDI CC2 (breath controller) at a bounded event rate.
- At loss of pressure readings or USB disconnect: enter a safe silent state.

## Shared I2C

Plan: RP2354A I2C0 on GP0 (SDA), GP1 (SCL) with external pull-ups to 3V3.
Candidate 7-bit addresses: MPR121 **0x5A** with ADDR grounded; LPS28DFW
**0x5C** with SA0 low (or 0x5D high). Check device strapping, signal voltage,
pull-up placement and the selected package pins before schematic release.

## Power and USB design constraints

- USB-C USB 2.0 device/sink: CC1 and CC2 each need **5.1 kohm Rd to GND**,
  not a single shared resistor.
- USB D+/D- to the RP2354A dedicated USB pins; route as a coupled pair.
  Add ESD protection near the receptacle; follow RP2350 reference design
  before adding optional series resistors/termination.
- LDO from VBUS to 3V3. Use its specified input/output capacitors.
- RP2354A has **its own internal core regulator**, not simply 3V3 power on
  every pin. Follow current Raspberry Pi RP2350 hardware design reference
  for regulator, **specified polarized inductor**, crystal and decoupling.
- Use the recommended 12 MHz reference oscillator network for USB clocking.
- Continuous GND plane; control sensor, USB and audio/power return paths.
- Low-noise, short, dry electrode traces; reserve ground shielding/guard
  experiments **without** adding ground directly beneath sensing electrodes.

## Optional speaker

Reserve one MCU GPIO suitable for PWM/PIO output and an amplifier enable
pin. Audio output must go through an appropriate reconstruction/low-pass
filter, gain stage and **separate speaker driver**. Never connect an 8-ohm
speaker directly to an RP2354A GPIO or use a small signal transistor as an
unlimited 5 V switch. Power an optional 5 V amp from USB VBUS only after
verifying connector/host USB current budget and amp ratings.

## Mechanical notes

The electrodes should be designed for two rows of finger positions, with
adjustable spacing in the first prototype. Keep finger electrodes away from
USB ground, MPR121 and switching-power loops. The pressure sensor port needs
a moisture-management channel or trap; protective gel does not make the
assembly immune to pooled water or contamination.
