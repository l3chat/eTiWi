# eTiWi Mini PCB - mechanical and routing design contract (draft)

Date: 2026-11-23. **A design proposal, not a fabricated or routed PCB.**
The official RP2350 hardware guide must govern the regulator core.

## Starting geometry for a first *test* carrier

- Board **160 x 32 mm**, 1.6 mm thick, 4 layers, prototype assumption
  (must be reviewed for grip, case, port, cost and finger reach).
- Place eight covered copper electrodes as two columns by four rows
  along the long axis, **8 x 12 mm each**, rotate the local footprint to
  make electrode long axis consistent with the instrument geometry.
- Candidate pad centres in mm from a provisional board origin, not final:
  (62,10), (62,22), (88,10), (88,22), (114,10), (114,22),
  (140,10), (140,22). Distances between adjacent columns 12 mm and
  between successive groups 26 mm. Reconfigure if ergonomic tests fail.
- Electronics, SWD and USB-C at the 0..52 mm end. Two inherited 1x15
  debug headers are intentionally **not suited** to the compact Mini
  body and should be replaced by optional test pads or a removable debug
  board *before* final Mini layout. Keep the original schematic/electrical
  functions documented until their removal is checked.
- CCLGA-7L pressure sensor must face a sealed breath pressure chamber,
  with a tube/outlet and saliva/water barrier. Keep top vent/pressure
  inlet accessible and respect ST's no-stress/keepout recommendations.

## Layer / return / USB strategy

1. **L1 and regulator**: place L1 pad1 with white mark connected to +1V1
   and pad2 to VREG_LX, immediately against RP2354A pins 48/50.
   Copy Raspberry Pi hardware-guide Fig. 4 topology; avoid arbitrary
   routing of VREG_LX. Place C25 4.7uF output, C24 4.7uF input and C26
   AVDD filter in their correct local loops.
2. U4 AP2112K: new **C201 1uF from VBUS to GND** next to VIN and
   **C2 1uF from +3V3 to GND** next to VOUT. Netlist gate verifies both.
3. **USB-C**: align J1 connector with mechanical board edge, verify real
   protrusion, through-hole shield tabs and no masking of signal pads.
   Route D+/D- as a close coupled, short pair with reference ground.
   Add a suitable USB ESD protection device **before fabrication**.
4. Use an uninterrupted reference GND layer beneath MCU/USB area.
   Isolate finger-electrode sense nets from USB switching/SMPS and audio.
   Do not put a blanket solid ground plane immediately below touch
   electrodes without empirical sensitivity tuning.
5. Use short decoupling loops, via-in-pad only when assembly process
   supports it, and thermal/paste treatment of RP2354A exposed pad.
6. 2x6 audio connector remains unpopulated; 5V output available only
   after defining host USB current budget/protection.
7. Top copper finger pads must have solder mask, *not* paste, and their
   body-contact outline/finish require mechanical validation.
8. Validate ST pressure sensor pad1 placement and central metal lid pad7
   connection in pick-and-place, mask and stencil. No board openings
   or copper in conflict with the sensor's pressure passage.

## Verification gates before a PCBA order

- KiCad ERC with `--exit-code-violations` and critical netlist check:
  must both pass.
- KiCad PCB DRC with pad clearance/track/edge constraints for JLCPCB
  stackup; manually inspect USB-C cutout and mechanical footprints.
- Revalidate schematic C2/C201, L1, U3 and chosen USB ESD device.
- Verify exact supplier component codes and in-stock vs pre-order.
- Produce and review Gerber, drill, BOM and CPL; inspect pick/place
  rotation for polarized L1, U3 and USB-C.
- Confirm 3D physical case fit, pressure chamber and finger pad comfort.

## Primary sources

- RP2350 PCB placement guide, Figure 4:
  https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008280-DS-2-hardware-design-with-rp2350.pdf
- ST LPS28DFW datasheet:
  https://www.st.com/resource/en/datasheet/lps28dfw.pdf
- Diodes AP2112:
  https://www.diodes.com/assets/Datasheets/AP2112.pdf

**Status: pre-layout constraints. A routed `.kicad_pcb` does not yet exist.**
