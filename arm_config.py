# ~/projects/robot_arm/arm_config.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# This is your official IO Map
ARM_CHANNELS = {
    'base': 14,
    'shoulder': 13,
    'elbow': 12,
    'wrist': 11,
    'claw': 15  # The suspect joint
}

def move_joint(joint_name, angle):
    channel = ARM_CHANNELS.get(joint_name)
    if channel is not None:
        print(f"Moving {joint_name} (Port {channel}) to {angle}")
        kit.servo[channel].angle = angle
    else:
        print(f"Joint {joint_name} not found in map.")

if __name__ == "__main__":
    # Test a sequence using names, not numbers
    move_joint('base', 45)
    time.sleep(1)
    move_joint('base', 90)
