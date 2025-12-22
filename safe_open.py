# ~/projects/robot_arm/safe_open.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 15

def safe_open():
    print("Commanding Claw to OPEN position (140)...")
    try:
        # Move to a likely open position
        kit.servo[CLAW].angle = 140
        time.sleep(1)
        
        # RELAX: This stops the buzzing/heating immediately
        print("Relaxing motor signal to prevent overheating...")
        kit.servo[CLAW].angle = None 
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    safe_open()
