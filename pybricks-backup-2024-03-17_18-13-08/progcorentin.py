from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()




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
bd.reset_angle
capteur = ColorSensor (Port.D)
backcapteur = ColorSensor (Port.C)

robot = DriveBase(moteurg, moteurd, wheel_diameter =88 , axle_track=98)
robot.settings(300, 200, 300, 300)

robot.use_gyro(True)
bd.run_until_stalled(-900, duty_limit=20)
wait(10)
bg.run_until_stalled(-900, duty_limit=20)
wait(10)
bd.reset_angle(0)
bg.reset_angle(0)
robot.straight(400)
robot.turn(45)
bd.run_target(400)

robot.straight(320)

bd.reset_angle(0)
bg.reset_angle(0)

robot.turn(45)
