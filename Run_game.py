import pygame
import player
import enime
from random import *  
from maess import *
from atk import *
from total_score import *
import os

pygame.init()
pygame.font.init()
gamedisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Bomberman")
icon = pygame.image.load("PlayGames.png").convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load("bg_g.jpg").convert_alpha()
bg1 = pygame.image.load("bg.png").convert_alpha()
s1 = pygame.image.load("s1.png").convert_alpha()
g1 = pygame.image.load("g.png").convert_alpha()
e1 = pygame.image.load("e1.png").convert_alpha()
e2 = pygame.image.load("e2.png").convert_alpha()
e3 = pygame.image.load("e3.png").convert_alpha()
e4 = pygame.image.load("e4.png").convert_alpha()

star = pygame.image.load("star.png").convert_alpha()


s1_x = s1.get_rect().size[0]
s1_y = s1.get_rect().size[1]
e1_x = e1.get_rect().size[0]
player = player.Player((1280-s1_x)/2,690-s1_y)
e1_y = e1.get_rect().size[1]
clock = pygame.time.Clock()
total_scroe = Total_Score(0)
health = Total_Score(3)
TERTIT = False


f = open('max_score.txt','r')
file = f.readlines()
max_score = int(file[0])


def main():

	def quitgame():
		gameexit = True
		pygame.quit()
		quit()

	def game_start():
		global gameexit
		gameexit = False
		y = 260
		x = 540
		select = "Play"
		select_set = "ON"
		start = False
		shoot = False 
		shoot2 = False
		shoot3 = False
		shoot4 = False
		pause = False
		settings = False
		scroe = 0
		start_enime = randint(0,300)%4 +1
		save_enime = start_enime
		enime1 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		enime2 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		enime3 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		enime4 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		while not gameexit:
			gamedisplay.blit(bg1,(0,0))	
			gamedisplay.blit(scroe_('Scroe: %d'%(total_scroe.get_total_score()),50),(20,10))
			gamedisplay.blit(scroe_('Health:',50),(20,60))
			gamedisplay.blit(scroe_('Top scroe:',50),(1000,10))
			gamedisplay.blit(scroe_('%d' %max_score,50),(1000,60))
			gamedisplay.blit(s1,(player.x,player.y))
			gamedisplay.blit(g1,(player.x+player.xg+35,player.y+player.yg))



			if health.get_total_score() >= 1:
				gamedisplay.blit(s1,(20, 120))
			if health.get_total_score() >= 2:
				gamedisplay.blit(s1,(20 + s1_x, 120))
			if health.get_total_score() == 3:
				gamedisplay.blit(s1,(20 + s1_x*2, 120))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quitgame()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						quitgame()
					if event.key == pygame.K_a:
						player.set_running("Left",True)
					if event.key == pygame.K_d:
						player.set_running("Right",True)
					if event.key == pygame.K_SPACE:
						if player.get_shot() == False:
							player.set_running("Gun",True)

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_a:
						player.set_running("Left",False)
						if player.get_shot() and not player.get_running("Gun"):
							player.set_xg(0)
					if event.key == pygame.K_d:
						player.set_running("Right",False)
						if player.get_shot() and not player.get_running("Gun"):
							player.set_xg(0)
					if event.key == pygame.K_SPACE:
						player.set_shot(True)

			if pause == False:
				if player.get_running("Left"):
					if player.x + s1_x > 321 + s1_x:
						player.x -= 3
						if player.get_running("Gun"):
							player.xg += 3
						else:
							player.set_xg(0)
				if player.get_running("Right"):
					if player.x + s1_x < 960:
						player.x += 3
						if player.get_running("Gun"):
							player.xg -= 3
						else:
							player.set_xg(0)
				if player.get_running("Gun"):
					player.yg -= 5
					if player.y + player.yg < -20:
						player.set_yg(0)
						player.set_xg(0)
						if player.get_shot():
							if player.y + player.yg >= -20:
								player.set_running("Gun",False)
								player.set_shot(False)

				if atk(enime1.x+enime1.xg+35,enime1.y+enime1.yg,player.x,player.y,s1_x) or atk(enime2.x+enime2.xg+35,enime2.y+enime2.yg,player.x,player.y,s1_x) or atk(enime3.x+enime3.xg+35,enime3.y+enime3.yg,player.x,player.y,s1_x) or atk(enime2.x+enime2.xg+35,enime2.y+enime2.yg,player.x,player.y,s1_x) or atk(enime4.x+enime4.xg+35,enime4.y+enime4.yg,player.x,player.y,s1_x):
					health.set_total_score(-1)
					
				
				# Start Enime
				if start_enime >= 1:
					ranshoot =  randint(0,100)
					if ranshoot == 50:
						shoot = True
					if shoot :
						enime1.yg += 5
						if enime1.y + enime1.yg > 750:
							enime1.set_yg(0)
							shoot = False
					ranmove = randint(0,200)
					if ranmove == 1 or ranmove == 200:
						if enime1.x - 50 > 321:
							enime1.x -= 50
						elif enime1.x - 40 > 321:
							enime1.x -= 40
						elif enime1.x - 30 > 321:
							enime1.x -= 30
						elif enime1.x - 20 > 321:
							enime1.x -= 20
					elif ranmove == 0 or ranmove == 100:
						if enime1.x + 50 < 960:
							enime1.x += 50
						elif enime1.x + 40 < 960:
							enime1.x += 40
						elif enime1.x + 30 < 960:
							enime1.x += 30
						elif enime1.x + 20 < 960:
							enime1.x += 20
					gamedisplay.blit(e1,(enime1.x,enime1.y))
					gamedisplay.blit(g1,(enime1.x+enime1.xg+20,enime1.y+enime1.yg+30))	
					if atk(player.x+player.xg+35,player.y+player.yg,enime1.x,enime1.y,e1_x):
						total_scroe.set_total_score(50)
						enime1.x = -10000
						enime1.y = -1000
						save_enime -= 1

				if start_enime >= 2:
					ranmove2 = randint(0,300)
					# ranmove2 = 2
					if ranmove2 == 1 or ranmove2 == 200:
						if enime2.x - 50 > 321:
							enime2.x -= 50
						elif enime2.x - 40 > 321:
							enime2.x -= 40
						elif enime2.x - 30 > 321:
							enime2.x -= 30
						elif enime2.x - 20 > 321:
							enime2.x -= 20
					elif ranmove2 == 0 or ranmove2 == 100:
						if enime2.x + 50 < 960:
							enime2.x += 50
						elif enime2.x + 40 < 960:
							enime2.x += 40
						elif enime2.x + 30 < 960:
							enime2.x += 30
						elif enime2.x + 20 < 960:
							enime2.x += 20
					elif ranmove2 == 2 or ranmove2 == 300:
						if enime2.y + e1_y < 720:
							enime2.y += 30
							if enime2.y + e1_y >= player.y + player.yg:
								enime2.x = +10000
								enime2.y = +10000
								health.set_total_score(-1)
					gamedisplay.blit(e2,(enime2.x,enime2.y))	
					if atk(player.x+player.xg+35,player.y+player.yg,enime2.x,enime2.y,e1_x):
						total_scroe.set_total_score(100)
						enime2.x = -10000
						enime2.y = -1000
						save_enime -= 1

				if start_enime >= 3:
					ranshoot3 =  randint(0,100)
					if ranshoot3 == 50:
						shoot3 = True
					if shoot3 :
						enime3.yg += 5
						if enime3.y + enime3.yg > 750:
							enime3.set_yg(0)
							shoot3 = False
					ranmove3 = randint(0,300)
					if ranmove3 == 1 or ranmove3 == 500:
						if enime3.x - 50 > 321:
							enime3.x -= 50
						elif enime3.x - 40 > 321:
							enime3.x -= 40
						elif enime3.x - 30 > 321:
							enime3.x -= 30
						elif enime3.x - 20 > 321:
							enime3.x -= 20
					elif ranmove3 == 0 or ranmove3 == 100:
						if enime3.x + 50 < 960:
							enime3.x += 50
						elif enime3.x + 40 < 960:
							enime3.x += 40
						elif enime3.x + 30 < 960:
							enime3.x += 30
						elif enime3.x + 20 < 960:
							enime3.x += 20
					elif ranmove3 == 2 or ranmove3 == 300:
						if enime3.y + e1_y < 720:
							enime3.y += 30
							if enime3.y + e1_y >= player.y + player.yg:
								enime3.x = +10000
								enime3.y = +10000
								health.set_total_score(-1)
					gamedisplay.blit(g1,(enime3.x+enime3.xg+20,enime3.y+enime3.yg+30))
					gamedisplay.blit(e3,(enime3.x,enime3.y))	
					if atk(player.x+player.xg+35,player.y+player.yg,enime3.x,enime3.y,e1_x):
						total_scroe.set_total_score(150)
						enime3.x = -10000
						enime3.y = -1000
						save_enime -= 1

				if start_enime == 4:
					ranshoot4 =  randint(0,100)
					if ranshoot4 == 50:
						shoot4 = True
					if shoot4 :
						enime4.yg += 5
						if enime4.y + enime4.yg > 750:
							enime4.set_yg(0)
							shoot4 = False
					ranmove4 = randint(0,200)
					if ranmove4 == 1 or ranmove4 == 50:
						if enime4.x - 50 > 321:
							enime4.x -= 50
						elif enime4.x - 40 > 321:
							enime4.x -= 40
						elif enime4.x - 30 > 321:
							enime4.x -= 30
						elif enime4.x - 20 > 321:
							enime4.x -= 20
					elif ranmove4 == 0 or ranmove4 == 100:
						if enime4.x + 50 < 960:
							enime4.x += 50
						elif enime4.x + 40 < 960:
							enime4.x += 40
						elif enime4.x + 30 < 960:
							enime4.x += 30
						elif enime4.x + 20 < 960:
							enime4.x += 20
					elif ranmove4 == 2 or ranmove4 == 200:
						if enime4.y + e1_y < 720:
							enime4.y += 40
							if enime4.y + e1_y >= player.y + player.yg:
								enime4.x = +10000
								enime4.y = +10000
								health.set_total_score(-1)
					elif ranmove4 == 4 or ranmove4 == 150:
						if enime4.y + e1_y < 0:
							enime4.y -= 40
					gamedisplay.blit(g1,(enime4.x+enime4.xg+20,enime4.y+enime4.yg+30))	
					gamedisplay.blit(e4,(enime4.x,enime4.y))
					if atk(player.x+player.xg+35,player.y+player.yg,enime4.x,enime4.y,e1_x):
						total_scroe.set_total_score(200)
						enime4.x = -10000
						enime4.y = -1000
						save_enime -= 1
			
	

			if save_enime == 0:
				game_start()
			
			if health.get_total_score() == 0:
				if (total_scroe.get_total_score() > max_score):
					max_score_file = open('max_score.txt', "w")
					max_score_file.write(str(total_scroe.get_total_score()))
				quitgame()
			
			pygame.display.update()
	game_start()

main()
