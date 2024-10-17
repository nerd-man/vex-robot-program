# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Isaac Hales                                                  #
# 	Created:      10/12/2024, 6:27:21 PM                                       #
# 	Description:  Building a 6 motor drivetrain                                #
#   Version:      0.0.2                                                        #
#   Changelog:    Hopefully fixed rotation of drivetrain and added change      #
#                 in speed based on how far joysticks are pushed               #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Set up DriveTrain object
def createDriveTrain():
    # Creating Left Motors
    motor1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1)
    motor2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1)
    motor3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1)

    left_group = MotorGroup(motor1, motor2, motor3)

    # Creating Right Motors
    # Reverses direction that motors spin so it can drive forward
    motor4 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True)
    motor5 = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)
    motor6 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)

    right_group = MotorGroup(motor4, motor5, motor6)

    # Create the full drivetrain
    # robot has a 4:5 external gear ratio which is 0.8 in float form
    drive_train = DriveTrain(left_group, right_group, externalGearRatio=0.8)

    return drive_train

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")

# Create DriveTrain
drive_train = createDriveTrain()

# Create Controller
controller = Controller()

while True:

    # Loop Through the controller axis
    # if past certain threshold then moves robot
    # left joystick for forward and backward movement
    # right joystick for left and right turns
    
    # Axis 1 = right joystick left and right
    # Axis 2 = right joystick up and down
    # Axis 3 = left joystick up and down
    # Axis 4 = left joystick left and right

    drive_train.drive(FORWARD, controller.axis3.position(), VelocityUnits.PERCENT)
    drive_train.turn(RIGHT, controller.axis1.position(), VelocityUnits.PERCENT)