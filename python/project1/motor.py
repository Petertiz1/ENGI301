import Adafruit_BBIO.GPIO as GPIO
import time

# Define the pins connected to the A4988 driver
STEP_PIN = "P2_06"
DIR_PIN = "P2_04"

# Set up the GPIO pins
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Set the direction (1 for clockwise, 0 for counterclockwise)
GPIO.output(DIR_PIN, 1)

# Set the stepping mode (1 for full step, 0 for half step)
FULL_STEP = 1

# Define the number of steps per revolution for the 28BYJ-48 motor
STEPS_PER_REVOLUTION = 2048 if FULL_STEP else 4096

def rotate_motor(degrees):
    # Calculate the number of steps to rotate the specified number of degrees
    steps = int(degrees / 360 * STEPS_PER_REVOLUTION)

    # Perform the steps
    for i in range(steps):
        # Pulse the STEP pin to move the motor
        GPIO.output(STEP_PIN, 1)
        time.sleep(0.001)  # Adjust this delay as needed
        GPIO.output(STEP_PIN, 0)
        time.sleep(0.001)  # Adjust this delay as needed

if __name__ == '__main__':
# Example usage: rotate the motor 90 degrees clockwise
    rotate_motor(90)
