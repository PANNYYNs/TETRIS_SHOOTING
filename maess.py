import pygame

def message(text,size,color,text_font= "munro.ttf"):

	myfont = pygame.font.Font(text_font,size)
	mymeassage = myfont.render(text,True,color)
	return mymeassage

def scroe_(value,size):
	return message(value,size,(255,255,255))