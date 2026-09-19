# Firmware

My own ESP32-S3 sketches, written as I work through the
[25-day roadmap](../docs/25-day-roadmap.md).

This folder is mostly empty right now — I'm on Day 4. Each sketch lands here as
it starts working, rather than all at the end, so the history shows the order I
actually learned things in.

## Board / toolchain

| | |
|---|---|
| Board | ESP32-S3-DevKitC-1 (N16R8) |
| IDE | Arduino IDE, ESP32 board package |
| Port | find it with `ls /dev/cu.*` |
| Upload | hold **BOOT** while uploading — this board doesn't auto-enter flash mode |

## Planned layout

```
firmware/
  01-blink/            Day 1  — toolchain check
  02-gpio-basics/      Day 2  — external LED, PWM fade, millis()
  03-oled-eyes/        Day 3  — dual SSD1306 on two I2C buses
  04-motor-single/     Day 4  — one stepper, A4988
  05-motor-both/       Day 5  — coordinated drive
  07-imu/              Day 7  — BNO055 pitch/roll/yaw
  11-pid-balance/      Day 11 — first balance attempt
  ...
```

## Hardware

| Part | Notes |
|---|---|
| ESP32-S3-DevKitC-1 N16R8 | main controller |
| BNO055 | 9-DOF IMU, I2C `0x28` |
| A4988 ×2 | stepper drivers |
| SSD1306 ×2 | OLED eyes — **need separate I2C buses**, they share address `0x3C` |
| LM2596 | buck converter, battery → 5 V rail |

See [`docs/reference/`](../docs/reference) for board pinouts.
