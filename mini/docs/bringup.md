# V0.1 bring-up and acceptance tests

These tests apply **after** creating/reviewing a schematic and PCB.
No board or firmware has been validated yet.

## 1. Before first power

- [ ] Check RP2354A symbol, QFN-60 footprint, pin 1 orientation, exposed
      ground pad and the official power/reference design.
- [ ] Verify 12 MHz crystal and the **specified polarized regulator inductor**
      against the Raspberry Pi hardware-design BOM.
- [ ] Verify all 3V3/USB connections, CC resistors, ESD diode orientation,
      MPR121 electrodes and LPS28DFW package orientation.
- [ ] Check for shorts between GND, VBUS and 3V3.

## 2. Power-on

- [ ] Use a current-limited 5 V test supply or USB power meter initially.
- [ ] Measure VBUS and 3V3 with sensors idle and during simultaneous touches.
- [ ] Confirm MCU boot via SWD; retain BOOTSEL and RESET access.

## 3. USB

- [ ] Enumerates on Windows/Linux/macOS or a compatible tablet as a
      **class-compliant USB-MIDI device** (not a USB serial bridge).
- [ ] Stable connection over repeated disconnect/reconnect cycles.
- [ ] Measure/record peak USB current; do not assume host supplies speaker
      power without checking the allowed USB current budget.

## 4. Touch

- [ ] Read 8 electrodes independently.
- [ ] Verify all 8 can register held simultaneously.
- [ ] Measure touch/release latency, rapid note changes, wet/dry hands and
      crosstalk between adjacent electrodes.
- [ ] Establish initial baseline/calibration and thresholds.

## 5. Pressure

- [ ] Sensor responds on I2C and returns reasonable atmospheric baseline.
- [ ] Characterize breath pressure range, noise, update rate, start/stop
      thresholds, hysteresis and moisture isolation.
- [ ] Test mouthpiece and airflow with sensor held out of the wet air stream.

## 6. MIDI behavior

- [ ] Observe note numbers from fingering changes.
- [ ] Verify Note On, Note Off and optional CC2 with a MIDI monitor.
- [ ] No stuck note after sudden pressure loss, USB reset or rapid fingering.
- [ ] Record input-event-to-MIDI latency; **target for study** <15 ms,
      not a measured or guaranteed specification.

## 7. Optional audio — separate test milestone

- [ ] Confirm MCU PWM/PDM clock/DMA feasibility and synthesis CPU budget.
- [ ] Confirm filter, AC coupling, amp input/output and gain arrangement.
- [ ] Start at safe low gain and with a known rated speaker.
- [ ] Verify acceptable noise, switching artifacts and USB current budget.
