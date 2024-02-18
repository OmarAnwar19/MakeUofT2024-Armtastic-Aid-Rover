from flask import Blueprint, jsonify
import robot_placeholder as robot

mobility = Blueprint('mobility', __name__)

@mobility.route('/forward', methods=['POST'])
def forward():
    robot.forward()
    return jsonify({'status': 'Moving forward'})

@mobility.route('/backward', methods=['POST'])
def backward():
    robot.backward()
    return jsonify({'status': 'Moving backward'})

@mobility.route('/left', methods=['POST'])
def left():
    robot.left()
    return jsonify({'status': 'Turning left'})

@mobility.route('/right', methods=['POST'])
def right():
    robot.right()
    return jsonify({'status': 'Turning right'})

@mobility.route('/stop', methods=['POST'])
def stop():
    robot.stop()
    GPIO.cleanup()
    return jsonify({'status': 'Stopping'})