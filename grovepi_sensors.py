from grove_rgb_lcd import *
import grovepi


#port description
potentiometer_port = 0
grovepi.set_bus("RPI_1")
ultrasonic_port = 4
setText("")
rst_flag = 1
prev_pot_val = 0


try:

    while True:
        time.sleep(0.5)
        #get rotary value
        potentiometer_value = grovepi.analogRead(potentiometer_port)

        #get ultrasonic value
        ultrasonic_value = grovepi.ultrasonicRead(ultrasonic_port)
        

        if(ultrasonic_value > potentiometer_value):
            setRGB(0,255,0)
            
            '''
            due to the purely additive nature of setText_norefresh,
            when using setText_norefresh, a onetime reset for the screen when ultrasonic reading 
            goes from 3 digits to 1 digit is neccesary so as to avoid the behaviour shown below:
            'xxx cm'
            'x cm m'
            '''

            if(rst_flag or  (potentiometer_value == 0 and prev_pot_value != 0)):
                rst_flag = 0
                setText(f"{potentiometer_value}cm \n{ultrasonic_value}cm")
            else:
                setText_norefresh(f"{potentiometer_value}cm \n{ultrasonic_value}cm")
            
        else:
            setRGB(255,0,0)
            rst_flag = 1
            setText_norefresh(f"{potentiometer_value}cm OBJ PRES\n{ultrasonic_value}cm")
    
        prev_pot_value = potentiometer_value

except KeyboardInterrupt:
    setText("Keyboard\nInterrupt")
    setRGB(100,100,100)
