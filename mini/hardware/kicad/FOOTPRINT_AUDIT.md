# eTiWi Mini — component footprint engineering audit (2026-11-23)

This is a **component-library and datasheet cross-check**, NOT board DRC,
assembly sign-off, supplier quote, or working-hardware validation. KiCad
ERC does not check if physical pads are rotated or if manufacturer package
dimensions have been followed.

| Ref | Exact item / footprint | Audit outcome | Remaining gate |
| --- | --- | --- | --- |
| U1 | Raspberry Pi RP2354A, QFN-60-1EP 7×7 mm, pitch 0.4 mm, EP 3.4×3.4 mm | Nominal package and footprint match RP2350A/RP2354A | Check EP solder-paste pattern, thermal vias, regulator placement |
| U2 | NXP MPR121QR2, QFN-20 3×3 mm P0.4; KiCad UQFN-20_3x3mm_P0.4mm | Datasheet 1=IRQ, 2=SCL, 3=SDA, 4=ADDR, 5=VREG, 6=VSS, 7=REXT, 8..19=ELE0..11, 20=VDD match KiCad custom symbol. Footprint package nominated specifically for MPR121 | Verify actual pad width, fiducials, assembly orientation |
| U3 | ST LPS28DFWTR, 2.8×2.8 mm ceramic CCLGA-7L | **Critical correction made:** old library located pad 1 left and pad 4 right; ST Figure 19 has pads 1/4 opposite top/bottom. Now pad 1 at top, pad 4 bottom, side pins mirrored for PCB top view; 7 lid pad at center | Prototype **draft**: validate footprint orientation against ST package mark and assembly drawing, stencil volume and pressure-port clearance |
| J1 | Korean Hroparts TYPE-C-31-M-14, 16P plus shield, eTiWi local footprint | 16 electrical pad numbers, S1 shield and connector family match; JLCPCB C223907, Standard PCBA, high assembly difficulty; rated 1A | Compare board-edge/recess cutout and mounting orientation; USB ESD / VBUS protection is **not** validated |
| L1 | Abracon AOTA-B201610S3R3-101-T polarized 3.3µH | Local copper lands nominal 1.0×1.6mm, 1.0mm spacing as manufacturer drawing | **Mandatory** pad 1 orientation and regulator loop layout versus Raspberry Pi hardware reference, otherwise startup risk |
| U4 | AP2112K-3.3TRG1 / SOT-23-5 | Manufacturer family and KiCad package compatible | Verify pin1/enable/ground and copper thermal design |
| RESET1, USBDEV1 | C&K KMR241G LFS / KiCad SW_Push_1P1T_NO_CK_KMR2 | Pad pattern family compatible | Cross-check selected procurement revision/rotations at PCB layout |
| Y1 | Abracon ABM8-272-T3 / 3.2×2.5 4-pin SMD | Footprint nominal package consistent | Check grounded pads, load capacitors, crystal part exact CL and routing |
| J2,J3,J4,J5 | Standard 2.54mm connectors | Pin counts/spacing are appropriate for hand soldering | Choice of optional mounting and actual physical package, remove oversized development headers if Mini is optimized |
| TP1–TP8 | 8×12mm solder-mask-covered PCB copper pad | One electrical copper pad per touch electrode | Mechanical finger spacing and sensitivity test in real instrument |
| R/C components | KiCad 0402/0603 SMD patterns | Nominal sizes standard | Select JLCPCB exact parts and check voltage/X7R derating, paste and PCBA side |

## ST LPS28DFW detailed physical check

ST datasheet Figure 3 and Figure 19 depict contacts 1=SDA, 2=SA0,
3=SCL, 4=INT_DRDY, 5=GND, 6=VDD, 7=metal lid. The old custom
footprint rotated the perimeter contact pattern in an incompatible manner.
The revised footprint now arranges 1 TOP, 4 BOTTOM, 2/3 on one side and
6/5 on the other; note that the datasheet figure is *bottom view* and
the KiCad land pattern is drawn from the PCB *component side*.

ST drawing: pad1/4 approx 1.40 × 0.35mm, pad2/3/5/6 about 0.90 × 0.35mm,
and center lid about 0.90 × 0.90mm. In draft land pattern, perimeter lands
are increased by 0.1mm in each planar dimension (TN0018 rule, gaps >200µm).
Top-view orientation and exact solder stencil for this high-stress
water-resistant package **still require human fabrication review**.
Central pad7 is on GND, per ST recommendation.

ST datasheet: https://www.st.com/resource/en/datasheet/lps28dfw.pdf
ST mounting guide TN0018: https://www.st.com/resource/en/technical_note/CD00134799.pdf

## Manufacturing prerequisites

1. Check J1 connector cutout and JLCPCB assembly/paste/rotation and protect
   USB D+/D− with appropriate ESD before placing USB-C on the PCB.
2. Check L1 polarity and regulated 1.1V switching-current return loop:
   do NOT arbitrarily rotate the component.
3. Confirm U3 pin1 marker orientation using top/bottom package views,
   PCB top layer and JLCPCB pick-and-place file; no copper/vias near
   pressure port; follow ST reflow guidance.
4. Audit source KiCad project footprints versus actual JLCPCB BOM/CPL.
5. Run PCB DRC after actual board is routed; there is **no PCB yet**.

Sources: https://www.nxp.com/docs/en/data-sheet/MPR121.pdf
https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008280-DS-2-hardware-design-with-rp2350.pdf
https://abracon.com/datasheets/AOTA-B201610S.pdf
https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M14/C223907
