# eTiWi Mini — footprint audit, 2026-11-23

**Stage:** manufacturer drawing comparison and local CAD audit, **NOT** a
PCB design-rule / assembly sign-off. There is no routed PCB.

## Check results

| Ref | Device, geometry | Source / decision | Status |
| --- | --- | --- | --- |
| U1 | RP2354A, QFN-60-EP, 7 x 7 mm, 0.4 mm pitch, 3.4 x 3.4 EP | KiCad `QFN-60-1EP_7x7mm_P0.4mm_EP3.4x3.4mm`; package family confirmed against RP2350A/RP2354A datasheet | Nominal geometry consistent; actual copper EP/GND and vias require PCB review |
| U2 | NXP MPR121QR2, 3 x 3 mm QFN-COL, 20 terminals, 0.4 mm pitch | NXP MPR121 datasheet pp. 23–25; `UQFN-20_3x3mm_P0.4mm` | Body/pitch matched; review terminal metallization/heel width and pin 1 against NXP COL package |
| U3 | ST LPS28DFWTR, CCLGA-7L, 2.8 x 2.8 mm, six contacts + lid pad7 | ST DS13317 Fig. 3, Fig. 19; TN0018 pad/mask rules | **Corrected local pad widths and spacing**; DRAFT remains until stencil/solder mask verified |
| L1 | Abracon AOTA-B201610S3R3-101-T, 2.0 x 1.6 mm, polarized, 3.3 µH | Abracon recommended 1.0 x 1.6 pads with 1.0 mm gap, polarity ink dot | Copper nominal matches; **dot/1V1/VREG_LX orientation critical** |
| J1 | HRO TYPE-C-31-M-14 USB-C | Locally included jenschr/USB-C-Connectors footprint, 16 signal pads + 4 shield tabs | Supplier exact MPN and land pattern / ESD / orientation still require check |
| RESET1, USBDEV1 | C&K KMR241G LFS | Standard KiCad `Button_Switch_SMD:SW_Push_1P1T_NO_CK_KMR2` | Plausible package match; pin mapping / chosen available SKU to be verified |
| U4 | AP2112K-3.3, SOT-23-5 | KiCad `Package_TO_SOT_SMD:SOT-23-5` | Package class matched; pinout and thermal/VBUS budget at PCB review |
| Y1 | Abracon ABM8 quartz, 3.2 x 2.5 mm | KiCad `Crystal_SMD_3225-4Pin_3.2x2.5mm` | Verify exact ordered crystal and load network |
| J5 | 2x6 2.54 mm through-hole audio expansion pads | KiCad standard 2x6 PinHeader footprint | Fits easy hand soldering; header **not** fitted at factory |
| TP1–TP8 | Copper electrode 8 x 12 mm | Local copper-only pad on F.Cu, F.Mask aperture absent | Functional geometry candidate; ergonomic tuning, shielding and board outline pending |

## U3: corrected ST mechanical / electrical mapping

ST DS13317 (figures 3 and 19) draws package pads from **bottom**.
The KiCad footprint is drawn as seen from **top of the board**.
Thus the bottom view is mirrored so installed copper aligns properly:

```text
PCB TOP VIEW:
        6     5
   1       7       4
        2     3
```

- Pads 1 / 4: 0.45 x 1.50 mm (side vertical pads)
- Pads 2 / 3 / 5 / 6: 1.00 x 0.45 mm
- Pad 7: 0.975 x 1.00 mm, connected to GND in current schematic
- Body: 2.8 x 2.8 mm, max height ~2.1 mm
- Mask margin: 0.05 mm (0.10 mm aperture enlargement per dimension)
- Pad pitches and manufacturer tolerances need a PCB assembly audit.

**The preceding local footprint mistakenly used 0.55 mm-long
top/bottom copper pads** instead of approximately 0.90 mm package lands
plus the TN0018 margin. It has been corrected. The relative pad numbers
were consistent with the mirrored ST bottom view.

The datasheet explicitly permits grounding pad 7 or leaving it unconnected,
but recommends physically soldering it to PCB; current electrical design
grounds it.

### Primary manufacturer references

- ST DS13317 LPS28DFW, Fig. 3 (p.3), Fig. 19 (p.42):
  https://www.st.com/resource/en/datasheet/lps28dfw.pdf
- ST TN0018, §3.7 (p.12), LGA footprint and mask rules:
  https://www.st.com/resource/en/technical_note/tn0018-surface-mounting-guidelines-for-mems-sensors--in-an-lga-package--stmicroelectronics.pdf
- NXP MPR121 datasheet, pp.23–25:
  https://www.nxp.com/docs/en/data-sheet/MPR121.pdf
- Raspberry Pi RP2350 datasheet:
  https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf
- Abracon AOTA-B201610S3R3-101-T:
  https://cdn-reichelt.de/documents/datenblatt/A300/AOTA_B201610S3R3_101_T-3518993.pdf
- C&K KMR2:
  https://www.ckswitches.com/media/1479/kmr2.pdf

## Manufacturing blockers before PCB / JLCPCB quote

1. Independent orientation audit for U3 and L1 relative to actual pin1
   and assembly rotations; validate solder paste aperture/stencil for U3.
2. Select purchasable USB-C connector model and verify matched land pattern
   and USB2 electrical routing/ESD.
3. Verify MPR121 COL land pattern vs generic UQFN, and RP2354A exposed pad
   solder mask/paste + ground via strategy.
4. Determine mechanical placement, 8 touch pads and pressure port/moisture
   management; check allowable board finish and solder mask.
5. Final stocked LCSC choices for **every** part, BOM/CPL and PCBA service class.

A clean KiCad schematic ERC is necessary but **not sufficient** for any
of these. No `*.kicad_pcb`, DRC, Gerbers or CPL currently exists.

## Additional part-catalog evidence

- HRO `TYPE-C-31-M-14`: JLCPCB/LCSC **C223907**; listing calls it
  16-pin USB Type-C, 1 A rated. A listing is not a verified solder
  footprint, and inventory/PCBA support must be checked at order time:
  https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M14/C223907
- Abracon `AOTA-B201610S3R3-101-T`: JLCPCB/LCSC **C42411119**:
  https://jlcpcb.com/partdetail/AbraconLLC-AOTA_B201610S3R3_101T/C42411119
- The manufacturing footprints remain subject to pad, assembly rotation
  and available stock confirmation; candidates in BOM are **not** approval.
