import time

import Adafruit_BBIO.GPIO as GPIO

# to be replaced by the SPI library
import button as BUTTON
import motor as MOTOR
import spi_screen as SPI_SCREEN


class Mech_split_flap_disp():
    
    reset_time = None
    button     = None  # for timer
    button2    = None  # for stopwatch
    display    = None
    motor1     = None
    motor2     = None

    def __init__(self, reset_time=1.5, 
                       button="P2_18",button2="P2_20", 
                       i2c_bus=1, i2c_address=0x70,
                       step_pin1="P2_6", dir_pin1="P2_4",
                       step_pin2="P2_10", dir_pin2="P2_8"):
                           
        """ Initialize variables and set up SPI display """

        self.reset_time = reset_time
        self.button     = BUTTON.Button(button)
        self.button2    = BUTTON.Button(button2)
        self.display    = SPI_SCREEN.SPI_Display()
        self.motor1     = MOTOR.StepperMotor(step_pin1, dir_pin1)
        self.motor2     = MOTOR.StepperMotor(step_pin2, dir_pin2)
        
        self._setup()
    
    # End def
    

# End class

    def _setup(self):
        """Setup the hardware components."""
        # Initialize Display

        print("Project setup()")
        self.display.blank()

    # End def
    
    def timer(self):
        # run the timer while the green button has not been pressed for 2 seconds
        print("timer starts")
        
        time.sleep(0.5)
        _time = 0
      
        self.display.text(["                   TIMER",
                           " ",
                           "Press:", 
                                 "   Green Button to set time",
                                 "   Black Button to start timer",
                                 "Long Press Black to exit"])
                                 
        loop = True
        button2_press_time = self.button2.wait_for_press()[0]
        
        if (button2_press_time > self.reset_time):
                loop = False
                
        while(loop):
        
            if (self.button.is_pressed()):
                _time = _time + 10
                self.display.text(["time set", str(_time)])
            elif (self.button2.is_pressed()):
                loop = False
            else:
                time.sleep(0.1)
              
            count = _time    
        while(_time):
            _time -= 1
            _realtime = count - _time
            mins, secs = divmod(_realtime, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # time.sleep(1)
            print(timer, end="\r")
            self.motor1.set_direction(1)  # Set direction to clockwise
            self.motor1.rotate_motor(1) # Rotate the first motor every second
            # if secs == 0:  # Rotate the second motor once every minute
            #     motor2.set_direction(1)  # Set direction to clockwise
            #     self.motor2.rotate_motor(36,1)  
            self.display.text(str(timer))
            if(self.button2.is_pressed()):
                break
            time.sleep(0.01)
            
        time.sleep(1)
        
    # End Def
   
    
    def stopwatch(self):
        print("stopwatch starts")
        time.sleep(0.5)
        _time2 = 0
        
        loop2 = True
        
        
        self.display.text(["            STOPWATCH",
                           " ",
                           "Press:", 
                                 " Green Button to start/stop",
                                 " Black Button to reset",
                                 " Long Press Black to exit"])
                                 
        button2_press_time = self.button2.wait_for_press()[0]
        if (button2_press_time > self.reset_time):
            loop2 = False  
        while(loop2):                       
            
            if (self.button.is_pressed()):
                loop3_1 = True
                while(loop3_1):
                    _time2 = _time2 + 1
                    mins2, secs2 = divmod(_time2, 60)
                    timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
                    print(timer2, end="\r")
                    # if secs2 == 0:  # Rotate the second motor once every minute
                    #     motor2.set_direction(1)  # Set direction to clockwise
                    #     self.motor2.rotate_motor(36,1)  
                    self.display.text(str(timer2))
                    self.motor1.set_direction(1)  # Set direction to clockwise
                    self.motor1.rotate_motor(1) # Rotate the first motor every second
                    var = 1
                    #time.sleep(0.5)
                    while(var):
                        var = var - 1
                        if (self.button.is_pressed()):
                            loop3_1 = False
                    #time.sleep(0.5)
                    
                    # if (self.button.is_pressed()):
                    #     #time.sleep(1)
                    #     self.display.text(str(timer2))
                    #     loop4 = True
                    #     while(loop4):
                    #         if (self.button.is_pressed()):
                    #             loop4 = False
            if (self.button2.is_pressed()):
                 
                _time2 = 0
                mins2, secs2 = divmod(_time2, 60)
                timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
                print(timer2, end="\r")
                self.display.text(str(timer2))
                time.sleep(0.1)
                loop2 = False 
                time.sleep(1)
                    
       
                
        
    # End Def
    
    def run(self):
        """Execute the main program."""
        button_press_time = 0.0  # Time button was pressed (in seconds)
        button2_press_time = 0.0
        
        print("Run Class")
        print("Welcome Message")
        self.display.text(["        Welcome to my", "  Timer/Stopwatch Program!"])
        time.sleep(2)
        
        while(1):
            print("In Run loop")
            # Wait for button press
            # button_press_time = self.button.wait_for_press()[0]
            # button2_press_time = self.button2.wait_for_press()[0]
            # Record time
    
            # My own code starts here
            
    
            print("SPI displays ")
            self.display.text(["                  HOME"
                                "  ",
                                "Press:",
                                "  Green Button for Timer",
                                "  Black Button for Stopwatch"])
          
            wait_forpress = True
            
            while(wait_forpress):
                
                if (self.button.is_pressed()):
                    # Run timer if green button is pressed
                    
                    wait_forpress = False
                    self.timer()
                    time.sleep(1.5)
           
                if (self.button2.is_pressed()):
                    # Run stopwatch if black button is pressed
                    wait_forpress = False
                    self.stopwatch()
    
                time.sleep(0.1)
           
        
            time.sleep(1)
    
            # Wait for button release
    
            # # Compare time to increment or reset people_count
            # if (button_press_time < self.reset_time):
            #     if people_count < HT16K33.HT16K33_MAX_VALUE:
            #         people_count = people_count + 1
            #     else:
            #         people_count = 0
            # else:
            #     people_count = 0
            # # Update the display
            # self.display.update(people_count)


    # End def


    def cleanup(self):
        """Cleanup the hardware components."""
        
        # Set Display to something unique to show program is complete
        self.display.text("        IDLE", fontsize=40)
        
        # Button does not need any cleanup code
        
    #End def

# End class


if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the mech_split_flap_disp
    mech_split_flap_disp = Mech_split_flap_disp()

    try:
       
        mech_split_flap_disp.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        mech_split_flap_disp.cleanup()

    print("Program Complete")