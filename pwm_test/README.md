# Pico WH PWM Test

A simple C++ demo for the Raspberry Pi Pico WH. The Pico receives a single character through USB serial and changes the PWM duty cycle on **GP15**.

## Files

- `pico_pwm.cpp` — Pico WH firmware.
- `CMakeLists.txt` — Pico SDK build configuration.
- `pico_sdk_import.cmake` — Pico SDK import file.

## Commands

| USB command | PWM duty cycle |
| --- | --- |
| `0` | 0% |
| `1` | 25% |
| `2` | 50% |
| `3` | 75% |

The PWM frequency is approximately **1 kHz**. The initial duty cycle is **50%**.

## How to Run

1. Open the project in VS Code with the Raspberry Pi Pico extension and select **Pico W** (also used for Pico WH).
2. Build the project and flash the generated `.uf2` file using **BOOTSEL**.
3. Connect the Pico WH to a computer or Raspberry Pi 4 via USB and open its USB serial port.
4. Send `0`, `1`, `2`, or `3` to change the PWM output.

Use an oscilloscope to check **GP15 (physical pin 20)** relative to a Pico **GND** pin.

**Note:** This is a basic PWM signal demo only; no motor driver or motor is connected. Actual PWM measurements should be recorded separately.
