import time
from adafruit_servokit import ServoKit

# ================= CONFIGURATION =================
# 1. PORT MAPPING (Swap these if your joints are mixed up!)
CLAW_PORT     = 1
BASE_PORT     = 11
SHOULDER_PORT = 12
ELBOW_PORT    = 13
WRIST_PORT    = 14

# 2. CALIBRATION OFFSETS (Change these to fix your alignment!)
# Positive numbers add degrees, Negative numbers subtract.
# Start with 0, then tweak to 5, -5, etc. until straight.
BASE_OFFSET     = 0   
SHOULDER_OFFSET = 0   
ELBOW_OFFSET    = 0
WRIST_OFFSET    = 0

# 3. CLAW LIMITS (Your Calibrated Numbers)
CLAW_CLOSED = 120
CLAW_OPEN   = 20
# =================================================

kit = ServoKit(channels=16)

def move_servo(port, target_angle, offset=0):
    """Moves a servo safely, applying the offset."""
    # Add the calibration offset
    final_angle = target_angle + offset
    
    # Safety Check: Don't let it try to go below 0 or above 180
    final_angle = max(0, min(180, final_angle))
    
    kit.servo[port].angle = final_angle

def set_posture(base, shoulder, elbow, wrist, delay=1.0):
    """Moves the whole arm to a pose."""
    print(f"Moving to: B={base} S={shoulder} E={elbow} W={wrist}")
    move_servo(BASE_PORT,     base,     BASE_OFFSET)
    move_servo(SHOULDER_PORT, shoulder, SHOULDER_OFFSET)
    move_servo(ELBOW_PORT,    elbow,    ELBOW_OFFSET)
    move_servo(WRIST_PORT,    wrist,    WRIST_OFFSET)
    time.sleep(delay)

def set_claw(angle):
    print(f"Claw to {angle}")
    kit.servo[CLAW_PORT].angle = angle
    time.sleep(0.5)

# --- THE MAIN ROUTINE ---
print("--- Waking Up ---")
# Set Pulse Widths (Safety)
for p in [CLAW_PORT, BASE_PORT, SHOULDER_PORT, ELBOW_PORT, WRIST_PORT]:
    kit.servo[p].set_pulse_width_range(500, 2500)

try:
    # 1. Home Position (Straight Up)
    print("1. Home Position")
    set_posture(90, 90, 90, 90)
    set_claw(CLAW_OPEN)

    # 2. Turn Left and Lean Down (The "Pick")
    print("2. Turning Left to Pick...")
    # Base=130 (Left), Shoulder=130 (Forward), Elbow=110 (Down), Wrist=60 (Level)
    set_posture(130, 130, 110, 60) 
    
    # 3. Grab
    print("3. Grabbing...")
    set_claw(CLAW_CLOSED)
    
    # 4. Lift Up
    print("4. Lifting...")
    set_posture(130, 90, 90, 90)

    # 5. Rotate to Right (The "Carry")
    print("5. Moving to Right...")
    set_posture(50, 90, 90, 90) # Base=50 (Right)

    # 6. Lean Down (The "Place")
    print("6. Placing...")
    set_posture(50, 130, 110, 60)

    # 7. Drop
    print("7. Dropping...")
    set_claw(CLAW_OPEN)

    # 8. Return Home
    print("8. Returning Home")
    set_posture(90, 90, 90, 90)
    set_claw(CLAW_CLOSED)

    print("--- Demo Complete ---")

except KeyboardInterrupt:
    print("\nStopping safely...")
    # Optional: Relax motors? 
    # kit.servo[1].angle = None