import time
import RPi.GPIO as GPIO 
from AngleMeterAlpha import AngleMeterAlpha

GPIO.setmode(GPIO.BOARD)
servopin=11
GPIO.setup(servopin,GPIO.OUT)
pwm=GPIO.PWM(servopin,50)

angleMeter = AngleMeterAlpha()
angleMeter.measure()

while True:
    roll=angleMeter.get_kalman_roll()
    pitch=angleMeter.get_int_pitch()
    #print(angleMeter.get_kalman_roll(),",", angleMeter.get_complementary_roll(), ",",angleMeter.get_kalman_pitch(),",", angleMeter.get_complementary_pitch(),".")
    if (abs(pitch)<=45):
        pwm.start(0)
        DC= ((1/18)*abs(roll))+2
        print(DC,roll,pitch)
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.08)

pwm.stop()
GPIO.cleanup()
