from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from urandom import randint

#Nos fonctions
from prog1 import prog1
from prog2 import prog2
from prog3 import prog3
from prog4 import prog4
from prog5 import prog5
from prog6 import prog6
from prog7 import prog7



#Initialize the hub
hub = PrimeHub()
hub.display.orientation(up=Side.TOP)

moteurg = Motor(Port.E, Direction.COUNTERCLOCKWISE)
moteurd = Motor(Port.F, Direction.CLOCKWISE)
bg = Motor(Port.A, Direction.COUNTERCLOCKWISE)
bd = Motor(Port.B)
capteur = ColorSensor (Port.D)
backcapteur = ColorSensor (Port.C)

robot = DriveBase(moteurg, moteurd, wheel_diameter =88 , axle_track=98)

#parametres vitesse
robot.settings(950, 750, 750, 750)

PROGRAM_TOTAL = 7
WAIT_TIME = 1000

current_program = 1


while True:
    hub.display.icon(Icon.HAPPY)

    # Wait for any button to be pressed, and save the result.
    pressed = []

    do = True

    while do:
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
         do = False

        if Button.RIGHT in pressed:
         current_program += 1

        if current_program > PROGRAM_TOTAL:
         current_program = 1

        hub.display.number(current_program)
        wait(600)

    if current_program == 1:
        prog1(current_program, hub, robot, bg, bd)       
    
    elif current_program == 2:
        hub.display.number(2)
        wait(WAIT_TIME)
        prog2(hub, robot, bg, bd)

    elif current_program == 3:
        hub.display.number(3)
        wait(WAIT_TIME)
        prog3(hub, robot, bg, bd)
    
    elif current_program == 4:
        hub.display.number(4)
        wait(WAIT_TIME)
        prog4(hub, robot, bg, bd)

    elif current_program == 5:
        hub.display.number(5)
        wait(WAIT_TIME)
        prog5(hub, robot, bg, bd)

    elif current_program == 6:
        hub.display.number(6)
        wait(WAIT_TIME)
        prog6(hub, robot, bg, bd)

    elif current_program == 7:
        hub.display.number(7)
        wait(WAIT_TIME)
        prog7(hub, robot, bg, bd)