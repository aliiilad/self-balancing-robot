# Third-party material

This project is a learning build. Some of the material I work from is other
people's, and it is credited here. Nothing in this section is my own design.

## Reference hardware design — Robonyx

The KiCad projects (`SBR1`, `SBR2`, `SBR2.1`, `SBRcontroller`) and the Arduino
sketches under `Code/` that I use as a reference are the work of:

> **H.M. Phan — Robonyx**, 2024
> Schematic title blocks read `(company "Robonyx")`; sketch headers read
> `// H.M.Phan - Robonyx`.

**These files are deliberately *not* included in this repository.** They carry
no license granting redistribution, so republishing them here would not be mine
to do. They live in a `Self_Balancing_Robot/` folder on my machine, excluded via
[`.gitignore`](../../.gitignore).

I use them to understand how a working self-balancing robot is put together —
how the A4988 drivers are wired, how the ESP-NOW link between robot and
controller is structured, how the PID loop is organised. My own firmware goes in
[`firmware/`](../../firmware) and is written from scratch as I work through the
[roadmap](../25-day-roadmap.md).

If you want the reference design, get it from Robonyx directly rather than from
me.

## Board documentation — Espressif

The ESP32-S3-DevKitC-1 pinout, system block diagram, annotated board photo and
N16R8 schematic in this folder are Espressif's own board documentation,
reproduced here as a working reference:

- `esp32-s3-devkitc-1-pinout.jpg`
- `esp32-s3-devkitc-1-system-block.png`
- `esp32-s3-devkitc-1-annotated.png`
- `esp32-s3-n16r8-schematic.pdf`
- `esp32-s3-pin-definitions-annotated.jpg` — a Chinese-annotated pin definition
  sheet for the same board, from the vendor listing.

Canonical source: <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html>

## Libraries

The firmware depends on, but does not vendor, these open-source Arduino
libraries — each under its own license:

| Library | Used for |
|---|---|
| `Adafruit_BNO055` + `Adafruit_Sensor` | IMU orientation |
| `Adafruit_SSD1306` + `Adafruit_GFX` | OLED eyes |
