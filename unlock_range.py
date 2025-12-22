# ~/projects/robot_arm/unlock_range.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 1 

# SG90s usually need the full 500-2500 range to actually move 180 degrees
kit.servo[CLAW].set_pulse_width_range(500, 2500)

print("Starting at current 85% open spot...")
kit.servo[CLAW].angle = 150
time.sleep(2)

print("Moving toward CLOSED (Try 100)...")
kit.servo[CLAW].angle = 100
time.sleep(2)

print("Moving toward CLOSED (Try 50)...")
kit.servo[CLAW].angle = 50
time.sleep(2)

kit.servo[CLAW].angle = None
