from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, 
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.tools import wait
from urandom import randint

#Nos library à nous
#from toto import prog1

    # 2024-03-16
    # 9 - Le code pour le BATEAU
def prog1(DriveBase: robot, Motor : bg, Motor: bd):
    robot.straight(380)
    bd.run_target(400, 400)
    robot.turn(-60)
    robot.straight(-150)
    bd.run_target(400, -300)
    robot.turn(-120)
    robot.straight(100)

'''
def prog2(DriveBase: robot, Motor : bg, Motor: bd):
 # 2024-03-16
 # 10 - Le code pour la table de mixage

  robot.turn(120)
  robot.straight(350)


def prog3(DriveBase: robot, Motor : bg, Motor: bd):
 # 2024-03-16
 # 1 - Le code pour le cinema 3D

 robot.straight(250)


def prog4(DriveBase: robot, Motor : bg, Motor: bd):
 # 2024-03-16
 # 2 - Changement de décor
 # 4 - Masterpiece
 # 5 - Fleur bleue 
 # 11 - Tour
 # 3 - Fleur violette
 
 robot.straight(80)
 robot.turn(-40)
 robot.straight(700)  

 robot.turn(-90)
 robot.straight(100)
 robot.straight(-100)
 robot.turn(-90)
 robot.straight(300)

 robot.turn(90)
 robot.straight(100)


#def prog5(DriveBase: robot, Motor : bg, Motor: bd):
 # 2024-03-16
 # 6  la scene P1
 # 7  la scene P2


#def prog6(DriveBase: robot, Motor : bg, Motor: bd):
 # 2024-03-16
 # 8 caméra sur rail


#def prog7(DriveBase: robot, Motor : bg, Motor: bd):
 # 2024-03-16
 # 12 imprimante
 # 13 poulet

'''

# Initialize the hub.
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

PROGRAM_TOTAL = 3
WAIT_TIME = 1000

current_program = 0


while True:
    hub.display.icon(Icon.HAPPY)

    # Wait for any button to be pressed, and save the result.
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        wait(10)

    if Button.LEFT in pressed:
        current_program -= 1 # current_program = current_program - 1

    elif Button.RIGHT in pressed:
        current_program += 1 # current_program = current_program + 1


    if current_program < 1:
        current_program = PROGRAM_TOTAL

    elif current_program > PROGRAM_TOTAL:
        current_program = 1


    if current_program == 1:
        prog1(robot, bg, bd)
        #hub.display.number(1)
        wait(WAIT_TIME)

    elif current_program == 2:
        prog2(robot, bg, bd)
        #hub.display.number(2)
        wait(WAIT_TIME)

    elif current_program == 3:
        prog3(robot, bg, bd)
        #hub.display.number(3)
        wait(WAIT_TIME)

