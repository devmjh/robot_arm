# ~/projects/robot_arm/force_wide_sweep.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 15

# Step 1: Force the widest possible pulse range
# Standard is usually 750-2250. We go 500-2500 to 'unlock' the motor.
kit.servo[CLAW].set_pulse_width_range(500, 2500)

def test_full_range():
    print("Testing absolute 0 to 180 degree limits...")
    
    print("Commanding: 0 Degrees (Should be one extreme)")
    kit.servo[CLAW].angle = 0
    time.sleep(2)
    
    print("Commanding: 180 Degrees (Should be the other extreme)")
    kit.servo[CLAW].angle = 180
    time.sleep(2)
    
    print("Commanding: 90 Degrees (Center)")
    kit.servo[CLAW].angle = 90
    time.sleep(1)
    
    # Do NOT set to None yet, we want to see if it holds
    print("Test complete. Is the claw still in a new position?")

if __name__ == "__main__":
    test_full_range()
