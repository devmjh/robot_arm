# ~/projects/robot_arm/servo_check.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# Map common Adeept arm channels (adjust if yours are different)
servos = {
    0: "Base (Swivel)",
    1: "Shoulder (Lower)",
    2: "Elbow (Upper)",
    3: "Claw/Gripper",
    4: "Claw Rotation (if 5th exists)"
}

def check_servos():
    for channel, name in servos.items():
        print(f"\n--- Testing {name} on Channel {channel} ---")
        user_input = input("Press Enter to move 30 degrees, or 's' to skip: ")
        
        if user_input.lower() == 's':
            continue
            
        try:
            print(f"Moving {name} to 120...")
            kit.servo[channel].angle = 120
            time.sleep(1)
            print(f"Moving {name} to 60...")
            kit.servo[channel].angle = 60
            time.sleep(1)
            print(f"Centering {name} to 90...")
            kit.servo[channel].angle = 90
        except Exception as e:
            print(f"Error on {name}: {e}")

if __name__ == "__main__":
    check_servos()
