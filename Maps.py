import random
from threading import RLock
from opensimplex import OpenSimplex
from City import *
import random
import string
import time
from timeit import default_timer as timer
import pygame
from pygame.locals import *
import option
from statistics import mean
from tiles import *
from disaster import *
pygame.init()

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



class Map():
	def __init__(self, option):
		self.map = list()
		self.width = option.nbCasesX * 30
		self.height = option.nbCasesY * 30
		self._cities = []
		if option.fullscreen == True:
			self.window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		else:
			self.window = pygame.display.set_mode((self.width, self.height))
		self.tmp = OpenSimplex(round(time.time()))
		self.sizeX = option.nbCasesX
		self.sizeY = option.nbCasesY
		self.tiles = ["sea", "mountain", "land", "forest", "iceberg", "colline", "jungle"]
		self.disasters = []
		for x in range(option.nbCasesX+1):
			self.map.append(list())
			for y in range(option.nbCasesY+1):
				self.map[x].append(thevoid(self.window, 0, 0, 0, 0))


	def getTile(self, X, Y):
		print(len(self.map))
		return (self.map[X][Y])

	def placeCity(self, city, X, Y):
		tile = self.map[X][Y]
		self.map[X][Y] = city
		del tile

	def getAdjacentCells(self, X, Y):
		result = []
		try:
			result.append(self.map[X-1][Y-1])
		except:
			pass
		try:
			result.append(self.map[X-1][Y])
		except:
			pass
		try:
			result.append(self.map[X-1][Y+1])
		except:
			pass
		try:
			result.append(self.map[X][Y-1])
		except:
			pass
		try:
			result.append(self.map[X][Y+1])
		except:
			pass
		try:
			result.append(self.map[X+1][Y-1])
		except:
			pass
		try:
			result.append(self.map[X+1][Y])
		except:
			pass
		try:
			result.append(self.map[X+1][Y+1])
		except:
			pass
		return (result)

	def hasSeaAccess(self, X, Y):
		result = self.getAdjacentCells(X, Y)
		for r in result:
			if r != 0:
				if (r.getName() == "sea"):
					return (True)
		return (False)

	def generate(self):
		x = 0
		while x < self.sizeX:
			y = 0
			while y < self.sizeY:
				z1 = (x + y) / 2
				s = (x + y + z1) / 3
				j = self.tmp.noise2d((x+s) / 16, (y+s) / 16)
				gradient_chaleur = self.tmp.noise2d((y+s)/40, (x+s)/40)
				reef_time = self.tmp.noise2d((x + y) / 2, (x + s) / 2)
				wetness = self.tmp.noise2d((x + y) / 20, (x + s) / 20)
				disaster_random = self.tmp.noise2d ((x + y) / 3, (x + s) / 3)
				if disaster_random > 0.7:
					a = volcan(x, y, self.sizeX, j, random.randint(0, 1), random.randint(1, 5), "wood", self.map, random.randint(1, 5), random.randint(1, 5))
					self.map[x][y] = a
					self.disasters.append(a)
				elif (j < -0.5):
					i = random.randint(10, 50)
					if (i == 42):
						self.map[x][y] = island_ocean(self.window, x, y, self.sizeX, j)
					else:
						self.map[x][y] = ocean(self.window, x, y, self.sizeX, j)
				elif (j < -0.3) and (gradient_chaleur < -0.4):
					self.map[x][y] = iceberg(self.window,  x, y, self.sizeX, j)
				elif (j < -0.3) :
					i = random.randint(10, 50)
					if (i == 42):
						self.map[x][y] = island(self.window, x, y, self.sizeX, j)
					else:
						if (reef_time < -0.20):
							self.map[x][y] = reef(self.window, x, y, self.sizeX, j)
						else:
							self.map[x][y] = sea(self.window, x, y, self.sizeX, j)
				elif (j < 0.20) and (gradient_chaleur > 0.5):
					self.map[x][y] = desert(self.window, x, y, self.sizeX, j)		
				elif (j < 0.20) and (gradient_chaleur > 0.3):
					self.map[x][y] = savanah(self.window, x, y, self.sizeX, j)		
				elif (j < 0.20) and (gradient_chaleur < -0.3):
					self.map[x][y] = tundra(self.window, x, y, self.sizeX, j)		
				elif (j < 0.20 and wetness > 0.4):
					self.map[x][y] = swamp(self.window, x, y, self.sizeX, j)
				elif (j < 0.20 ):
					self.map[x][y] = land(self.window, x, y, self.sizeX, j)
				elif (j < 0.50) and (gradient_chaleur > 0.3) and wetness > 0.4:
					self.map[x][y] = jungle(self.window, x, y, self.sizeX, j)
				elif (j < 0.50) and (gradient_chaleur < -0.3):
					self.map[x][y] = taiga(self.window, x, y, self.sizeX, j)
				elif (j < 0.50):
					self.map[x][y] = forest(self.window, x, y, self.sizeX, j)
				elif (j < 0.60) and (gradient_chaleur < -0.3):
					self.map[x][y] = colline_enneige(self.window, x, y, self.sizeX, j)
				elif (j < 0.60):
					self.map[x][y] = colline(self.window, x, y, self.sizeX, j)
				else:
					self.map[x][y] = mountain(self.window, x, y, self.sizeX, j)
				y += 1
			x += 1

	def start(self, option, nbcities, popstart, nbyears):
		for i in range(nbcities):
			name = randomString(random.randint(3, 10))
			c = cities(self, 1000, popstart ,name,  nbyears, self.window)
			c.placeOnMap(self, option.nbCasesX, option.nbCasesY)
			c.initializePopulation()
			self._cities.append(c)
		for s in self._cities:
			s.start()


	def show(self):
		self.offset_h = 0
		self.offset_v = 0
		continuer = 1
		infoObject = pygame.display.Info()
		screenresW = infoObject.current_w
		screenresH = infoObject.current_h
		listes_frame = list()
		pygame.display.set_caption('Evolution, History')
		while continuer:
			a = timer()
			pygame.draw.rect(self.window, (0, 0, 0), (0, 0, screenresW, screenresH))
			for x in range(self.sizeX):
				for y in range(self.sizeY):
					tiles = self.map[x][y]
					tileX = tiles.X*30 + (self.offset_v *30)
					tileY = tiles.Y * 30 + (self.offset_h * 30)
					if (tileX >= 0 and tileX < screenresW) and (tileY >= 0 and tileY < screenresH):
						self.window.blit(tiles.img, (tileX, tileY))

			pygame.display.flip()
			for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
				pygame.key.set_repeat()
				if event.type == QUIT:     #Si un de ces événements est de type QUIT
					continuer = 0 
					print("Je quitte la fenêtre")
					return 
				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					Y = int(event.pos[1] / 30) - self.offset_h
					X = int(event.pos[0] / 30) - self.offset_v
					print("---------------")
					print(self.map[X][Y].tileName, X, Y)
					if (self.map[X][Y].tileName.startswith("City ")):
						pop = self.map[X][Y]._populationSize
						if (pop != 0):
							print("La ville ", self.map[X][Y].tileName, " possède une population de ", pop, " âmes, et un stock de nourriture de ", self.map[X][Y]._quantityFood)
						else:
							print("La ville ", self.map[X][Y].tileName, " est déserte. Tout ses habitants sont morts.")
						solo = self.map[X][Y].when_pressed()
						"""if (solo != None):
							option.saveToFile(solo)"""
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					continuer = 0
					print("je quitte la fenêtre")
					print("Temps moyen: ", mean(listes_frame))
					print("La frame la plus courte: ", min(listes_frame))
					print("La frame la plus longue: ", max(listes_frame))
				if event.type == KEYDOWN and event.key == K_e:
					for dis in self.disasters:
						dis.trigger()

				if (event.type == KEYDOWN) and (event.key == K_SPACE):
					for x in range(self.sizeX):
						for y in range(self.sizeY):
							if (self.map[x][y].tileName.startswith("City ")):
								self.map[x][y].pause_the_city()

				#pygame.key.set_repeat(10)
				if event.type == KEYDOWN and (event.key == K_DOWN or event.key == K_s):
					self.offset_h -= 1
				if event.type == KEYDOWN and (event.key == K_UP or event.key == K_z):
					self.offset_h += 1
				if event.type == KEYDOWN and (event.key == K_RIGHT or event.key == K_d):
					self.offset_v -= 1
				if event.type == KEYDOWN and (event.key == K_LEFT or event.key == K_q):
					self.offset_v += 1
			b = timer() - a
			listes_frame.append(b)

class simulation(Thread):
	def __init__(self, sizeX, sizeY, option):
		self.map = Map(option)
		self.map.generate()

if __name__ == "__main__":
	option1 = option.loadFromFile("options")
	a = simulation(30, 30, option1)
	a.map.show()