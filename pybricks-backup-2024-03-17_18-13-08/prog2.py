def prog2(hub:PrimeHub, robot:DriveBase, bg:Motor, bd:Motor):
 # 2024-03-16
 # 10 - Le code pour la table de mixage
  
 #J'y vais 
 
 robot.settings(600, 600, 750, 750)

 toto = bd.run_until_stalled(400, duty_limit = 10)
 #print(toto)

 

 bd.run_angle(200, -300)
 robot.straight(100)
 robot.turn(50)
 robot.straight(250)
 
 robot.settings(200, 200, 200, 200)

 robot.straight(90)#100
 robot.turn(-15)
 bd.run_angle(200, 500)#300
 robot.settings(100, 100, 100, 100)
 robot.turn(45)
 robot.settings(600, 600, 750, 750)
 robot.straight(-300)
 


 #Je réalise la mission
 #Todo