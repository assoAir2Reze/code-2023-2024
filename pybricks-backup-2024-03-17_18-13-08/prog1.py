def prog1(nb, hub:PrimeHub, robot:DriveBase, bg:Motor, bd:Motor):
 # 2024-03-16
 # 9 - Le code pour le BATEAU
 hub.display.number(nb)
 #wait(WAIT_TIME)
 
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

 robot.turn(30)
 robot.straight(450)
 bg.run_angle(200, 300)
