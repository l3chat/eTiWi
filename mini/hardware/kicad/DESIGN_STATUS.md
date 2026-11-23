# eTiWi Mini schematic status (2026-11-23)

An editable **KiCad 9 .kicad_sch schematic** is now included, adapted from
the [jenschr/RP2354A MIT reference](https://github.com/jenschr/RP2354A).
The primary source is provided with license copy; see
`LICENSE_reference_RP2354A.txt`.

New electrical components added: MPR121QR2, 8 capacitive pad symbols and
corresponding PCB touch footprint, LPS28DFWTR, required MPR121 75k/1%
REXT and 100nF VREG bypass, I2C/IRQ pullups, pressure supply cap,
2x6 audio header and two-stage RC/AC coupling filter.

**NOT manufacturing ready.** A KiCad ERC/netlist export has NOT been run
(no KiCad CLI in this environment). The file passed only lexical
parenthesis, string and unique UUID checks. Further electrical review
and symbol/footprint verification are mandatory.

- Base reference has USB-C, RP2354A, core regulator, **polarized Abracon
  AOTA-B201610S3R3-101-T inductor**, crystal, LDO, SWD,
  buttons and GPIO breakout headers. Verify latest official design.
- Base still has demonstration RGB LED and two GPIO headers; these may
  be removed after testing if size/cost matter.
- LPS28DFWTR U3 footprint deliberately unassigned: verify CCLGA-7L
  land pattern from ST; the lid pad may be grounded.
- Check MPR121 footprint `UQFN-20_3x3mm_P0.4mm` against actual package.
- Verify original USB-C footprint/ESD/current handling for chosen connector
  and current JLCPCB procurement before ordering.
- Eight finger pads use initial custom 8x12mm mask-covered copper.
- All audio output is signal-level only: no on-board amp.
- No PCB or Gerber files have been produced.

Next:
```
kicad-cli sch erc mini/hardware/kicad/eTiWi-mini.kicad_sch -o mini-erc.txt
kicad-cli sch export netlist mini/hardware/kicad/eTiWi-mini.kicad_sch -o mini.net
```
Review manually in KiCad, correct ERC, assign actual footprints, generate
BOM from schematic, then layout PCB and run DRC.
