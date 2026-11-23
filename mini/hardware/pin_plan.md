# Provisional RP2354A pin/resource plan

This is a **logical GPIO plan**, not a QFN-60 physical pad-number map.
Confirm pin mux, actual pad numbers, boot constraints, I/O voltage and
alternate functions in the RP2350/RP2354 datasheet and KiCad.

| RP2354A signal | Role | Notes |
| --- | --- | --- |
| GP0 | I2C0 SDA | MPR121 + LPS28DFW, 3V3 pull-up |
| GP1 | I2C0 SCL | MPR121 + LPS28DFW, 3V3 pull-up |
| GP2 | MPR121 IRQ | Active-low, check pull-up/interface |
| GP3 | LPS28DFW INT/DRDY | Optional: may leave unused/poll I2C |
| GP4 | Status LED | Series resistor; active level TBD |
| GP5 | PWM/PDM audio data | RESERVED, no speaker connected directly |
| GP6 | Amplifier enable/mute | Optional future-populated audio |
| GP7 | Control button 1 | Optional |
| GP8 | Control button 2 | Optional |
| GP9 | Future control / test | Optional |
| SWCLK, SWDIO | Debug pads | Dedicated debug interface |
| RUN | Reset access | Validate pull-up and reset network |
| USB_DP, USB_DM | Native USB data | Dedicated USB pins, not GPIO |
| XIN, XOUT | 12 MHz crystal | Reference clock network |
| QSPI_SS / flash pins | In-package flash / BOOTSEL | Do not repurpose |

**Not assigned:** remaining GPIOs. Keep room for later controls, OLED and
a possible VS1053B interface. The on-chip power network needs separate
pin-by-pin treatment from the official hardware design reference.
