# ~/projects/robot_arm/engage.py
import time
from adafruit_servokit import ServoKit

# Initialize
kit = ServoKit(channels=16)

def engage():
    print("Forcing PWM signal to channels 0-3 at 50Hz...")
    for i in range(4):
        # Setting an initial angle should 'stiffen' the arm
        kit.servo[i].angle = 90
    print("Arm should now be rigid. Try to gently move a joint.")
    time.sleep(10)

if __name__ == "__main__":
    engage()
