# ~/projects/robot_arm/real_open.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 15

def real_open():
    print("Commanding Claw to OPEN in the opposite direction (40)...")
    try:
        # If 140 closed it, 40 should open it.
        kit.servo[CLAW].angle = 40
        time.sleep(1)
        
        # Power down the signal so it stops fighting the plastic
        kit.servo[CLAW].angle = None 
        print("Signal detached. Is the claw open and quiet?")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    real_open()
