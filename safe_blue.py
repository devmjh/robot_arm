# ~/projects/robot_arm/safe_blue.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 1 

# NARROW the range to prevent over-travel (1000 to 2000 is very safe)
kit.servo[CLAW].set_pulse_width_range(1000, 2000)

print("Moving to Center (90)...")
kit.servo[CLAW].angle = 90
time.sleep(1)

print("Moving to 60 (Should be safe Open)...")
kit.servo[CLAW].angle = 60
time.sleep(1)

print("Moving to 120 (Should be safe Closed)...")
kit.servo[CLAW].angle = 120
time.sleep(1)

kit.servo[CLAW].angle = None

