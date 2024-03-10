from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#dépose bonhomme 1 janv

moteurg = Motor(Port.E, Direction.COUNTERCLOCKWISE)
moteurd = Motor(Port.F, Direction.CLOCKWISE)
bg = Motor(Port.C)
bd = Motor(Port.D)

robot = DriveBase(moteurg, moteurd, wheel_diameter = 56, axle_track=85)


robot.settings(700, 600, 600, 600)
#(vitesse max en mm/s)  
#accélération lorsqu'il commence à se déplacer et lorsqu'il s'arrête (mm/s²)
#taux de rotation maximal pour les commandes de virage °/s=vitesse du robot qd il tourne
#tx d'accélération de rotation °/s²+ vitesse qd le robot commence et finit de tourner


robot.use_gyro(True)
robot.straight(500)
robot.turn(-45)
robot.straight(200)
robot.turn(-40)
robot.straight(750)
robot.turn(90)
robot.straight(190)  #dépose
robot.straight(-350)
robot.turn(-45)
robot.straight(150)
robot.turn(-45)

