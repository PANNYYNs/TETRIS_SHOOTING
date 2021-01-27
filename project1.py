import pygame
import player
import enime
from random import *  
from maess import *
from atk import *
from total_score import *
import os
from game1 import *

pygame.init()
pygame.font.init()
gamedisplay = pygame.display.set_mode((1280,700))
icon = pygame.image.load("PlayGames.png").convert_alpha()
pygame.display.set_icon(icon)
s2 = pygame.image.load("s2.png").convert_alpha()
bg = pygame.image.load("bg_g.jpg").convert_alpha()
bg1 = pygame.image.load("bg.png").convert_alpha()
p1 = pygame.image.load("p.png").convert_alpha()
set_1 = pygame.image.load("set.jpg").convert_alpha()
s1 = pygame.image.load("s1.png").convert_alpha()
g1 = pygame.image.load("g.png").convert_alpha()
e1 = pygame.image.load("e1.png").convert_alpha()
e2 = pygame.image.load("e2.png").convert_alpha()
e3 = pygame.image.load("e3.png").convert_alpha()
e4 = pygame.image.load("e4.png").convert_alpha()
d1 = pygame.image.load("d1.png").convert_alpha()
star = pygame.image.load("star.png").convert_alpha()
go = pygame.image.load("go.png").convert_alpha()

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
print(max_score)


