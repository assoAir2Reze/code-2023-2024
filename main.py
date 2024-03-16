from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from urandom import randint


def prog1(nb, hub, robot, bg, bd):
 # 2024-03-16
 # 9 - Le code pour le BATEAU
 hub.display.number(nb)
 wait(WAIT_TIME)
 
 #J'y vais
 robot.straight(380)
 
 
 #Mission
 bd.run_target(400, 400)
 robot.turn(-60)
 robot.straight(-150)
 
 #Je rentre à la base
 bd.run_target(400, -300)
 robot.turn(-120)
 robot.straight(100)


def prog2(robot, bg, bd):
 # 2024-03-16
 # 10 - Le code pour la table de mixage
  
 #J'y vais 
 robot.turn(120)
 robot.straight(350)

 #Je réalise la mission
 #Todo


def prog3(robot, bg, bd):
 # 2024-03-16
 # 1 - Le code pour le cinema 3D

 #J'y vais
 robot.straight(250)
 
 #Je réalise la mission
 #Todo


def prog4(robot, bg, bd):
 # 2024-03-16
 # 2 - Changement de décor
 # 4 - Masterpiece
 # 5 - Fleur bleue 
 # 11 - Tour
 # 3 - Fleur violette
 
 #J'y vais
 robot.straight(80)
 robot.turn(-40)
 robot.straight(700)  

 #Je fais
 robot.turn(-90)
 robot.straight(100)
 robot.straight(-100)
 robot.turn(-90)
 robot.straight(300)

 #jy retourne a une autre mission
 robot.turn(90)
 robot.straight(100)

def prog5(robot, bg, bd):
 # 2024-03-16
 
 # Je place le robot, avec le module
 # Todo

 # Le robot va a la mission 6
  robot.turn(0)
 # Todo
 
 # Je fais la mission 6
 # Todo
 
 # Je fais la mission 7
 # Todo

 # Je reviens a la base
 # Todo

def prog6(robot, bg, bd):
 # 2024-03-16
 
 # Je place le robot
 # Todo

 # Il va a la mission 8
 robot.turn(0)
 # Todo

 # Il fait la mission 8
 # Todo
 
 # Il rentre a la base
 # Todo

def prog6(robot, bg, bd):
 # 2024-03-16
 
 # Je place le robot
 # Todo

 # Il va a la mission 8
 robot.turn(0)
 # Todo

 # Il fait la mission 8
 # Todo
 
 # Il rentre a la base
 # Todo

def prog7(robot, bg, bd):
 # 2024-03-16
 
 # Je place le robot
 # Todo

 # Le robot va aux missions 12 et 13
 robot.turn(0)
 # Todo

 # Il fait la mission 12
 # Todo

 # Il fait la mission 13
 # Todo

 # Il termine la mission 12
 # Todo

 # Il rentre à la base
 # Todo


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
        prog1(current_program, hub, robot, bg, bd)       
    
    elif current_program == 2:
        hub.display.number(2)
        wait(WAIT_TIME)
        prog2(robot, bg, bd)

    elif current_program == 3:
        hub.display.number(3)
        wait(WAIT_TIME)
        prog3(robot, bg, bd)
    
    elif current_program == 4:
        hub.display.number(4)
        wait(WAIT_TIME)
        prog4(robot, bg, bd)

    elif current_program == 5:
        hub.display.number(5)
        wait(WAIT_TIME)
        prog5(robot, bg, bd)

    elif current_program == 6:
        hub.display.number(6)
        wait(WAIT_TIME)
        prog6(robot, bg, bd)

    elif current_program == 7:
        hub.display.number(7)
        wait(WAIT_TIME)
        prog7(robot, bg, bd)