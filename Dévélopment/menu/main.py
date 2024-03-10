from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Side, Icon
from pybricks.tools import wait

from urandom import randint

PROGRAM_TOTAL = 3
WAIT_TIME = 1000

current_program = 0

# Initialize the hub.
hub = PrimeHub()
hub.display.orientation(up=Side.TOP)


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
        hub.display.number(1)
        wait(WAIT_TIME)

    elif current_program == 2:
        hub.display.number(2)
        wait(WAIT_TIME)

    elif current_program == 3:
        hub.display.number(3)
        wait(WAIT_TIME)