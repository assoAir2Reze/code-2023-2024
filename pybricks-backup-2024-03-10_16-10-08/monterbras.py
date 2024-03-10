from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
left_attach = Motor(Port.C)
right_attach = Motor(Port.D)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter = 56, axle_track=85)


#initialise le sensor
sensor_gauche = ColorSensor(Port.B)
sensor_droite = ColorSensor(Port.A)


drive_base.settings(600, 500, 500, 250)

drive_base.use_gyro(True)

#Modifier a chaque fois que le deuxiemme.
left_attach.run_angle(600, -50)
wait(500)

drive_base.straight(335)
wait(200)

drive_base.turn(-35)
wait(200)

drive_base.straight(50)

wait(100)
drive_base.turn(50)
