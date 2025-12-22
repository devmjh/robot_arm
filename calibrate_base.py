# ~/projects/robot_arm/calibrate_base.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def test_base():
    print("Testing Base Rotation (Channel 0)...")
    # Move slowly to 45 degrees
    kit.servo[0].angle = 45
    time.sleep(1)
    # Move back to Center
    kit.servo[0].angle = 90
    print("Base Test Complete.")

if __name__ == "__main__":
    test_base()
