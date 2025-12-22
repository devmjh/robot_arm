import time
from adafruit_servokit import ServoKit

# --- CONFIGURATION ---
# The User's Actual Ports
CLAW = 1
BODY_SERVOS = [11, 12, 13, 14]

# Safe Center
CENTER = 90

# --- SETUP ---
kit = ServoKit(channels=16)

print("--- WAKING UP PORTS 1 and 11-14 ---")
print("Warning: The robot will stand up now.")
time.sleep(1)

# 1. Wake the Claw (Port 1)
print(f"Centering CLAW (Port {CLAW})...")
kit.servo[CLAW].set_pulse_width_range(500, 2500)
kit.servo[CLAW].angle = CENTER
time.sleep(0.5)

# 2. Wake the Body (Ports 11-14)
for port in BODY_SERVOS:
    print(f"Centering Motor on Port {port}...")
    kit.servo[port].set_pulse_width_range(500, 2500)
    kit.servo[port].angle = CENTER
    time.sleep(0.5)

print("--- All connected motors should be holding 90° ---")