import time
from AngleMeterAlpha import AngleMeterAlpha
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servo = 11
GPIO.setup(servo, GPIO.OUT)
def Drive_servo(roll,pitch):
        
        if abs(pitch) < 60 and abs(pitch) != 0:
                pwm = GPIO.PWM (servo,50)
                pwm.start(7)
                DC = (abs((roll)*1.5)/18)+2
                pwm.ChangeDutyCycle(DC)
              
        else:
                pwm = GPIO.PWM (servo,50)
                pwm.start(7)
                pwm.stop() 
                
        time.sleep(0.05)

        

angleMeter = AngleMeterAlpha()
angleMeter.measure()
while True:
        
        print(angleMeter.get_kalman_roll()+19,",,",angleMeter.get_kalman_pitch()-6,".")
        Drive_servo(angleMeter.get_kalman_pitch()-6, angleMeter.get_kalman_roll()+19 )
        #print(angleMeter.get_int_roll(), angleMeter.get_int_pitch())
        time.sleep(0.3)

