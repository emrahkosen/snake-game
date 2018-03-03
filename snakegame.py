import pygame
import time
import random


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (250,50,50)
x = (4,45,84)
y = (65,115,245)
g_over = (100,55,55)
applerenk = (250,80,80)
green = (0,155,0)



display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((800,600)) #ekranboyutu

pygame.display.set_caption('baslik')
pygame.display.update() #pygame.display.flip() same

 

block_size = 10
FPS = 10

clock = pygame.time.Clock() # zaman ayarini yapiyoruz

font = pygame.font.SysFont(None, 50)

def message_to_screen(msg,color):
	screen_text = font.render(msg,True,color)
	gameDisplay.blit(screen_text, [10,10])
	

def snake(block_size, snakeList):
		for XnY in snakeList:
			gameDisplay.fill(y,rect = [XnY[0],XnY[1],block_size,block_size])


def gameloop():
	gameExist = False
	gameOver = False
	
	lead_x = display_width/2 
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0



	snakeList = []
	snakeLength = 5




	randApplex = round(random.randrange(10,display_width-block_size-5)/10)*10
	randAppley = round(random.randrange(0, display_height -block_size-5)/10)*10
	# round yazarak random sayinin 10 un katlari bir sayi gibi yaziyoruz
	# yada 10 dan kucuk bisey olarak
	# burda olmuyor ama hareketli simge ile
	# ayni hizada tutmaya yariyor



	while not gameExist:

		while gameOver == True:
			gameDisplay.fill(black)
			message_to_screen("game over :( press 'C' or  Q  ",g_over)
			pygame.display.update()	

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q :
						gameOver = False
						gameExist = True
					if event.key == pygame.K_c:
						gameloop()


		for event in pygame.event.get():
			print event

			if event.type == pygame.QUIT:
				gameExist = True
			else:
				gameExist = False

			# if event.type == pygame.KEYDOWN:
			#	if event.key == pygame.K_LEFT:
			#		lead_x -= 10
			#	if event.key == pygame.K_RIGHT:
			#		lead_x += 10
			#eger boyle yaparsak tuslara bastigimizda sadece 
			#bir defa ilerler
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0 

				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				#elif event.key == pygame.K_BACKSPACE:
				#	lead_x_change = 0
				#	lead_y_change = 0
				# backspace de hareketi durudurmak istedim
				# am durmadi :(	

			#if event.type == pygame.KEYUP:
			#	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			#		lead_x_change = 0
			#		lead_y_change = 0
				# burdada eger 	tuslardan elimizi cektigimiz zaman cisim duracak
		
		if lead_x > (display_width +5) or lead_x < (0-5) or lead_y > (display_height+5) or lead_y < (0- 5) :
			gameOver = True
			#burdada eger sinirlari gecerse cizim ekran kapaniyor 
		
		



		lead_x += lead_x_change	
		lead_y += lead_y_change

		gameDisplay.fill(x)

		
		pygame.draw.rect(gameDisplay,black,[400,300,100,100])
		
		pygame.draw.rect(gameDisplay,applerenk,[randApplex,randAppley,block_size,block_size])
		


		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		if len(snakeList) > snakeLength:
			del snakeList[0]

		snake(block_size, snakeList) # cismi function olarak yazdik




		pygame.display.update()
		if lead_x == randApplex and lead_y == randAppley:
			randApplex = round(random.randrange(0,display_width-block_size)/500)*500 # burda da bunu yaparak ust uste geldigi anda cismin yeri degisiyor
			randAppley = round(random.randrange(0, display_height -block_size)/500)*500
			snakeLength += 5

		clock.tick(FPS) #100 salise yada hangi birim biliyorum okadar zaman diliminde tekrarlaniyor


	message_to_screen("Gule Gule :(",red)
	pygame.display.update()

	time.sleep(1)
	pygame.quit()

	quit()


gameloop()
	