import pygame
#import player
#import enime

#from atk import *

pygame.init()
pygame.font.init()
gamedisplay = pygame.display.set_mode((1280,720))
icon = pygame.image.load("PlayGames.png").convert_alpha()
pygame.display.set_icon(icon)
s2 = pygame.image.load("s2.png").convert_alpha()
bg = pygame.image.load("bg_g.jpg").convert_alpha()
bg1 = pygame.image.load("bg.png").convert_alpha()
p1 = pygame.image.load("p.png").convert_alpha()
set_1 = pygame.image.load("set.jpg").convert_alpha()



def main():
	
	def quitgame():
		pygame.quit()
		quit()

	def game_start():
		gameexit = False
		y = 260
		select = "Play"
		select_set = "ON"
		start = False
		#shoot = False 
		pause = False
		settings = False
		#scroe = 0
		while not gameexit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quitgame()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						if start == True :
							if pause == False:
								pause = True
							else:
								pause = False

					if event.key == pygame.K_q:
						start = False
						
						pause = False
						if settings :
							settings = False
							y = 315

					if event.key == pygame.K_RETURN: # เปลี่ยนตัวออก "q"

						if select == "Exit":
							quitgame()
						if select == "Play":
							start = True
						if select == "Settings":
							settings = True
							y = 160
							x = 630 


					if event.key == pygame.K_DOWN:
						if settings == False:
							if select == "Play":
								y = 315
								select = "Settings"
							elif select == "Settings":
								y = 375
								select = "Exit"
							elif select == "Exit":
								y = 270
								select = "Play"
						elif settings == True:
							if select_set == "ON":
								x = 700

							else:
								pass
				

			if start:
                                #import game1
				pygame.quit()
				import pygame_
				
			else:
				if settings:
					gamedisplay.blit(bg1,(0,0))	
					gamedisplay.blit(s2,(590,y))
					# gamedisplay.fill((0,0,0))
					

				else:
					gamedisplay.blit(bg,(0,0))
					gamedisplay.blit(s2,(540,y))
			

			
			pygame.display.update()
	game_start()

if __name__ == '__main__':
	main()
