from flask import Blueprint, jsonify
import robot
import RPi.GPIO as GPIO

mobility = Blueprint('mobility', __name__)

@mobility.route('/forward', methods=['POST'])
def forward():
    robot.forward()
    print({'status': 'Moving forward'})

@mobility.route('/backward', methods=['POST'])
def backward():
    robot.backward()
    print({'status': 'Moving backward'})

@mobility.route('/left', methods=['POST'])
def left():
    robot.left()
    print({'status': 'Turning left'})

@mobility.route('/right', methods=['POST'])
def right():
    robot.right()
    print({'status': 'Turning right'})

@mobility.route('/stop', methods=['POST'])
def stop():
    robot.stop()
    GPIO.cleanup()
    print({'status': 'Stopping'})