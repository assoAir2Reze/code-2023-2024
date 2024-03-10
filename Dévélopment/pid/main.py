from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

NOIR = 100
BLANC = 0

KP = 5
VITESSE= 25

moteurg = Motor(Port.E, Direction.COUNTERCLOCKWISE)
moteurd = Motor(Port.F, Direction.CLOCKWISE)

capteur = ColorSensor (Port.A)

objective = (NOIR + BLANC) / 2

while True:

    error = objective - capteur.reflection()

    kpe = KP * error

    moteurd.run(kpe - VITESSE)

    moteurg.run(kpe + VITESSE)
