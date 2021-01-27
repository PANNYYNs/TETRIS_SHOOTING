import pygame
#import player
#import enime
import game1
#from game1 import *


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
    gameexit = False
    y = 260
    select = "Play"
    select_set = "ON"
    start = False
    pause = False
    settings = False
	
    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==  pygame.KEYDOWN:
                print("FUCK")
                game1.TER_main_menu()
                
            pygame.display.update()
pygame.init()
main()
