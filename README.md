# AI Lab Robot Arm Project

## Hardware Overview
- **Controller:** Raspberry Pi 5 / Jetson Orin Nano
- **Driver:** PCA9685 16-Channel PWM Driver (I2C Address 0x40)
- **Power:** External 5V/6A Supply for Servos

## Pin Mapping (Custom Configuration)
| Joint     | PCA9685 Port | Description |
|-----------|--------------|-------------|
| **N/A** | 0            | *Reserved for Calibration* |
| **Claw** | 1            | Gripper mechanism |
| **Base** | 11           | Main Swivel (Left/Right) |
| **Shoulder**| 12         | Lower Arm Lift |
| **Elbow** | 13           | Upper Arm Lift |
| **Wrist** | 14           | Rotation/Tilt |
| **N/A** | 15           | *Unused* |

## Usage
1. Activate Virtual Environment: `source .venv/bin/activate`
2. Run Setup verification: `python3 verify_setup.py`
