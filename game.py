import pygame
import time
import random

pygame.init()


screen_width = 800
screen_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green  = (0, 255, 0)

block_color = (53, 115, 255)

car_width =73



gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('game')
clock = pygame.time.Clock


carImg =pygame.image.load('racecar.png')



def things_dodge(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+str(count), True, black)
	gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
	gameDisplay.blit(carImg, (x,y))


def text_objects(text, font):
	textsurface = font.render(text, True, black)
	return textsurface, textsurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)	
	TextRect.center = ((screen_width/2),(screen_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():
	message_display('CRASHED')

def button(msg, x,y,w,h,ic,ac):	
	mouse = pygame.mouse.get_pos()

if x+w > mouse[0] > x and y+h > mouse[1] > y:
	pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
else:
	pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

smallText = pygame.font.Font("freesansbold.ttf",20) 	
TextSurf, TextRect =text_objects(msg, smallText)
TextRect.center = ((x+(w/2)), (y+(h/2)))
gameDisplay.blit(TextSurf, TextRect)

def quitgame ():
	pygame.quit()
	quit()

def pause():
	pause =True	
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

gameDisplay.fill((white))

largeText = pygame.font.Font('freesansbold.ttf',115)	
TextSurf, TextRect = text_objects("paused", largeText)	
TextRect.center = ((screen_width/2),(screen_height/2))
gameDisplay.blit(TextSurf, TextRect)

#making button interactive
button("Continue",150,450,100,50,green,bright_green,)
button("QUIT",550,450,100,50,red,bright_red)

pygame.display.update()
clock(15)		


def game_intro():
	intro =True	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

gameDisplay.fill((white))

largeText = pygame.font.Font('freesansbold.ttf',115)	
TextSurf, TextRect = text_objects("game", largeText)	
TextRect.center = ((screen_width/2),(screen_height/2))
gameDisplay.blit(TextSurf, TextRect)

#making button interactive
button("GO!",150,450,100,50,green,bright_green, game_loop)
button("QUIT",550,450,100,50,red,bright_red, quitgame)

pygame.display.update()
clock(15)		

# drawing button
pygame.draw.rect(gameDisplay, green, (150,450,100,50))
pygame.draw.rect(gameDisplay, red, (550,450,100,50))


pygame.display.update()
clock.tick(15)


def game_loop():
    x= (screen_width * 0.45)
    y= ( screen_height *0.8)	

x_change= 0

thing_startx = random.randrange(0, screen_width)
thing_starty = -600
thing_speed = 4
thing_width = 100
thing_height = 100

thingCount = 1

dodged = 0 

gameExit =False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

			if event.type == pygame.KEYDOWN:
				if event.type == pygame.K_LEFT:
					x_change = -5 
				elif event.key == pygame.K_RIGHT:
					x_change = -5	

		if event.type == pygame.KEYUP:
			if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0

	x += x_change 			
	gameDisplay.fill(white)

	things(thing_startx, thing_starty, thing_width, thing_height, block_color)
	thing_starty += thing_speed

	car(x,y)

things_dodged= (dodged)

if x > screen_width - car_width or x < 0:
	    crash()

if thing_starty > screen_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,screen_width)	
			dodged += 1
			thing_speed += 0.1
			thing_width += (dodged * 1.2)

if y < thing_starty+thing_height:
	print('y crossover')

if x > thing_startx and x < thing_startx + thing_width or x+car_width >thing_startx and x + car_width < thing_startx+thing_width:
	print('x crossover')
	crash()
	

pygame.display.update()	
clock.tick(60)
	
game_intro()
game_loop()
pygame.quit()
quit()
