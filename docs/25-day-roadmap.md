# 25-Day Build Roadmap

**ESP32-S3 · IMU + PID balancing · OLED eyes · Bluetooth control**

> Rendered from [`Self_Balancing_Robot_25_Day_Roadmap.docx`](../Self_Balancing_Robot_25_Day_Roadmap.docx).
> The `.docx` is the working original; regenerate this file with `python3 tools/docx2md.py`.

---

## Overview & schedule notes

This roadmap includes two dedicated buffer days (Day 6 and Day 15) to absorb the inevitable slippage in a hardware project like this — particularly around Days 11–14, the balancing and PID-tuning phase, which is the highest-risk and least predictable part of the build. Chassis 3D printing starts early (Day 1) and runs in the background so it isn't a bottleneck on Day 9.

If the schedule falls behind after Day 15, cut features in this order: **Day 17 (wiring cleanup) first, then Day 18 (OLED personality).** Both are cosmetic and can be shortened or skipped without affecting whether the robot actually balances, moves, and takes commands.

## Milestones

| Days | Goal |
|---|---|
| 1–5 | ESP32 basics, OLED, motor control (chassis printing in background) |
| 6 | **Buffer Day #1** — catch-up / chassis finishing |
| 7–9 | IMU, power, final assembly |
| 10 | PID theory (no coding) |
| 11–14 | First balance attempt → tuning → stable balance |
| 15 | **Buffer Day #2** — reserved for balance overrun |
| 16 | Robustness (recovery, noise, oscillation) |
| 17–18 | Wiring cleanup + OLED personality (cut first if behind) |
| 19 | Motion while balancing |
| 20–22 | Bluetooth control + full integration |
| 23 | Polish |
| 24 | Testing + filming |
| 25 | Edit + publish |

---

## Daily plan

### Day 1 — Inventory & Planning
**Goal:** Know every component and get the toolchain working.

- Unbox everything and label every component.
- Find datasheets and read pinouts.
- Sketch a wiring diagram.
- Install Arduino IDE or PlatformIO.
- Install the ESP32 board package.
- Test uploading "Blink".
- Kick off 3D printing of the first chassis part (base or legs) so it runs in the background over the next few days.

**Deliverable:** ESP32 successfully programmed; first print job running.

### Day 2 — Learn ESP32 Basics
**Goal:** Become comfortable programming the ESP32.

- GPIO output, PWM, Serial Monitor.
- Functions, variables, timing (`millis()`).
- Mini projects: blink LED, fade LED, print numbers.

**Deliverable:** Comfortable writing and uploading simple ESP32 sketches.

### Day 3 — OLED Screens
**Goal:** Display graphics on both OLEDs.

- Learn I2C, SDA, SCL.
- Learn the Adafruit SSD1306 library.
- Build: Hello World → static eyes → blink animation.
- Queue the next chassis part to print overnight.

**Deliverable:** Both OLEDs display independently.

### Day 4 — Motor Driver (Single Motor)
**Goal:** Spin one motor reliably.

- Learn H-bridge, PWM, and direction pins.
- Forward, backward, variable speed, stop.

**Deliverable:** One motor spins smoothly and predictably.

### Day 5 — Both Motors
**Goal:** Coordinate both motors together.

- Drive forward and backward.
- Turn left and turn right.
- Change speed on the fly.

**Deliverable:** Both motors behave correctly and in sync.

### Day 6 — Buffer Day #1 (Catch-up)
**Goal:** Absorb any slippage from Days 1–5 before moving into IMU and assembly work.

- Finish any incomplete task from Days 1–5.
- Check on / finish 3D prints; test-fit parts against motors and battery.
- Refine the wiring diagram before committing to permanent wiring.
- If on schedule instead: get ahead by starting to read BNO055 documentation.

> This day has no fixed content by design — it exists to protect the rest of the schedule. Use it; don't skip ahead just because you can.

**Deliverable:** Fully caught up — all Day 1–5 goals solid, chassis parts test-fitted.

### Day 7 — IMU
**Goal:** Understand the BNO055.

- Read pitch, roll, and yaw.
- Move the sensor around by hand and watch the values respond.
- Print values to Serial.

**Deliverable:** Reliable, sensible angle readings.

### Day 8 — Battery & Power
**Goal:** Get the full electrical system running safely.

- Wire battery → switch → buck converter → ESP32 + driver.
- Measure the 5 V rail and battery voltage.
- Check current flow is sane under load.

**Deliverable:** Entire system powers correctly and safely.

### Day 9 — Final Chassis Assembly
**Goal:** Physically assemble the robot.

- All chassis parts should already be printed (from Days 1–6) — this day is assembly only, not printing.
- Mount motors, battery, ESP32, driver, and OLEDs.

**Deliverable:** Robot physically assembled. No balancing yet.

### Day 10 — Understand PID (No coding)
**Goal:** Know *why* PID works before writing a line of tuning code.

