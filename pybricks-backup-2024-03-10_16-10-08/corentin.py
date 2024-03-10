from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import  Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task


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

#suivi noir blanc


# NOIR = 0
# BLANC = 100
# KP = 0.6
# VITESSE = 80

# objective=(NOIR+BLANC)/2
# direction=1
# moteurd.reset_angle()
# moteurg.reset_angle()
# angle=0

# while angle<360
#     error = objective - capteur.reflection()
#     kpe = KP* error
#     moteurd.run(VITESSE-(kpe*direction))
#     moteurd.run(VITESSE+(kpe*direction))
#     angle = moteurd.angle()
# bd.run_angle(-200,400)
# bg.run_angle(-200,400)

# debut scene

# robot.straight(420)
# robot.turn(-45)
# robot.straight(350)
# robot.turn(90)
# robot.straight(200)
# bd.run_angle(100,300)
# robot.straight(-70)
# bd.run_angle(100,-93)
# robot.straight(10)
# robot.turn(45)
# robot.straight(-200)
bg.run_angle(100,100)
# robot.turn(45)
# robot.straight(500)
# robot.turn(45)
# robot.straight(400)
# bg.run_angle(100,200)