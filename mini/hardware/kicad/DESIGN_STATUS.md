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

## Additional post-commit audit

- Electrical label/wire check: 96 labels, 255 wires; all labels for
  I2C_SDA, I2C_SCL, TOUCH_IRQ, PRESS_INT, AUDIO_PWM_RAW, AMP_EN,
  I2S_BCLK, I2S_LRCLK, I2S_DOUT, AUDIO_OUT, MPR_VREG and MPR_REXT
  were found attached to actual schematic wires. This is **not ERC**.
- Newly generated BOM `../bom.csv` now tracks the **53 assembly-capable
  components from the actual schematic**, including DNP header J5.
  Touch electrodes TP1..TP8 are PCB copper and excluded from assembly BOM.
- Important inherited reference footprint blockers:
  - `J1` USB-C uses `USB-C-Power-tester:TYPE-C-31-M-14` —
    external private footprint library is not included here.
  - `USBDEV1` switch also uses an external private footprint library.
  - `L1` polarized Abracon 3.3uH inductor is temporarily assigned an
    ordinary resistor-0805 footprint in the source reference; **must
    verify and replace**, and enforce inductor polarity/orientation.
  - `U3` LPS28DFW still has no verified CCLGA-7L footprint assigned.
  - Any other reference-board MPN and footprint must still be checked.
- **Do not send the supplied schematic/BOM directly to JLCPCB.** A
  manufacturer-qualified footprint selection, proper local library,
  ERC, and human review remain required.

## 2026-11-23: L1 footprint correction (draft)

- Replaced the inherited resistor-0805 pad pattern of L1 with project-local
  `eTiWi:Abracon_AOTA_B201610S3R3_101_T`.
- Physical land pattern uses manufacturer's two 1.0x1.6mm pads separated
  by 1.0mm. The marker is placed near pad1; reference Raspberry Pi
  regulator drawing has the marked pad on +1V1 side and VREG_LX on pad2.
- **This is not a qualified SMPS layout.** Review the actual on-board
  inductor rotation and capacitors/loop geometry against the official
  Raspberry Pi RP2350 guide (especially its Figure 4) before routing.
- Previously identified J1, RESET1 and USBDEV1 private-library footprints,
  and U3 CCLGA pressure footprint, remain unresolved.

## 2026-11-23: Footprints and power-net correction

- Fixed **eight mislabeled +3V3 local nets** to **+3.3V** (the
  inherited RP2354A power-symbol net). This was an actual design bug:
  previous sensors and pull-ups were NOT connected to the 3.3V source.
- Added a project-local **TYPE-C-31-M-14** USB footprint copied from
  jenschr/USB-C-Connectors (Unlicense). Mapped footprint mounting pads
  to the symbol's S1 shield. Extra A8/B8 SBU pads intentionally remain
  unused. Connector final geometry and orientation still need PCB review.
- Replaced both switch footprints RESET1 and USBDEV1 with matching standard
  KiCad `Button_Switch_SMD:SW_Push_1P1T_NO_CK_KMR2`.
- Assigned a **provisional** project-local `LPS28DFW_CCLGA-7L_2.8x2.8mm_DRAFT`
  footprint with six pads and central pad 7. Pin arrangement follows
  the ST datasheet bottom-view mirror; land widths are tentative
  (must check manufacturer guidance TN0018 and production line).
- Updated schematic BOM. These changes reduce missing-file dependencies,
  but they **do not constitute an ERC pass**.

## Verified supply net semantics (correction to previous wording)

The inherited symbol is `power:+3.3V`, but its embedded power pin
**electrical net name is +3V3** (while the symbol's displayed library value
is +3.3V). Therefore the eight Mini supply labels must be **+3V3**, not
+3.3V. I verified the embedded `(name "+3V3")` from the actual
KiCad library symbol and restored these eight labels to +3V3.
This correction supersedes the earlier claim that +3V3 was an error.

## Current status of automated KiCad checks

- GitHub workflow `.github/workflows/mini-kicad-preview.yml` was added
  to run KiCad 9 via the official container, export PDF and netlist, run
  ERC and upload outputs as GitHub Actions artifacts.
- **At time of this note no completed run/individual ERC violation list
  has been verified.** An ERC exit code of nonzero is written into the
  artifact report; PDF export alone does not mean ERC passed.
- When an actual PCB appears, the workflow contains a conditional
  PDF plot and DRC report for its layers. No PCB file exists yet.
