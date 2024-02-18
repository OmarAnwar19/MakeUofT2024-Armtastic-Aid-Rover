from flask import Blueprint, jsonify
import robot_placeholder as robot

arm = Blueprint('arm', __name__)

@arm.route('/rotateLeft', methods=['POST'])
def rotateLeft():
    if robot.ServoAng[0] > -90:
        robot.setBase(robot.ServoAng[0] - 10)
    return jsonify({'status': 'Rotating left'})

@arm.route('/rotateRight', methods=['POST'])
def rotateRight():
    if robot.ServoAng[0] < 90:
        robot.setBase(robot.ServoAng[0] + 10)
    return jsonify({'status': 'Rotating right'})

@arm.route('/extendForward', methods=['POST'])
def extendForward():
    if robot.ServoAng[1] < 90:
        robot.setZ(robot.ServoAng[1] + 10)
    return jsonify({'status': 'Extending forward'})

@arm.route('/extendBackward', methods=['POST'])
def extendBackward():
    if robot.ServoAng[1] > -10:
        robot.setZ(robot.ServoAng[1] - 10)
    return jsonify({'status': 'Extending backward'})

@arm.route('/extendUpward', methods=['POST'])
def extendUpward():
    if robot.ServoAng[2] < 90:
        robot.setEffAng(robot.ServoAng[2] + 10)
    return jsonify({'status': 'Extending upward'})

@arm.route('/extendDownward', methods=['POST'])
def extendDownward():
    if robot.ServoAng[2] > -10:
        robot.setEffAng(robot.ServoAng[2] - 10)
    return jsonify({'status': 'Extending downward'})

@arm.route('/openClaw', methods=['POST'])
def openClaw():
    robot.setEffAng(-90)
    return jsonify({'status': 'Opening claw'})

@arm.route('/closeClaw', methods=['POST'])
def closeClaw():
    robot.setClaw(0)
    return jsonify({'status': 'Closing claw'})


@arm.route('/pwmStop', methods=['POST'])
def PwmStop():
    robot.PwmStop()
    GPIO.cleanup()
    return jsonify({'status': 'PWM stopped'})


def init():
    robot.setClaw(0)
    robot.setEffAng(50)
    robot.setZ(0)