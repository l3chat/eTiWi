# eTiWi Mini hardware — planned, not yet schematic

## V0.1 blocks

1. **USB-C** device connector, CC1/CC2 Rd, VBUS path, USB ESD.
2. **3V3 rail** from VBUS; RP2354A local core regulator/reference inductor,
   crystal and all per-pin decoupling.
3. **RP2354A** with 2 MB in-package Flash, BOOTSEL, RESET, SWD test pads.
4. **MPR121QR2** on I2C, IRQ to MCU, 8 PCB copper electrodes.
5. **LPS28DFWTR** on the same I2C bus, provision for optional DRDY.
6. One debug/status LED and future-use pads.
7. **Universal audio connector**: unpopulated 2x6, 2.54 mm through-hole
   header exposing raw PWM/PDM, filtered AC-coupled mono analog, I2S,
   amplifier enable, 3V3, USB 5V and grounds. No on-board speaker amp.
   Small filter passives are installed at JLCPCB. An external module
   requires a correctly wired adapter and current-budget review.

## Design references

- Raspberry Pi RP2350 design guide (RP2354A package variant).
  https://pip.raspberrypi.com/categories/1214-rp2350
- NXP MPR121:
  https://www.nxp.com/docs/en/data-sheet/MPR121.pdf
- ST LPS28DFW:
  https://www.st.com/resource/en/datasheet/lps28dfw.pdf

## Files

- [Provisional pin plan](pin_plan.md).
- [Universal audio interface](audio_interface.md).
- [Candidate BOM](bom.csv) — **not a finalized procurement file**.
- [KiCad schematic](kicad/eTiWi-mini.kicad_sch) and [draft status](kicad/DESIGN_STATUS.md) — unverified electrical draft.

## Gate before manufacturing

For each component, lock exact MPN, package, KiCad symbol pin-map,
footprint land pattern, JLCPCB stock/assembly availability, reference
design schematic, power budget and ERC/DRC checks. BOM part numbers alone
do not prove a buildable or functional PCB.
