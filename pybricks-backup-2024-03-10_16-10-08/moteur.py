from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

moteurg = Motor(Port.E, Direction.COUNTERCLOCKWISE)
moteurd = Motor(Port.F, Direction.CLOCKWISE)

bg = Motor(Port.A, Direction.COUNTERCLOCKWISE)
bd = Motor(Port.B)

capteur = ColorSensor (Port.D)
backcapteur = ColorSensor (Port.C)

robot = DriveBase(moteurg, moteurd, wheel_diameter =88 , axle_track=98)
robot.settings(300, 200, 300, 300)
robot.use_gyro(True)

#Je définie le reset des bras

bg.reset_angle(0)
bd.reset_angle(0)



# Le code , pur et dur


# bd.run_angle(400, -200)
# robot.straight(280)
# bd.run_angle(200, 300)
# robot.straight(-100)
# robot.turn(-45)
# bd.run_angle(400, -200)
# robot.straight(-200)



# Cinéma 3D

# robot.straight(100)
# robot.turn(-20)
# robot.straight(100)
# bg.run_angle(400, 100)
# robot.turn(20)

# bg.run_angle(600, -300)
# robot.straight(-200)


# bg.run_angle(300, -75)
# robot.straight(280)
# bg.run_angle(400, 200)
# robot.turn(50)
# wait(200)
# robot.turn(-30)
# bg.run_angle(400, -200)
# robot.straight(-200)

# robot.straight(360)
# robot.turn(-30)
# robot.turn(60)




# table de mixage


