# ~/projects/robot_arm/side_by_side.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def compare():
    print("Comparing Claw (Port 0) with Spare (Port 1)...")
    # Apply identical wide ranges to both
    for p in [0, 1]:
        kit.servo[p].set_pulse_width_range(500, 2500)
    
    print("Syncing both to 10 degrees...")
    kit.servo[0].angle = 10
    kit.servo[1].angle = 10
    time.sleep(2)
    
    print("Syncing both to 170 degrees...")
    kit.servo[0].angle = 170
    kit.servo[1].angle = 170
    time.sleep(2)

if __name__ == "__main__":
    compare()
