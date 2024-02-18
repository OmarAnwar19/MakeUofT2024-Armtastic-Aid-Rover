import RPi.GPIO as GPIO
import time
from piservo import Servo

GPIO.setmode(GPIO.BCM)

ENA = 2 # Enable A
ENB = 3 # Enable B
IN1 = 5 # Input 1
IN2 = 6 # Input 2
IN3 = 13 # Input 3
IN4 = 19 # Input 4

#SRV1 = 12 #Base servo
SRV2 = 16 #Z axis servo
SRV3 = 20 #Wrist servo
SRV4 = 21 #End effector servo

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
#GPIO.setup(SRV1, GPIO.OUT)
GPIO.setup(SRV2, GPIO.OUT)
GPIO.setup(SRV3, GPIO.OUT)
GPIO.setup(SRV4, GPIO.OUT)

pwmA = GPIO.PWM(ENA, 100)
pwmB = GPIO.PWM(ENB, 100)
#Servo1=Servo(SRV1) #Base
#Servo2=Servo(SRV2) #Z
#Servo3=Servo(SRV3) #Effector angle
#Servo4=Servo(SRV4) #Claw
ServoAng=[90, 90, 90, 0]

# 50% Cycle
pwmA.start(50)
pwmB.start(50)

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

def SetAngle(angle, SRV, srvpwm):
    duty = angle / 18 + 2
    GPIO.output(SRV, True)
    srvpwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SRV, False)
    srvpwm.ChangeDutyCycle(0)

def PwmStop():
    pwmA.stop()
    pwmB.stop()
    
def ServoReset():
    Servo1.write(90)
    Servo2.write(90)
    Servo3.write(90)
    Servo4.write(0)
    Servo1.stop()
    Servo2.stop()
    Servo3.stop()
    Servo4.stop()