def main():
	
	def quitgame():
		pygame.quit()
		quit()

	def start_game():
		settings = False
		select = "Play"
		y = 260
		gamestart = False
		while not gamestart:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quitgame()
				if event.type == pygame.KEYDOWN:
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
					if event.key == pygame.K_RETURN: # เปลี่ยนตัวออก "q"
						if select == "Exit":
							quitgame()
						if select == "Play":
							game_start(health)
							gamestart = True
						if select == "Settings":
							settings = True
							y = 160
							x = 630 
				
				gamedisplay.blit(bg,(0,0))
				gamedisplay.blit(s2,(540,y))
			pygame.display.update()

	def game_restart():
		health = Total_Score(3)
		game_start(health)

	def game_start(i=0): 
		health = i
		pause = False
		restart = False
		gameexit = False
		start = False
		start = False
		shoot = False 
		shoot2 = False
		shoot3 = False
		shoot4 = False
		scroe = 0
		star_X = -100
		star_Y = -100
		star_ck = False
		start_enime = randint(1,4)
		save_enime = start_enime
		enime1 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		enime2 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		enime3 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		enime4 = enime.Enime(randint(321+e1_x,960-e1_x),5)
		while not gameexit:
			gamedisplay.blit(bg1,(0,0))
			# gamedisplay.blit(scroe_('Scroe: %d'%(total_scroe.get_total_score()),50),(20,10))
			# gamedisplay.blit(scroe_('Health:',50),(20,60))
			# gamedisplay.blit(scroe_('Top scroe:',50),(1000,10))
			# gamedisplay.blit(scroe_('%d' %max_score,50),(1000,60))
			gamedisplay.blit(s1,(player.x,player.y))
			gamedisplay.blit(g1,(player.x+player.xg+35,player.y+player.yg))
			gamedisplay.blit(star,(star_X,star_Y))

			if start_enime >= 1:
				gamedisplay.blit(e1,(enime1.x,enime1.y))
				gamedisplay.blit(g1,(enime1.x+enime1.xg+20,enime1.y+enime1.yg+30))
			if start_enime >= 2:
				gamedisplay.blit(e2,(enime2.x,enime2.y))
			if start_enime >= 3:
				gamedisplay.blit(g1,(enime3.x+enime3.xg+20,enime3.y+enime3.yg+30))
				gamedisplay.blit(e3,(enime3.x,enime3.y))
			if start_enime == 4:
				gamedisplay.blit(g1,(enime4.x+enime4.xg+20,enime4.y+enime4.yg+30))	
				gamedisplay.blit(e4,(enime4.x,enime4.y))

			if health.get_total_score() >= 1:
				gamedisplay.blit(s1,(20, 120))
			if health.get_total_score() >= 2:
				gamedisplay.blit(s1,(20 + s1_x, 120))
			if health.get_total_score() == 3:
				gamedisplay.blit(s1,(20 + s1_x*2, 120))
			if pause:
				if health.get_total_score() == 0:
					gamedisplay.blit(go,(0,0))
				else:
					gamedisplay.blit(d1,(0,0))
			ranTERTIT =  randint(4999,5000)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quitgame()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						quitgame()
					if event.key == pygame.K_r:
						if health.get_total_score() == 0:
							game_restart()


					if event.key == pygame.K_p:
						if pause == False:
							pause = True
						else:
							pause = False
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
						# print("sdasda")
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
						if enime1.x - 50 > 324:
							enime1.x -= 50
						elif enime1.x - 40 > 324:
							enime1.x -= 40
						elif enime1.x - 30 > 324:
							enime1.x -= 30
						elif enime1.x - 20 > 324:
							enime1.x -= 20
					elif ranmove == 0 or ranmove == 100:
						if enime1.x + 50 < 910:
							enime1.x += 50
						elif enime1.x + 40 < 910:
							enime1.x += 40
						elif enime1.x + 30 < 910:
							enime1.x += 30
						elif enime1.x + 20 < 910:
							enime1.x += 20
						
					if atk(player.x+player.xg+35,player.y+player.yg,enime1.x,enime1.y,e1_x):
						total_scroe.set_total_score(50)
						enime1.x = -532311
						enime1.y = -123434
						save_enime -= 1

				if start_enime >= 2:
					ranmove2 = randint(0,300)
					if ranmove2 == 1 or ranmove2 == 200:
						if enime2.x - 50 > 324:
							enime2.x -= 50
						elif enime2.x - 40 > 324:
							enime2.x -= 40
						elif enime2.x - 30 > 324:
							enime2.x -= 30
						elif enime2.x - 20 > 324:
							enime2.x -= 20
					elif ranmove2 == 0 or ranmove2 == 100:
						if enime2.x + 50 < 910:
							enime2.x += 50
						elif enime2.x + 40 < 910:
							enime2.x += 40
						elif enime2.x + 30 < 910:
							enime2.x += 30
						elif enime2.x + 20 < 910:
							enime2.x += 20
					elif ranmove2 == 2 or ranmove2 == 300:
						if enime2.y + e1_y < 720:
							enime2.y += 30
							if enime2.y + e1_y >= player.y + player.yg:
								enime2.x = +12342
								enime2.y = +123423
								health.set_total_score(-1)
						
					if atk(player.x+player.xg+35,player.y+player.yg,enime2.x,enime2.y,e1_x):
						total_scroe.set_total_score(100)
						enime2.x = -12343
						enime2.y = -123432
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
						if enime3.x - 50 > 324:
							enime3.x -= 50
						elif enime3.x - 40 > 324:
							enime3.x -= 40
						elif enime3.x - 30 > 324:
							enime3.x -= 30
						elif enime3.x - 20 > 324:
							enime3.x -= 20
					elif ranmove3 == 0 or ranmove3 == 100:
						if enime3.x + 50 < 910:
							enime3.x += 50
						elif enime3.x + 40 < 910:
							enime3.x += 40
						elif enime3.x + 30 < 910:
							enime3.x += 30
						elif enime3.x + 20 < 910:
							enime3.x += 20
					elif ranmove3 == 2 or ranmove3 == 300:
						if enime3.y + e1_y < 720:
							enime3.y += 30
							if enime3.y + e1_y >= player.y + player.yg:
								enime3.x = +123423
								enime3.y = +1234234
								health.set_total_score(-1)
					
					if atk(player.x+player.xg+35,player.y+player.yg,enime3.x,enime3.y,e1_x):
						total_scroe.set_total_score(150)
						enime3.x = -1325234
						enime3.y = -123425
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
						if enime4.x - 50 > 324:
							enime4.x -= 50
						elif enime4.x - 40 > 324:
							enime4.x -= 40
						elif enime4.x - 30 > 324:
							enime4.x -= 30
						elif enime4.x - 20 > 324:
							enime4.x -= 20
					elif ranmove4 == 0 or ranmove4 == 100:
						if enime4.x + 50 < 910:
							enime4.x += 50
						elif enime4.x + 40 < 910:
							enime4.x += 40
						elif enime4.x + 30 < 910:
							enime4.x += 30
						elif enime4.x + 20 < 910:
							enime4.x += 20
					elif ranmove4 == 2 or ranmove4 == 200:
						if enime4.y + e1_y < 720:
							enime4.y += 40
							if enime4.y + e1_y >= player.y + player.yg:
								enime4.x = +12342
								enime4.y = +123124
								health.set_total_score(-1)
					elif ranmove4 == 4 or ranmove4 == 150:
						if enime4.y + e1_y < 0:
							enime4.y -= 40
					
					if atk(player.x+player.xg+35,player.y+player.yg,enime4.x,enime4.y,e1_x):
						total_scroe.set_total_score(200)
						enime4.x = -3123123
						enime4.y = -12313
						save_enime -= 1
				if star_ck == False:
					
					if ranTERTIT == 5000:
						ranNUM =  randint(10,14)
						star_X = ranTERTIT // ranNUM
						star_Y = -10

				star_Y += 1
				star_ck = True
				if star_Y > 750:
					star_Y = -100
					star_X = -100
					star_ck = False

				if atk (star_X,star_Y,player.x,player.y,s1_x) :
					star_ck = False
					pause = True
					star_X = -100
					sraR_y = 780
					TER_main_menu()
					# print("sdasd")

				if save_enime == 0:
					game_start()
					
				if health.get_total_score() == 0:
					if (total_scroe.get_total_score() > max_score):
						max_score_file = open('max_score.txt', "w")
						max_score_file.write(str(total_scroe.get_total_score()))
					pause = True

			pygame.display.update()

	start_game()

if __name__ == '__main__':
	main()
