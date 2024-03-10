

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialisation du hub et des moteurs
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)

# Configuration de DriveBase
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=85)

# Faire avancer le robot à 100 mm/s tout en tournant à 10 degrés/s
robot.drive(100, 10)

# Continuer ce mouvement pendant la distance souhaitée (650 mm pour 65 cm)
robot.straight(650)

# Arrêter le robot après avoir parcouru la distance
robot.stop()