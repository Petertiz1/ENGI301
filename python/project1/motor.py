import Adafruit_BBIO.GPIO as GPIO
import time

class StepperMotor():
    def __init__(self, step_pin, dir_pin, full_step=True):
        self.STEP_PIN = step_pin
        self.DIR_PIN = dir_pin
        self.FULL_STEP = full_step
        self.STEPS_PER_REVOLUTION = 2048 if self.FULL_STEP else 4096
        self._time2 = 0

        # Set up the GPIO pins
        GPIO.setup(self.STEP_PIN, GPIO.OUT)
        GPIO.setup(self.DIR_PIN, GPIO.OUT)

    def set_direction(self, direction):
        # Set the direction (1 for clockwise, 0 for counterclockwise)
        GPIO.output(self.DIR_PIN, direction)

    def rotate_motor(self, time_in):
        # Calculate the number of degrees to rotate per second
        degrees_per_second = 36
        degrees = degrees_per_second * time_in
        
        # Calculate the number of steps to rotate the specified number of degrees
        steps = int(degrees / 360 * self.STEPS_PER_REVOLUTION)
        
        # Calculate the delay for a 36-degree rotation per second
        delay = 1 / (degrees_per_second / 360 * self.STEPS_PER_REVOLUTION)
        
        # Perform the steps
        for i in range(steps):
            # Pulse the STEP pin to move the motor
            GPIO.output(self.STEP_PIN, 1)
            time.sleep(delay/2)  # Adjusted delay
            GPIO.output(self.STEP_PIN, 0)
            time.sleep(delay/2)  # Adjusted delay

if __name__ == '__main__':
    motor1 = StepperMotor("P2_6", "P2_4")
    #motor2 = StepperMotor("P2_10", "P2_8")
    motor1.set_direction(1)  # Set direction to clockwise
    #motor2.set_direction(1)
    motor1.rotate_motor(10)  # Rotate the motor time_in seconds clockwise
   # motor2.rotate_motor(36,10)
