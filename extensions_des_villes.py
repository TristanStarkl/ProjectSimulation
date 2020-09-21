import random
import time
import pygame


def rotation_random2():
	a = [0, 90, 180, 270]
	return (random.choice(a))

class extension():
	def __init__(self):
		self.tileName = ""
		self._city = 0
		self.passable = False
		self.hasSeaAccess = False
		self._urbanisation = 0
		self._forestSize = 0
		self._mountainSize = 0
		self._fieldsSize = 0
		self._citiesSpace = 0
		self._waterSpace = 0
		self._labSpace = 0
		self._liveStockSize = 0
		self._artisanSpace = 0
		self._soldierSpace = 0
		self.isExtension = True
		self.X = 0
		self.Y = 0
		self.img = pygame.image.load("tiles/void.png")

class logement(extension):
	def __init__(self, X, Y, city, size, typeOfMaterial):
		extension.__init__(self)
		self.tileName = "logement"
		self._city = city
		self.X = X
		self.Y = Y
		self._urbanisation = 500
		self.typeOfMaterial = ["wood", "stone"]
		for material in typeOfMaterial:
			if (material == "desert"):
				self.img_desert_village = pygame.image.load("tiles/village_d.png").convert()
				self.img_desert_ville = pygame.image.load("tiles/ville_d.png").convert()
				self.img = self.img_desert_village
			elif (material == "land"):
				self.img_village = pygame.image.load("tiles/village.png").convert()
				self.img_ville = pygame.image.load("tiles/city.png").convert()
				self.img = self.img_village

class dock(extension):
	def __init__(self, X, Y, city, size):
		extension.__init__(self)
		self.tileName = "dock"
		self._city = city
		self.X = X
		self.Y = Y
		self._waterSpace = size
		self.img = pygame.image.load("tiles/dock.png").convert()
		self.typeOfMaterial = ["wood"]


class farmland(extension):
	def __init__(self, X, Y, city, size):
		extension.__init__(self)
		self.tileName = "farmland"
		self.typeOfMaterial = ["wood"]
		self._city = city
		self.X = X
		self.Y = Y
		self._fieldsSize = size
		self.img = pygame.image.load("tiles/champs.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random2())

class orchard(extension):
	def __init__(self, X, Y, city, size):
		extension.__init__(self)
		self.tileName = "orchard"
		self.typeOfMaterial = ["wood"]
		self._city = city
		self.X = X
		self.Y = Y
		self._forestSize = size
		self.img = pygame.image.load("tiles/verger.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random2())


