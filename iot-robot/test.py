import robot
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

try:
    while True:
        robot.forward()
        time.sleep(1)
except KeyboardInterrupt:
    print("stopping")
    robot.PwmStop()
    robot.stop()
    GPIO.cleanup()

