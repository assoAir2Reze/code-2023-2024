from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

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
robot.settings(600, 600, 600, 600)
#(vitesse max en mm/s)  
#accélération lorsqu'il commence à se déplacer et lorsqu'il s'arrête (mm/s²)
#taux de rotation maximal pour les commandes de virage °/s=vitesse du robot qd il tourne
#tx d'accélération de rotation °/s²+ vitesse qd le robot commence et finit de tourner
#conseil (200-300,100-200, 100-200, 100-200)

robot.use_gyro(True)

bg.reset_angle(0)
bd.reset_angle(0)

#presse et ramassage skate
robot.straight(250)
robot.turn(-90)
robot.straight(190)
bg.run_angle(500, -550)
bd.run_angle(500, 600)

robot.turn(39)
bg.run_angle(500, 542)
robot.straight(65)
bg.run_angle(500,-250)

robot.straight(170)

robot.straight(150)
robot.straight(-50)
bd.run_angle(500,-500)
robot.straight(-100)
bd.run_angle(500,500)
robot.turn(90)
robot.straight(240)
robot.turn(-25)
robot.straight(200)

#concert
#bd.run_angle(-500, 400)
#robot.turn(-10)

#bd.run_angle(500, 30) #barre droite concert
#robot.turn(-25)
#bd.run_angle(500,100)
#robot.straight(-100)
#robot.turn(-50)
#robot.straight(160)
#robot.turn(100)
#robot.straight(80)
#robot.turn(-45)
#robot.straight(150)

#fleur

bg.stop()

#dragon seraphin ok avec barre noire rose jaune. barre à 4cm
#robot.straight(327)
#robot.turn(-15)
#robot.turn(45)
#robot.turn(-30)
#robot.straight(-140)