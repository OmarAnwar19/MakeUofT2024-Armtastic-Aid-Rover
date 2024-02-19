from flask import Blueprint
import robot

arm = Blueprint('arm', __name__)

@arm.route('/rotateLeft', methods=['POST'])
def rotateLeft():
    if robot.Servo1.angle < 90:
        robot.setBase(robot.Servo1.angle + 50)
    print({'status': 'Rotating left'})

@arm.route('/rotateRight', methods=['POST'])
def rotateRight():
    if robot.Servo1.angle > -90:
        robot.setBase(robot.Servo1.angle - 50)
    return print({'status': 'Rotating right'})

@arm.route('/extendForward', methods=['POST'])
def extendForward():
    if robot.Servo1.angle < 80:
        robot.setZ(robot.Servo1.angle + 30)
    print({'status': 'Extending forward'})

# @arm.route('/extendBackward', methods=['POST'])
# def extendBackward():
#     if robot.Servo2.angle > 20:
#         robot.setZ(robot.Servo1.angle - 30)
#     print({'status': 'Extending backward'})

# @arm.route('/extendUpward', methods=['POST'])
# def extendUpward():
#     if robot.Servo3.angle < 90:
#         robot.setEffAng(robot.Servo3.angle + 50)
#     print({'status': 'Extending upward'})

@arm.route('/extendDownward', methods=['POST'])
def extendDownward():
    if robot.Servo3.angle > -50:
        robot.setEffAng(robot.Servo3.angle - 50)
    print({'status': 'Extending downward'})

@arm.route('/openClaw', methods=['POST'])
def openClaw():
    robot.setClaw(0)
    print({'status': 'Opening claw'})

@arm.route('/closeClaw', methods=['POST'])
def closeClaw():
    robot.setClaw(-90)
    print({'status': 'Closing claw'})


@arm.route('/pwmStop', methods=['POST'])
def PwmStop():
    robot.PwmStop()


def init():
    robot.setClaw(-90)
    robot.setEffAng(50)
    robot.setZ(0)