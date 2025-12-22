import sys
import time
from adafruit_servokit import ServoKit

# CONFIGURATION
CLAW_PORT = 1
CLOSED_ANGLE = 120  # 0%
OPEN_ANGLE = 40     # 100%

# INITIAL SETUP
kit = ServoKit(channels=16)
kit.servo[CLAW_PORT].set_pulse_width_range(500, 2500)

def set_claw(percent):
    # Clamp input to 0-100
    percent = max(0, min(100, percent))
    
    # Calculate angle: Linear map from [0, 100] to [140, 40]
    # Note: 0% is 140 (High angle), 100% is 40 (Low angle)
    angle = CLOSED_ANGLE - (percent * (CLOSED_ANGLE - OPEN_ANGLE) / 100.0)
    
    print(f"Claw at {percent}% (Angle: {int(angle)})")
    kit.servo[CLAW_PORT].angle = angle
    time.sleep(0.5)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = float(sys.argv[1])
        set_claw(user_input)
    else:
        print("Usage: python3 claw.py [0-100]")
        print("Example: python3 claw.py 50  <-- Half open")
