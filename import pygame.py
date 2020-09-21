import pygame
from pygame.locals import *
 
pygame.init()
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
"""fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert()
fenetre.blit(perso, (200,300))

#Rafraîchissement de l'écran
pygame.display.flip()
"""

continuer = 1
while  continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0 
			print("Je quitte la fenêtre")
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			print(event.pos)
			print("Je clique sur la souris")