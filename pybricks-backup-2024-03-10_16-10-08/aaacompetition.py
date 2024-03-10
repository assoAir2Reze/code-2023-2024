from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor,ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch,multitask, run_task

hub = PrimeHub()

#position : test code  4 fev

moterug = Motor(Port.E, Direction.COUNTERCLOCKWISE)
moteurd = Motor(Port.F, Direction.CLOCKWISE)
bg = Motor(Port.D, Direction.COUNTERCLOCKWISE)
bd = Motor(Port.C)
bouton = ForceSensor(Port.B)  # Bouton connecté au port B
# bras vers le bas =- (avant =-)

robot = DriveBase(moteurg, moteurd, wheel_diameter = 56, axle_track=85)

#parametres vitesse 
robot.settings(950, 750, 750, 750)
#straight speed en mm/s  
#straight acceleration (mm/s²)
#turn rate °/s=taux rotation du robot qd il tourne
#turn acceleration °/s² 

robot.use_gyro(True)#gyro utilisé

# Fonction pour attendre que le bouton soit pressé
def attendre_bouton():
    while not bouton.pressed():
        wait(10)

# Coroutine pour replier les bras et les réinitialiser
async def replier_bras():
    await bg.run_until_stalled(950, duty_limit=50)
    await bd.run_until_stalled(950, duty_limit=50)
    bg.reset_angle(0)
    bd.reset_angle(0)

# Coroutine pour attraper l'objet avec le bras gauche
async def expert():
    await bg.run_target(600, -540, then=Stop.HOLD, wait=True)

# Coroutine principale pour les mouvements du robot et des bras
async def debut():
    # Avancer tout en repliant les bras
    await multitask(
        robot.straight(150),
        replier_bras()
    )

    # Effectuer le virage et attraper expert
    await robot.turn(58)
    await expert()

    # Autres mouvements après les tâches précédentes
    await robot.straight(230)
    await replier_bras()
    

#Exécuter bras + initialisation + avancer + expert
run_task(debut())
wait(100)


bg.run_target(990, -300, then=Stop.HOLD, wait=True)  
# Monter le bras à 6 cm après avoir attrapé expert

robot.settings(950, 950, 950, 950)
#presse 
robot.turn(-10)
robot.straight(200)
robot.straight(-38)
bd.run_target(990,-500)
robot.straight(-65)
bd.run_target(100,-483)
robot.straight(-240)

#base récuperation expert2 :  
robot.use_gyro(False)#gyro utilisé

#pousser expert (position trait avt dernier)
attendre_bouton()
wait(10)
robot.use_gyro(True)#gyro utilisé
bg.run_target(950,-530)
robot.straight(200)
robot.turn(30)
robot.straight(90)
robot.turn(-150)
robot.straight(60)

#base : 
robot.use_gyro(False)#gyro non utilisé
attendre_bouton()
wait(10)
robot.use_gyro(True)#gyro utilisé

#bateau
bg.run_target(950, -190) #levier §
robot.straight(340)#déplacement parallèle
bg.run_target(950,-550)
wait(10)
robot.straight(450)#déplacement2 parallèle
bg.run_target(950,-150)#fin
robot.turn(-2)
bd.run_target(950,0)

robot.straight(-800)#retour

bg.run_target(950, -250) #modification

robot.use_gyro(False)#gyro utilisé
attendre_bouton()
wait(10)
bd.run_target(950, -387) #levier §
robot.use_gyro(True)#gyro utilisé

# # # Scène
bd.run_target(950, -387) #levier §
robot.straight(630)#déplacement

robot.turn(-40)
bd.run_target(950,-340)
robot.settings(950, 450, 450, 450)
robot.straight(-80) #recule
robot.turn(-18)
robot.straight(190)
robot.turn(20)
bd.run_target(950, 0) 
bd.reset_angle(0)
robot.turn(70)
robot.straight(40)#barre hologramme
robot.straight(-100)

robot.settings(950, 950, 950, 950)
robot.turn(130)
robot.straight(-210)
robot.turn(-19)#dépose bonhomme
robot.straight(-70)
bg.run_target(100,0)
robot.turn(19)
robot.straight(600)
bg.run_target(950, -250) 

#base vers masterpiece
robot.use_gyro(False)#gyro non utilisé
#chargement
#se caler la droite sur le dernier gros trait face à l'autre base

attendre_bouton()
wait(10)
robot.use_gyro(True)#gyro utilisé

robot.settings(950, 650, 650, 650)

#traversée vers fleur2
robot.straight(640)
bg.run_target(950,-250)
robot.turn(93)#90
robot.straight(540)#fin trajet

#vers fleur2
robot.settings(950, 350, 150, 150)
bd.run_target(950,-10)
bd.run_target(950, -650)

robot.straight(-150)#levier (-2cm)
robot.turn(35)
robot.straight(-60)
bd.run_target(950, -200)
robot.turn(-90)
robot.settings(950, 950, 950, 950)
#masterpiece
robot.straight(200)#déplacement
robot.turn(35)
robot.straight(30) #dépose
robot.straight(-160)

#vers plateforme violette
robot.turn(-75)
robot.straight(350)
robot.turn(88)
robot.straight(25)

bd.run_target(950,-600, then=Stop.HOLD, wait=False)#modifier
wait (200)#essai1
robot.straight(-10)

bd.run_target(950,-300, then=Stop.HOLD, wait=False)#modifier
robot.turn(2)
robot.straight(15)

bd.run_target(200,-601)#essai2

bd.run_target(950, -20) 
robot.straight(-40)
robot.turn(-65)#déplacement
robot.straight(250)

#depose expert skate
robot.turn(-85)
robot.straight(-30)
robot.turn(-20)
robot.straight(-30)
bg.run_target(50, 0)

#vers base
robot.turn(30)
robot.straight(700)#déplacement

robot.use_gyro(False)#gyro utilisé

#vers dragon
attendre_bouton()
wait(10)
robot.use_gyro(True)#gyro utilisé

#dragon
bd.run_target(950, -20)
bg.run_target(600, -540, then=Stop.HOLD, wait=True)
robot.straight(290)
robot.turn(-15)
robot.turn(45)
robot.turn(-30)
robot.straight(-40)
robot.turn(-15)
robot.turn(45)
bg.run_target(600, -550, then=Stop.HOLD, wait=True)
robot.straight(-140)
robot.use_gyro(False)#gyro utilisé
attendre_bouton()
robot.use_gyro(True)#gyro utilisé
wait(10)

#depose expert dragon scenariste
bg.run_target(950, -250)
robot.straight(440)
robot.straight(-300)


# bd.run_target(950, -20)
# bg.run_target(600, -530, then=Stop.HOLD, wait=True)
# robot.straight(300)
# robot.turn(-15)
# robot.turn(45)
# robot.turn(-30)
# robot.straight(-140)


# # tour
# # Lancer le mouvement du bras gauche, sans attendre qu'il se termine
# bg.run_target(50, -100, then=Stop.HOLD, wait=False)

# # Lancer immédiatement le mouvement du bras droit
# bd.run_target(50, -100, then=Stop.HOLD, wait=True)

# # Attendre que le bras gauche ait terminé
# while not bg.control.done():
#     wait(100)
    
# bg.run_target(600, -400, then=Stop.HOLD, wait=False)
# bd.run_target(600, -400, then=Stop.HOLD, wait=True)





