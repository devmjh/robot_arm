# ~/projects/robot_arm/force_snap.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 0 # Verify you are still on Port 0

# We are going to 'over-drive' the signal to force a reaction
kit.servo[CLAW].set_pulse_width_range(400, 2600)

print("Forcing OPEN... Watch the rocker arm.")
kit.servo[CLAW].angle = 10
time.sleep(2)

print("Forcing CLOSED...")
kit.servo[CLAW].angle = 170
time.sleep(2)

# Detach so it doesn't hum/heat up
kit.servo[CLAW].angle = None
