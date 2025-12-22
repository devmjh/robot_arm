# ~/projects/robot_arm/victory_wave.py
import time
from adafruit_servokit import ServoKit

# Initialize the 16-channel driver
kit = ServoKit(channels=16)

# Your discovered port map
BASE = 14
SHOULDER = 13
ELBOW = 12
WRIST = 11

def wave():
    print("Initializing joints to center...")
    joints = [BASE, SHOULDER, ELBOW, WRIST]
    for j in joints:
        kit.servo[j].angle = 90
    time.sleep(1)

    print("Performing the Victory Wave...")
    for _ in range(3):
        # Move the Base (14) and Wrist (11) back and forth
        kit.servo[BASE].angle = 70
        kit.servo[WRIST].angle = 120
        time.sleep(0.5)
        
        kit.servo[BASE].angle = 110
        kit.servo[WRIST].angle = 60
        time.sleep(0.5)

    # Return to safety
    kit.servo[BASE].angle = 90
    kit.servo[WRIST].angle = 90
    print("Sequence complete!")

if __name__ == "__main__":
    wave()
