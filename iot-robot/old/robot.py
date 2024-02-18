import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import gpiozero

gpiozero.Device.pin_factory = PiGPIOFactory('127.0.0.1')
#remember to run sudo pigpiod


GPIO.setmode(GPIO.BCM)

#Note pin numberings are in BCM mode
ENA = 2 # Enable A Orange
ENB = 3 # Enable B Grey
IN1 = 5 # Input 1 Yellow
IN2 = 6 # Input 2 Green
IN3 = 25 # Input 3 Blue
IN4 = 26 # Input 4 Purple

SRV1 = 20 #Base servo purple-blue
SRV2 = 23 #Z axis servo grey
SRV3 = 24 #Wrist servo
SRV4 = 21 #End effector servo Yellow
#Servo wiring is red to +5, orange to signal, brown to ground


GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
# GPIO.setup(SRV1, GPIO.OUT)
# GPIO.setup(SRV2, GPIO.OUT)
# GPIO.setup(SRV3, GPIO.OUT)
# GPIO.setup(SRV4, GPIO.OUT)

pwmA = GPIO.PWM(ENA, 100)
pwmB = GPIO.PWM(ENB, 100)
Servo1=AngularServo(SRV1, min_angle=-90, max_angle=90) #Base
Servo2=AngularServo(SRV2, min_angle=-90, max_angle=90) #Z
#Servo3=AngularServo(SRV3, min_angle=-90, max_angle=90) #Effector angle
Servo4=AngularServo(SRV4, min_angle=-90, max_angle=90) #Claw

# 50% Cycle
pwmA.start(50)
pwmB.start(50)

def setBase(ang): #Can go between 0 and 180
    Servo1.angle=ang
    time.sleep(0.5)

def setZ(ang): #ranges 20 (back) to 90
    Servo2.angle=ang
    time.sleep(0.5)

def setEffAng(ang): #Doesnt work
    Servo3.angle=ang
    time.sleep(0.5)

def setClaw(ang): #0 for close, -90 for open
    Servo4.angle=ang
    time.sleep(0.5)

def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def PwmStop():
    pwmA.stop()
    pwmB.stop()
    

def ServoReset():
    #Servo1.write(90)
    #Servo2.write(90)
    #Servo3.write(90)
    #Servo4.write(90)
    Servo1.stop()
    Servo2.stop()
    Servo3.stop()
    Servo4.stop()

# try:
#     while True:
#         # setClaw(-45)
#         # time.sleep(1)
#         setClaw(20)
#         time.sleep(1)
#         setClaw(45)
#         time.sleep(1)
#         setClaw(80)
#         time.sleep(1)
#         setClaw(45)
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("stopping")
#     PwmStop()
#     stop()
#     #ServoReset()
#     GPIO.cleanup()
    