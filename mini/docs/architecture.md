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
                            +---- GP5 PWM/PDM --> low-pass + AC coupling --+
                            |                                     AUDIO_OUT
                            +---- GP6 (AMP_EN), GP10..12 (PIO I2S) --------+
                                                                  2x6 HEADER
                                                                  (ext. module)
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

## Universal audio expansion (no onboard amp)

A **2x6, 2.54 mm through-hole pad field**, optionally fitted with a header,
exports grounds, regulated 3V3, USB 5V, GP5 PWM/PDM_RAW, GP6 AMP_EN,
GP10 I2S_BCLK, GP11 I2S_LRCLK, GP12 I2S_DOUT, and an AC-coupled mono
AUDIO_OUT formed by a two-stage RC filter from GP5. The RC/filter capacitors
are inexpensive SMD components intended for factory assembly.

This accommodates (a) analog-input class-D amplifier modules using
AUDIO_OUT, or (b) digital-I2S DAC/amplifier modules using the I2S signals.
No amplifier chip, speaker connector or speaker power stage is placed on the
Mini V0.1 PCB. The header is not plug-and-play with any particular module;
check its pin order, logic and power ratings and use a wired adapter.

Never connect an 8-ohm speaker directly to an RP2354A GPIO, to the AC
coupled output, or as a load on a small-signal transistor. Power a 5V amp
from USB VBUS **only** after checking the USB host/port current budget and
adding adequate supply protection and local bypass capacitors on the module.
See [audio interface wiring](../hardware/audio_interface.md).

## Mechanical notes

The electrodes should be designed for two rows of finger positions, with
adjustable spacing in the first prototype. Keep finger electrodes away from
USB ground, MPR121 and switching-power loops. The pressure sensor port needs
a moisture-management channel or trap; protective gel does not make the
assembly immune to pooled water or contamination.
