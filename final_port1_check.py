# ~/projects/robot_arm/final_port1_check.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 1 

# Set the standard range
kit.servo[CLAW].set_pulse_width_range(500, 2500)

print("Testing Port 1 Claw... snapping to 40 (Open)")
kit.servo[CLAW].angle = 40
time.sleep(2)

print("Snapping to 140 (Closed)")
kit.servo[CLAW].angle = 140
time.sleep(2)

# Keep it at 90 for a final look
kit.servo[CLAW].angle = 90
