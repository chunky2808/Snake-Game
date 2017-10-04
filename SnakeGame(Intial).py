# Snake Game

import pygame #module containg sound,graphics,used for 2d games
import sys # module has exit function 
import random # module - In snake game put food at random value so using it
import time #module - use when game is over

#checking initalization error

check_errors = pygame.init() # pygame.init() -initialise pygame,checking error

if check_errors[1] > 0: #return tuple (6,0) 6 succeful ,0 error 
	print("(!) Had {0} initializing errors,exiting....".format(check_errors[1]))
	sys.exit(-1) #use sys module to exit from game give error code -1
else:
	print("(+) Pygame successfully initialized!")

#checking initalization error

# Play Surface
playSurface = pygame.display.set_mode((720,460)) #uses function setmode to set width and height of screen
#set_mode take single argument so taking tuple as a argument using () for tuple

pygame.display.set_caption('Snake Game!!') #changing title of window

#time.sleep(5) #using sleep for 5 sec so that windows last for 5 seconds

# Play Surface

#Colors - Using RGB
red = pygame.Color(255,0,0)# Gameover #using text color takes 3 argument (R,G,B) 0 to 255
green = pygame.Color(0,255,0)# Snake # (r,g,b)red green blue
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food
yellow = pygame.Color(255,255,0)
#Colors


# FPS Controller  frames per second controller
fpsController = pygame.time.Clock()

#Important Variables

snakePos = [100,50] #variable for head (x,y) list 
#Don't Exceed Value Given in playSurface

snakeBody = [[100,50],[90,50],[80,50]] #list of list Have 3 block at start game having (x.y) coordinate
#using a block of list having (x,y) Coordinate
#Important Variables

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10] #using random module to place food taking argument in range (x,y)
foodSpawn = True

direction =  'RIGHT'
changeto = direction

score = 0

#Game over Function
def gameOver():#cantuse print to print something as it print on console not on screen
	myFont = pygame.font.SysFont('comicsansms',72) #name and size of font
	Gosurf = myFont.render('GAME OVER!!', True , red)#require 4 argument text,anti aliasing,color,background
	Gorect = Gosurf.get_rect() #rectangular component of game
	Gorect.midtop = (360, 15) #tuple (x,y) coordinate
	playSurface.blit(Gosurf,Gorect)
	showScore(123456778)
	pygame.display.flip()#update screen to show it in screen
	time.sleep(3)
	pygame.quit()#exit from pygame window
	sys.exit()#exit from console

#Game over Function

def showScore(choice=1):#showing score
	sFont = pygame.font.SysFont('comicsansms',26) #name and size of font
	Ssurf = sFont.render('Score : {0}'.format(score), True , green)#require 4 argument text,anti aliasing,color,background
	Srect = Ssurf.get_rect() #rectangular component of game
	if choice == 1:
		Srect.midtop = (80,10)#shows score on top left corner
	else:
		Srect.midtop = (360,120)#shows score on midle screen	
	playSurface.blit(Ssurf,Srect)
	
	
	

#EVENTS where something happen hit button in keyboard 
#first - hit
#second - amount of time u hold button
#third - release time period

#for every frame we get event

# Main Logic of snake game
while 1: #infinite Loop
	for event in pygame.event.get(): #give list of event inside pygame eveny
		if event.type == pygame.QUIT:#quit from game
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'): #ord checks ascii value
				changeto = 'RIGHT' #CHANGE DIRECTION TO RIGHT
			if event.key == pygame.K_LEFT or event.key == ord('a'): #ord checks ascii value
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'): #ord checks ascii value UP KEY OR W KEY IS PRESSED
				changeto = 'UP'		
			if event.key == pygame.K_DOWN or event.key == ord('s'): #ord checks ascii value DOWN KEY OR S KEY IS PRESSED
				changeto = 'DOWN'	#CHANGE DIRECTION TO DOWN
			if event.key == pygame.K_ESCAPE:#WHEN ESCAPE KEY IS PRESSED
				pygame.event.post(pygame.event.Event(pygame.QUIT)) #used to creater event (QUIT GAME)	

	#validation of direction
	#if we are moving to left then we cant move to right directly firest we go up then right
	#similarly if we are moving up then we cannot move down directly first we go to left/right then down
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'			
   #validation of direction
	
 #changing snake direction

	if direction == 'RIGHT':
		snakePos[0] += 10 #X coordinate
	if direction == 'LEFT':
 		snakePos[0] -= 10 #X coordinate
	if direction == 'UP':
 		snakePos[1] -= 10 #Y coordinate
	if direction == 'DOWN':
 		snakePos[1] += 10 #Y coordinate

  #changing snake direction
		
 	#Snake Body

	snakeBody.insert(0, list(snakePos)) #location where u want to insert and data what u want to put there

	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]: #matching x and y coordinate of snake and food 	
		score +=1
		foodSpawn = False #Snake Ate food  so it is not on screen
	else:
		snakeBody.pop()#if snake and food position does not match then reduce size

#food 

	if foodSpawn == False :#if food eaten then generate new food using generate
		foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10] #using random module to place food taking argument in range (x,y)
	foodSpawn = True
 	    
	#Background
	playSurface.fill(black)#fill entire game window with specific color
	
	#Draw Snake
	for pos in snakeBody:
		#pygame.Rect(pos[0],pos[1],10,10)#(x,y,sizex,sizey)
		pygame.draw.rect(playSurface, white , pygame.Rect(pos[0],pos[1],10,10) ) #draw snake require 3 argument player surface,color,component with x and y axis
	
	pygame.draw.rect(playSurface, yellow , pygame.Rect(foodPos[0],foodPos[1],10,10) ) #draw food	

  #Draw snake

#Boundaries of snake

	if snakePos[0]>710 or snakePos[0]<0 : #gameover window
		gameOver()
	if snakePos[1]>450 or snakePos[1]<0 : #gameover window
		gameOver()

	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]: #checking whether snake head touches its body if yes then game over
			gameOver()

#Boundaries of snake

	showScore()
	pygame.display.flip()#update screen to show it in screen
	fpsController.tick(22)#controls speed of game

