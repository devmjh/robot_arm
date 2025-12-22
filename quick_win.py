# ~/projects/robot_arm/quick_win.py
import time
from adafruit_servokit import ServoKit

# Initialize for 16 channels
try:
    kit = ServoKit(channels=16)
    print("PCA9685 Initialized. Moving Gripper...")
    
    # Sweep to prove life
    kit.servo[3].angle = 90
    time.sleep(1)
    kit.servo[3].angle = 140
    time.sleep(1)
    kit.servo[3].angle = 90
    
    print("Movement successful!")
except Exception as e:
    print(f"Failed to move: {e}")
