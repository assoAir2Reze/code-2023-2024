from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, 
from pybricks.parameters import Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task


hub = PrimeHub()

#ne pas effacer

moteurg = Motor(Port.E, Direction.COUNTERCLOCKWISE)
moteurd = Motor(Port.F, Direction.CLOCKWISE)
bg = Motor(Port.A, Direction.COUNTERCLOCKWISE)
bd = Motor(Port.B)
capteur = ColorSensor (Port.D)
backcapteur = ColorSensor (Port.C)

robot = DriveBase(moteurg, moteurd, wheel_diameter =88 , axle_track=98)

#parametres vitesse
robot.settings(950, 750, 750, 750)

bg.run_target(300,200)


def Noirg_blcdroite ():
    NOIR=100
    BLANC=0
    KP=0.6
    VITESSE=80
    objective = (NOIR + BLANC) / 2
    direction = 1
    moteurd.reset_angle()
    moteurg.reset_angle()
    angle = 0
    
    while angle < 360:
        error = objective - capteur.reflection()
        kpe = KP * error
        moteurd.run(VITESSE - (kpe * direction))
        moteurg.run(VITESSE + (kpe * direction))
        angle = moteurd.angle()
    # Print the values.
    print(angle)


while angle < 360:
    error = objective - capteur.reflection()
    kpe = KP * error
    moteurd.run(VITESSE - (kpe * direction))
    moteurg.run(VITESSE + (kpe * direction))
    angle = moteurd.angle()

robot.straight(400)