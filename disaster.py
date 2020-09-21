import random
import pygame
from tiles import *


class disasters(tiles):
	def __init__(self, X, Y, sizeX, j, intensityMin, intensityMax, typeOfMaterialAffected, mape):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.intensityMin = intensityMin
		self.intensityMax = intensityMax
		self.actualIntensity = -1
		self.typeOfMaterialAffected = typeOfMaterialAffected
		self.isOn = False
		self.numberTurnPrepPhase = 0
		self.counter = 0
		self.numberTurnIsActive = 0
		self.passable = False
		self.chanceItHappens = 10
		self.map = mape
		self.img_normal = pygame.image.load("tiles/void.png").convert()
		self.img_prep_phase = pygame.image.load("tiles/void.png").convert()
		self.img_is_on = pygame.image.load("tiles/void.png").convert()
		self.isPrepping = False
		self.isActive = False
		self.img = self.img_normal
		self.img = pygame.transform.rotate(self.img, rotation_random())

	
	def get_cells_around_this_point(self):
		a = []
		for i in range(-self.actualIntensity, self.actualIntensity + 1):
			for z in range(-self.actualIntensity, self.actualIntensity + 1):
				try:
					a.append(self.map[self.X + i][self.Y + z])
				except Exception as E:
					print(E)
		return (a)

	def trigger(self):
		if (self.actualIntensity == -1):
			self.actualIntensity = random.randint(self.intensityMin, self.intensityMax)
			self.isPrepping = True
		if (self.counter == self.numberTurnPrepPhase and self.isActive == False and self.isPrepping == True):
			print("Je suis là dedans")
			self.isPrepping == False
			self.isActive = True
			self.counter = 0
			self.img = self.img_is_on
			liste_cells = self.get_cells_around_this_point()
			for cells in liste_cells:
				for material in cells.typeOfMaterial:
					if material == self.typeOfMaterialAffected:
						self.map[cells.X][cells.Y].img = self.map[cells.X][cells.Y].img_being_destroyed
		elif (self.counter == self.numberTurnIsActive and self.isActive == True):
			print("L'éruption est finie")
			self.img = self.img_normal
			self.isActive = False
			liste_cells = self.get_cells_around_this_point()
			for cells in liste_cells:
				for material in cells.typeOfMaterial:
					if material == self.typeOfMaterialAffected:
						self.map[cells.X][cells.Y].img = self.map[cells.X][cells.Y].img_destroyed
			self.counter = 0
		print("Self counter = ", self.counter, "self.numberTurnIsActive = ", self.numberTurnIsActive)
		self.counter += 1


	def isDisasterHappening(self):
		if (self.isOn == True):
			self.trigger()
		else:
			i = random.randint(0, 1000)
			if (i < self.chanceItHappens):
				self.isOn = True 


class volcan(disasters):
	def __init__(self, X, Y, sizeX, j, intensityMin, intensityMax, typeOfMaterialAffected, mape, numberActive, numberPrepPhase):
		disasters.__init__(self, X, Y, sizeX, j, intensityMin, intensityMax, typeOfMaterialAffected, mape)
		self.tileName = "volcan"
		self.intensityMin = intensityMin
		self.intensityMax = intensityMax
		self.actualIntensity = -1
		self.typeOfMaterialAffected = typeOfMaterialAffected
		self.isOn = False
		self.numberTurnPrepPhase =numberPrepPhase
		self.counter = 0
		self.numberTurnIsActive = numberActive
		self.chanceItHappens = 10
		self.map = mape
		self.img_normal = pygame.image.load("tiles/volcan_e.png").convert()
		self.img_prep_phase = pygame.image.load("tiles/volcan_actif.png").convert()
		self.img_is_on = pygame.image.load("tiles/volcan_eruption.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())

		self.img = self.img_normal


if __name__ == "__main__":
	a = []
