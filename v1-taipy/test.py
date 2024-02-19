import robot
import time
import RPi.GPIO as GPIO
from piservo import Servo
#remember to run sudo pigpiod
#run alias python3=python3.9
#Claw servo closed is 60, open is 90
#note that doing servo.write() will make the servo try to move to the new position instantly, there is no speed control
#If implementing a continuous increase in angle, you need to somehow increment it with time

Servo1=Servo(12)

# claw: 60 close, 90 open

try:
    while True:
        Servo1.write(90)
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping")
    robot.PwmStop()
    robot.stop()
    #robot.ServoReset()
    GPIO.cleanup()