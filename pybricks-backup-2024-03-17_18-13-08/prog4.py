def prog4(hub:PrimeHub, robot:DriveBase, bg:Motor, bd:Motor):
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
