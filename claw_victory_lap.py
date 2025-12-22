# ~/projects/robot_arm/claw_victory_lap.py
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
CLAW = 0

# Set the wide range one last time for Port 0
kit.servo[CLAW].set_pulse_width_range(500, 2500)

def victory_lap():
    print("Moving to 90 (Center/Half-Open)...")
    kit.servo[CLAW].angle = 90
    time.sleep(1)
    
    print("Moving to 30 (Wide Open)...")
    kit.servo[CLAW].angle = 30
    time.sleep(1)
    
    print("Moving to 150 (Tight Closed)...")
    kit.servo[CLAW].angle = 150
    time.sleep(1)
    
    print("Returning to 90 and relaxing...")
    kit.servo[CLAW].angle = 90
    time.sleep(1)
    kit.servo[CLAW].angle = None

if __name__ == "__main__":
    victory_lap()
