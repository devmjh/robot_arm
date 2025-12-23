# arm_config.py
# Purpose: Central configuration for Robot Arm Pinout and Calibration
# Hardware: Nvidia Jetson / Raspberry Pi via PCA9685 Driver

from adafruit_servokit import ServoKit

# --- HARDWARE MAPPING ---
# Port 0: Reserved for Calibration (Empty)
# Port 15: Reserved (Empty)

# Active Ports
PIN_CLAW      = 1
PIN_BASE      = 11
PIN_SHOULDER  = 12
PIN_ELBOW     = 13
PIN_WRIST     = 14

# --- SERVO CALIBRATION ---
# Standard Analog Servos usually require 500-2500.
# Library default is 1000-2000 which causes "slight movement" or stiffness.
MIN_IMPULSE = 500
MAX_IMPULSE = 2500

# Initialize the Board
try:
    kit = ServoKit(channels=16)
except Exception as e:
    print(f"CRITICAL ERROR: PCA9685 Board not found. Check I2C connection. {e}")
    kit = None

def init_arm():
    """
    Applies the correct pulse width range to all active motors.
    Must be called at the start of every script.
    """
    if kit is None:
        return

    active_pins = [PIN_CLAW, PIN_BASE, PIN_SHOULDER, PIN_ELBOW, PIN_WRIST]
    
    print("--- Initializing Arm Configuration ---")
    for pin in active_pins:
        try:
            kit.servo[pin].set_pulse_width_range(MIN_IMPULSE, MAX_IMPULSE)
        except Exception as e:
            print(f"Error configuring Pin {pin}: {e}")
    print("--- Arm Configured (500-2500us) ---")

def get_kit():
    return kit
