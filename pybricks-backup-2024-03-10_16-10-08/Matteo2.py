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

'''
La partie de Séraphin:
-bateau
-La table de mixage
-Le cinéma 3D
'''

robot.straight(380)
bd.run_target(400, 400)
robot.turn(-60)
robot.straight(-150)
bd.run_target(400, -300)
robot.turn(-120)
robot.straight(100)

''' Table de Mixage '''


wait(500)

robot.turn(120)
robot.straight(250)








'''
La partie de Matteo
'''




robot.turn(10)
robot.straight(650)

robot.turn(-30)
robot.turn(75*2)
robot.straight(-300)

# début de la partie de Matteo

robot.straight(80)
robot.turn(-40)
robot.straight(700)  # on vas mettre MASTERPIECE


robot.turn(-90)
robot.straight(100)
robot.straight(-100)
robot.turn(-90)
robot.straight(300)

robot.turn(90)
robot.straight(100)