- Understand error, P, I, D, overshoot, and oscillation.
- Watch 3Blue1Brown and Brian Douglas.
- Read worked examples.

**Deliverable:** Solid conceptual understanding of PID control, ready to implement it tomorrow.

### Day 11 — First PID Attempt
**Goal:** Get the robot attempting to stand.

- Strip the problem down to angle only.
- Forget encoders, forget Bluetooth, forget OLED logic in the loop.
- Let the robot try to balance — expect failure. That's the baseline.

**Deliverable:** A working (if bad) PID loop and a first sense of how the robot behaves.

### Day 12 — PID Tuning, Day 1
**Goal:** Begin systematic tuning.

- Adjust Kp, Ki, Kd.
- Record every attempt — numbers and short video clips (these make great future content).

**Deliverable:** Documented tuning log with visible improvement over Day 11.

### Day 13 — PID Tuning, Day 2
**Goal:** Continue tuning toward a real balance.

- Keep adjusting Kp, Ki, Kd based on Day 12's log.
- Target: robot almost balances — 2–3 seconds counts as real progress.

**Deliverable:** Consistent 2–3 second balance attempts.

### Day 14 — Stable Balance
**Goal:** 10+ seconds of continuous balancing.

- Keep tuning until the robot holds itself up reliably.

> **Do not move on until this works.** This is the load-bearing milestone of the whole project — everything after it assumes balance is solved.

**Deliverable:** Robot balances for 10+ seconds.

### Day 15 — Buffer Day #2 (Reserved for balance overrun)
**Goal:** Protect the schedule if Day 14's target slipped.

- If Day 14's target isn't met yet: continue tuning, no new features today.
- If Day 14 succeeded: push the robot and test recovery, or get ahead on Day 16.

**Deliverable:** Reliable 10+ second balance, confirmed repeatable across multiple attempts.

### Day 16 — Robustness
**Goal:** Make the balance resilient, not just possible.

- Improve recovery behavior.
- Filter sensor noise.
- Reduce oscillation.
- Push the robot and check if/how it recovers.

**Deliverable:** Balance survives small disturbances, not just a static stand.

### Day 17 — Clean Wiring *(cut first if behind schedule)*
**Goal:** Make the build safe and camera-ready.

- Zip ties, heat shrink, cable management.
- Mount everything securely.

> Skippable without affecting core function — this is the first thing to cut if the schedule is under pressure.

**Deliverable:** Wiring is safe, tidy, and camera-ready.

### Day 18 — OLED Eyes / Personality *(cut second if behind schedule)*
**Goal:** Give the robot visual character.

- Expressions: happy, blink, sleeping, surprised.
- Moving / animated eyes.

> Nice-to-have, not core — the second thing to cut if the schedule is under pressure.

**Deliverable:** Robot has visual personality via the OLEDs.

### Day 19 — Motion While Balancing
**Goal:** Move the robot without it falling over.

- Add forward and backward motion.
- Add rotation.
- All while actively balancing.

**Deliverable:** Robot can move under balance control.

### Day 20 — Bluetooth Basics
**Goal:** Get phone-to-robot communication working.

- Learn ESP32 Bluetooth (Classic SPP or BLE).
- Send forward / backward / stop commands from a phone.

**Deliverable:** Phone can send basic commands the ESP32 receives correctly.

### Day 21 — Bluetooth UI
**Goal:** Build a usable control interface.

- Build phone-side buttons or a joystick control (e.g. a Bluetooth terminal app or simple custom app).

**Deliverable:** Usable phone control interface.

### Day 22 — Full Integration
**Goal:** Bring every subsystem together.

- Combine balance + motion + Bluetooth commands into one system.

**Deliverable:** Robot balances, moves, and responds to phone input simultaneously.

### Day 23 — Polish
**Goal:** Make everything reliable, not just functional once.

- Fix bugs, loose wiring, rough code, mounting issues, animation timing.

**Deliverable:** Everything works reliably, repeatably.

### Day 24 — Testing + Filming
**Goal:** Stress-test the robot and capture all raw footage.

- Test on different floors, at different battery levels, under pushes, while turning, and over a long runtime — find weaknesses.
- Film: assembly shots, failure clips, successful balance, close-ups of OLEDs, Bluetooth control in action.
- Get all raw footage today so editing isn't blocked tomorrow.

**Deliverable:** Full raw footage library plus a known list of remaining issues.

### Day 25 — Edit & Publish
**Goal:** Turn footage into finished content and close out the project.

- Edit a long-form video (5–10 min) from Day 24 footage.
- Edit several short-form clips (30–60 s).
- Write up: what I learned, biggest mistakes, what surprised me, what I'd improve next.

> Tip: if you jot one line of reflection at the end of each day throughout the project (30 seconds, no extra day needed), this becomes assembly, not writing, on Day 25.

**Deliverable:** Published long-form video, published short-form clips, and a written reflection.
