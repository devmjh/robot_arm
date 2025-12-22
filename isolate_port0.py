# ~/projects/robot_arm/isolate_port0.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# The active joints we want to relax
ARM_JOINTS = [11, 12, 13, 14, 15]
CLAW_TEST_PORT = 0

def isolate_and_test():
    print("Relaxing all arm joints (11-15)...")
    for port in ARM_JOINTS:
        kit.servo[port].angle = None
    
    print("System isolated. Testing Claw on Port 0...")
    # Apply the 'Deep Pulse' range to Port 0
    kit.servo[CLAW_TEST_PORT].set_pulse_width_range(500, 2500)
    
    # Sweep Port 0
    targets = [10, 90, 170, 90]
    for angle in targets:
        print(f"Port 0 -> {angle} degrees")
        kit.servo[CLAW_TEST_PORT].angle = angle
        time.sleep(2)

if __name__ == "__main__":
    isolate_and_test()
