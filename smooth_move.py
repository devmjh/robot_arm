# ~/projects/robot_arm/smooth_move.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# Our verified mapping
BASE = 14
SHOULDER = 13
ELBOW = 12
WRIST = 11

def move_smooth(channel, target_angle, speed=0.02):
    """
    Moves a servo slowly to the target angle.
    speed: seconds to wait between each degree of movement.
    """
    # Note: We don't know current angle, so we start from a safe 'assumed' 90
    # In a pro setup, we'd track this in a variable.
    current_angle = 90 
    
    step = 1 if target_angle > current_angle else -1
    
    for angle in range(current_angle, target_angle + step, step):
        kit.servo[channel].angle = angle
        time.sleep(speed)

if __name__ == "__main__":
    print("Executing smooth base rotation...")
    move_smooth(BASE, 150)
    time.sleep(0.5)
    move_smooth(BASE, 30)
    time.sleep(0.5)
    move_smooth(BASE, 90)
