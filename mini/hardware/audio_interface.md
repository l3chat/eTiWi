# Universal audio expansion connector — eTiWi Mini V0.1

**Decision:** no on-board audio amplifier, no soldered speaker-driver chip
and no speaker output terminal on the first Mini PCB. The board exports
**low-power signal-level audio interfaces** for a user-supplied analog
amplifier or I2S DAC/amplifier module. The header pads use **2.54 mm plated
through-holes** so hand-soldering is easy. A connector need not be populated.

## J_AUDIO: 2x6, 2.54 mm, provisional electrical pinout

This is the *electrical design contract* for the later KiCad schematic.
PCB mechanical pin-1 marking, female/male connector choice and pad numbering
must be checked on the eventual native KiCad footprint and silkscreen.

| Pin | Name | Direction | Usage |
| --- | --- | --- | --- |
| 1 | GND | power return | Common signal and power return |
| 2 | USB_5V | power output | VBUS from USB; power budget required |
| 3 | GND | power return | Ground near power rails |
| 4 | 3V3 | power output | Regulated 3.3 V; limited by LDO capacity |
| 5 | AUDIO_PWM_RAW | MCU output | GP5; high-frequency 3.3 V PWM/PDM only |
| 6 | AUDIO_OUT | analog output | LPF + AC-coupled mono audio from GP5 |
| 7 | AMP_EN | MCU output | GP6, 3.3 V logic; active polarity depends on module |
| 8 | GND | return | Analog/module ground |
| 9 | I2S_BCLK | MCU output | GP10 via PIO |
| 10 | I2S_LRCLK | MCU output | GP11 via PIO |
| 11 | I2S_DOUT | MCU output | GP12 via PIO |
| 12 | GND | return | I2S ground |

**Always wire by signal name, not by guesswork:** these contacts are NOT a
standardized I2S or amplifier module pinout. Use a short, labeled adapter
cable or solder wires directly to the plated holes. No on-board I2S MCLK
is dedicated in V0.1; modules requiring MCLK are not automatically
compatible (a free GPIO can be added later).

## Factory-assembled provisional mono audio filter

```text
RP2354A GP5 PWM_RAW ---+-------------------------------> J_AUDIO pin 5
                       |
                       R_A1 1k
                       |
                N1 ----+---- C_A1 10nF ---- GND
                       |
                       R_A2 1k
                       |
                N2 ----+---- C_A2 10nF ---- GND
                       |
                  C_A3 1uF (non-polar ceramic, AC coupling)
                       |
                AUDIO_OUT ---- R_A3 100k ---- GND
                       |
                       +-------------------------------> J_AUDIO pin 6

RP2354A GP6 ---- R_AEN 1k -----------------------------> J_AUDIO pin 7
RP2354A GP10/11/12 ------------------------------------> I2S pins 9/10/11
```

R/C values above are **initial candidate values**, not an optimized
production analog output. The two passive stages have a nominal individual
unloaded corner around 15.9 kHz; stages load one another, and module input
impedance changes actual frequency response and output amplitude.
The signal is **mono, unbuffered, AC-coupled and low-current**.
Some analog amplifier modules already include input capacitors/biasing:
review their schematic before connecting. Start firmware output at low volume.

All resistors/capacitors here should be standard 0603/0805 SMD footprints,
**factory populated at JLCPCB**. Do not request manual soldering of SMDs.

## How to connect modules

### A. Analog-input amplifier (e.g. a ready-made class-D mono module)

- GND -> module GND
- USB_5V -> module supply ONLY if module is rated for 5 V and USB host
  current allowance is sufficient
- AUDIO_OUT -> module LINE/IN+ or audio input (as its manual specifies)
- AMP_EN -> module enable/shutdown only after checking polarity/levels;
  otherwise omit and use the module's permanent enable.
- Module's **SPK+ and SPK-** -> actual 8-ohm speaker.
  BTL speaker `SPK-` is **NOT** ground.

### B. Digital I2S DAC or I2S speaker amplifier

- 3V3 (or USB_5V if supported by that module), GND,
  I2S_BCLK, I2S_LRCLK (WS), I2S_DOUT -> corresponding module pins.
- No I2S stream is produced until RP2354A PIO firmware implements one.
- I2S is **not** equivalent to PWM/PDM; do not interchange connections.
- Check any required external MCLK, exact logic voltage, and gain/power.

### C. Speaker only / raw transistor stage

**Unsupported.** Never put a low-impedance speaker directly across GP5
and GND or directly from AUDIO_OUT, and never assume a single small
transistor is a safe 5 V speaker amplifier. Use a rated amplifier.

## USB power safety / assembly

- USB-C VBUS may be 5 V but cannot be treated as unlimited current.
  USB host and port limits, enumeration/current advertisement and any
  protective switch/fuse must be checked before using external amplifiers.
- A 3V3 rail may be unable to supply power-hungry speaker amplifiers.
  The header must not expose 5 V to RP2354A GPIO or I2S signals.
- Provide local decoupling on the *external module*, short audio/ground
  wiring and keep sensor electrodes away from high-current speaker loops.
- On the first PCB, **do not populate** J_AUDIO by default; both a
  2x6 header and individual wires can be attached with an ordinary iron.
- Label pin 1, both voltage rails, and each audio signal on silkscreen.
  Keep through-hole pads accessible from the finished enclosure.
- Add an optional 4-pin analog breakout footprint only if a selected
  amplifier module justifies it; avoid multiplying connectors for now.

## Gate before KiCad sign-off

1. Verify RP2354A GPIO assignments against its exact physical pin map.
2. Verify available I2S/PIO clocking against intended audio sample rate.
3. Evaluate RC/filter/AC coupling against the actual module input.
4. Verify 2x6 connector footprint and pin numbering in KiCad.
5. Confirm all SMD components are JLCPCB-assemblable and quote parts.
6. Run KiCad ERC then PCB DRC; inspect USB host current limits.
