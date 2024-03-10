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



# 40
# tourne 25 droite 
# 15

robot.turn(10)
robot.straight(650)

robot.turn(-30)
robot.turn(75*2)
robot.straight(-300)

# # début de la partie de Matteo

robot.straight(80)
robot.turn(-40)
robot.straight(700)  # on vas metre MASTERPIECE
robot.turn(-115)
robot.straight(200)
robot.straight(-100)
robot.turn(75)
robot.straight(25)


bd.run_angle(300, -200)
robot.turn(-10)
bd.run_angle(400, 700)
robot.turn(50)

robot.turn(120*2)
robot.straight(400)
 