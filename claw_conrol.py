# ~/projects/robot_arm/claw_control.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 15

# Set the wider pulse range to ensure we get full movement
kit.servo[CLAW].set_pulse_width_range(500, 2500)

def control():
    print("Claw Control Active. The arm should now be STIFF.")
    print("Commands: 'o' = Open (10), 'c' = Close (130), 'q' = Quit")
    
    while True:
        cmd = input("Enter Command: ").lower()
        if cmd == 'o':
            print("Opening...")
            kit.servo[CLAW].angle = 10
        elif cmd == 'c':
            print("Closing...")
            kit.servo[CLAW].angle = 130
        elif cmd == 'q':
            # This makes it go limp again for safety
            kit.servo[CLAW].angle = None
            break

if __name__ == "__main__":
    control()
