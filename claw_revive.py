# ~/projects/robot_arm/claw_revive.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

CLAW = 15

def revive_claw():
    print("Testing Claw on Port 15 with expanded pulse range...")
    try:
        # Standard is 750-2250, we'll try 500-2500 for a 'kickstart'
        kit.servo[CLAW].set_pulse_width_range(500, 2500)
        
        print("Commanding 10-degree increments. Listen for humming.")
        for angle in [90, 100, 110, 120, 110, 100, 90, 80, 70]:
            print(f"Target: {angle}")
            kit.servo[CLAW].angle = angle
            time.sleep(0.5)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    revive_claw()
