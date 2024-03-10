from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, 
from pybricks.parameters import Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#initialiser moteur
hub = PrimeHub()

#position : 1 er trait vers la gauche

moteurg = Motor(Port.E, Direction.COUNTERCLOCKWISE)
moteurd = Motor(Port.F, Direction.CLOCKWISE)
bg = Motor(Port.C)
bd = Motor(Port.D)

robot = DriveBase(moteurg, moteurd, wheel_diameter = 56, axle_track=85)


#initialise le sensor
sensor_gauche = ColorSensor(Port.B)
sensor_droite = ColorSensor(Port.A)

#parametres vitesse max 500
robot.settings(600, 500, 500, 250)

robot.use_gyro(True)

# bd.run_angle(600, 600)
bg.run_angle(600, 600)
bd.run_angle(600, -600)


# Arrêter le moteur
bg.stop()
bd.stop()