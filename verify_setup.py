# verify_setup.py
# Purpose: Test the new custom pin mapping defined in arm_config.py

import time
import arm_config

def test_joint(name, pin):
    print(f"\nTesting {name} on Pin {pin}...")
    kit = arm_config.get_kit()
    
    # Move to Center
    print(f"  -> Center (90)")
    kit.servo[pin].angle = 90
    time.sleep(1.0)
    
    # Gentle move one way
    print(f"  -> Move (110)")
    kit.servo[pin].angle = 110
    time.sleep(0.5)
    
    # Gentle move other way
    print(f"  -> Move (70)")
    kit.servo[pin].angle = 70
    time.sleep(0.5)
    
    # Return Center
    print(f"  -> Rest (90)")
    kit.servo[pin].angle = 90
    time.sleep(0.5)

def main():
    # 1. Apply the configuration (Pulse Widths)
    arm_config.init_arm()
    
    # 2. Test in the order you specified
    test_joint("CLAW", arm_config.PIN_CLAW)
    test_joint("BASE", arm_config.PIN_BASE)
    test_joint("SHOULDER", arm_config.PIN_SHOULDER)
    test_joint("ELBOW", arm_config.PIN_ELBOW)
    test_joint("WRIST", arm_config.PIN_WRIST)
    
    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    main()
EOFcat << 'EOF' > verify_setup.py
# verify_setup.py
# Purpose: Test the new custom pin mapping defined in arm_config.py

import time
import arm_config

def test_joint(name, pin):
    print(f"\nTesting {name} on Pin {pin}...")
    kit = arm_config.get_kit()
    
    # Move to Center
    print(f"  -> Center (90)")
    kit.servo[pin].angle = 90
    time.sleep(1.0)
    
    # Gentle move one way
    print(f"  -> Move (110)")
    kit.servo[pin].angle = 110
    time.sleep(0.5)
    
    # Gentle move other way
    print(f"  -> Move (70)")
    kit.servo[pin].angle = 70
    time.sleep(0.5)
    
    # Return Center
    print(f"  -> Rest (90)")
    kit.servo[pin].angle = 90
    time.sleep(0.5)

def main():
    # 1. Apply the configuration (Pulse Widths)
    arm_config.init_arm()
    
    # 2. Test in the order you specified
    test_joint("CLAW", arm_config.PIN_CLAW)
    test_joint("BASE", arm_config.PIN_BASE)
    test_joint("SHOULDER", arm_config.PIN_SHOULDER)
    test_joint("ELBOW", arm_config.PIN_ELBOW)
    test_joint("WRIST", arm_config.PIN_WRIST)
    
    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    main()
EOFcat << 'EOF' > verify_setup.py
# verify_setup.py
# Purpose: Test the new custom pin mapping defined in arm_config.py

import time
import arm_config

def test_joint(name, pin):
    print(f"\nTesting {name} on Pin {pin}...")
    kit = arm_config.get_kit()
    
    # Move to Center
    print(f"  -> Center (90)")
    kit.servo[pin].angle = 90
    time.sleep(1.0)
    
    # Gentle move one way
    print(f"  -> Move (110)")
    kit.servo[pin].angle = 110
    time.sleep(0.5)
    
    # Gentle move other way
    print(f"  -> Move (70)")
    kit.servo[pin].angle = 70
    time.sleep(0.5)
    
    # Return Center
    print(f"  -> Rest (90)")
    kit.servo[pin].angle = 90
    time.sleep(0.5)

def main():
    # 1. Apply the configuration (Pulse Widths)
    arm_config.init_arm()
    
    # 2. Test in the order you specified
    test_joint("CLAW", arm_config.PIN_CLAW)
    test_joint("BASE", arm_config.PIN_BASE)
    test_joint("SHOULDER", arm_config.PIN_SHOULDER)
    test_joint("ELBOW", arm_config.PIN_ELBOW)
    test_joint("WRIST", arm_config.PIN_WRIST)
    
    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    main()
