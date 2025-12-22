# ~/projects/robot_arm/claw_tune.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 15

def tune_claw():
    # Start at the center you just calibrated
    current_angle = 90
    print(f"Claw initialized at {current_angle}")
    
    while True:
        print("\nCommands: 'o' (open +10), 'c' (close -10), 's' (save & exit)")
        cmd = input("Enter command: ").lower()
        
        if cmd == 'o':
            current_angle += 10
        elif cmd == 'c':
            current_angle -= 10
        elif cmd == 's':
            print(f"Final Angle: {current_angle}")
            break
        else:
            continue
            
        # Safety clamp
        current_angle = max(0, min(180, current_angle))
        print(f"Moving to: {current_angle}")
        kit.servo[CLAW].angle = current_angle

if __name__ == "__main__":
    tune_claw()
