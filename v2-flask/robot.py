import RPi.GPIO as GPIO
import time
from piservo import Servo

GPIO.setmode(GPIO.BCM)

#Note pin numberings are in BCM mode
ENA = 2 # Enable A Orange
ENB = 3 # Enable B Grey
IN1 = 5 # Input 1 Yellow
IN2 = 6 # Input 2 Green
IN3 = 25 # Input 3 Blue
IN4 = 26 # Input 4 Purple

SRV1 = 12 #Base servo purple-blue
SRV2 = 13 #Z axis servo grey
SRV3 = 18 #Wrist servo
SRV4 = 19 #End effector servo Yellow
#Servo wiring is red to +5, orange to signal, brown to ground


GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(SRV1, GPIO.OUT)
GPIO.setup(SRV2, GPIO.OUT)
GPIO.setup(SRV3, GPIO.OUT)
GPIO.setup(SRV4, GPIO.OUT)

pwmA = GPIO.PWM(ENA, 100)
pwmB = GPIO.PWM(ENB, 100)
Servo1=Servo(SRV1) #Base
Servo2=Servo(SRV2) #Z
Servo3=Servo(SRV3) #Effector angle
Servo4=Servo(SRV4) #Claw
ServoAng=[90, 90, 90, 90]

# 50% Cycle
pwmA.start(50)
pwmB.start(50)

def setBase(ang):
    Servo1.write(ang)

def setZ(ang):
    Servo2.write(ang)

def setEffAng(ang):
    Servo3.write(ang)

def setClaw(ang):
    Servo4.write(ang)

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
    Servo1.write(90)
    Servo2.write(90)
    Servo3.write(90)
    Servo4.write(90)
    Servo1.stop()
    Servo2.stop()
    Servo3.stop()
    Servo4.stop()
