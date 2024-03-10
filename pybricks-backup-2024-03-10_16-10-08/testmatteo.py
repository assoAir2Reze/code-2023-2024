from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
from pybricks.tools import wait

hub = PrimeHub()

bg = Motor(Port.D, Direction.COUNTERCLOCKWISE)
bd = Motor(Port.C, Direction.CLOCKWISE)

# Lancer le mouvement du bras gauche, sans attendre qu'il se termine
bg.run_target(100, 500, then=Stop.HOLD, wait=False)

# Lancer immédiatement le mouvement du bras droit
bd.run_target(100, 500, then=Stop.HOLD, wait=True)

# Attendre que le bras gauche ait terminé
while not bg.control.done():
    wait(10)
