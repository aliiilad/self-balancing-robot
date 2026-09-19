# Engineering Log

**ESP32-S3 · BNO055 IMU · PID balance control · OLED eyes · BLE**
25-day build · daily documentation

> Rendered from [`Self_Balancing_Robot_Engineering_Log.docx`](../Self_Balancing_Robot_Engineering_Log.docx).
> The `.docx` is the working original — fill it in each day, then run `python3 tools/docx2md.py`
> to refresh this file. Only days with content are reproduced here.

## How to use this log

- **Fill in each day's page the same day you do the work.** Reconstructing failures later loses authenticity.
- **Prioritise the "What broke / failed" section.** Documented failure is more valuable than a clean success.
- **A 30-second entry is enough on a rough day.** The goal is consistency, not polish.

---

## Glossary

| Term | Meaning |
|---|---|
| GPIO | General Purpose Input/Output |
| PWM | Pulse Width Modulation |
| `digitalWrite()` | Binary on/off output in C++ / Arduino |
| I2C | 2-wire communication protocol — one wire for data (SDA), one for timing (SCL). One way to find the address of an I2C device is the I2C scanner sketch. |

---

## Day 1 — Inventory & Planning
**Goal:** Know every component and get the toolchain working.
**Date:** 16 Jul · **Time spent:** 3.5 h

**What I did**
Unpacked materials, connected the ESP32 to the Arduino IDE, downloaded the board printouts, and ran my first Blink program successfully.

**What broke / failed**
I didn't really understand how the ESP32 works. I tried to use the GPIO number for the LED to make it blink, but it only worked with the default `LED_BUILTIN` variable. I also couldn't make sense of the pinout of the ESP32 board.

**What I learned / how I fixed it**
The board connects to the Arduino IDE through two functions, `void setup()` and `void loop()`. Code for the board runs inside these two functions (mainly the loop). The GPIO number can be used to address pins on the board.

**Tomorrow**
Figure out why the LED didn't blink on GPIO 48, which is supposed to be the built-in LED — and try to code it myself. Understand how to use the ESP32 for my robot.

---

## Day 2 — Learn ESP32 Basics
**Goal:** Become comfortable programming the ESP32.
**Date:** 17 Jul · **Time spent:** 3 h

**What I did**
First time using GPIO to drive an external LED and run the Blink program. Also ran a dimming program and tried the Serial Monitor — this will later be used to check IMU angles in real time. Learned the `millis()` function, which is better than `delay()` and lets you check the time elapsed since the last action.

**What broke / failed**
- I didn't know how to connect the board to an external LED at first, since the board takes up almost the whole breadboard and there isn't enough space on the other side to reach GND.
- The Arduino IDE kept throwing an error saying the port was wrong, even though the correct port was connected and selected.

**What I learned / how I fixed it**
- There are GND pins on **both** sides of the board. Connecting GND to a negative rail on the side of the breadboard makes it much easier to reach the LED, with the anode going to a GPIO pin.
- I checked which ports were in use from the terminal with `cd /dev` then `ls /dev/cu.*`, then selected the correct port in the Arduino IDE.
- Every time I upload I have to hold the **BOOT** button, because this board doesn't automatically enter download/flash mode.

**Tomorrow**
Build a mini project using a button to control the LED on/off — `pinMode(pin, INPUT_PULLUP)`, `digitalRead(pin)`.

---

## Day 3 — OLED Screens
**Goal:** Display graphics on both OLEDs.
**Date:** 18 Jul · **Time spent:** 3 h

**What I did**
- First time wiring an OLED to the ESP32.
- Learned about the I2C scanner sketch.
- Got the Hello World example running.
- One eye blinking.
- Wired the second OLED.
- Both eyes blinking.

**What broke / failed**
Although two OLEDs are connected to the board, only **one** I2C address shows up — so the two OLEDs can't display separately. They're wired in parallel and share an address.

**What I learned / how I fixed it**
Because both displays answer to the same address, it's ambiguous which one is responding. The fix is to use the ESP32-S3's **second hardware I2C bus**: the S3 has two I2C peripherals, so I can wire the second OLED to a different pair of pins as bus 1. In software this means creating two `Wire` objects instead of one.

**Tomorrow**
Get both OLEDs displaying independently.

---

## Day 4 — Motor Driver (Single Motor)
**Goal:** Spin one motor reliably.
**Date:** 19 Jul

*Entry not yet written.*

---

## Days 5–25

*Not yet started. See the [25-day roadmap](25-day-roadmap.md) for each day's goal and deliverable.*

---

## Entry template

Copy this block for each new day:

```markdown
## Day N — Title
**Goal:**
**Date:** · **Time spent:** h

**What I did**


**What broke / failed**   ← be specific, this is the good stuff


**What I learned / how I fixed it**


**Content captured** (photos / clips / notes worth filming)


**Tomorrow**

```
