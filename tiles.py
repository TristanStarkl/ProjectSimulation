import random
import pygame

def rotation_random():
	a = [0, 90, 180, 270]
	return (random.choice(a))

class tiles():
	def __init__(self, X, Y, sizeX, j):
		self.tileName = ""
		self.passable = True
		self.size = 3000
		self.ores = []
		self.X = X
		self.Y = Y
		self.radius = 30
		self.j = j
		self.ForestSize = 0
		self.MountainSize = 0
		self.FieldSize = 0
		self.img = pygame.image.load("tiles/void.png").convert()
		self.img_normal = pygame.image.load("tiles/void.png").convert()
		self.img_destroyed = pygame.image.load("tiles/void.png").convert()
		self.img_being_destroyed = pygame.image.load("tiles/void.png").convert()
		self.typeOfMaterial = ["none"]
		self.isExtension = False

	def getForestSize(self):
		return (self.ForestSize)

	def getMountainSize(self):
		return (self.MountainSize)

	def getFieldSize(self):
		return (self.FieldSize)

	def getName(self):
		return (self.tileName)

	def onClick(self):
		print(self.X, self.Y, "j = ", round(self.j, 3))

class thevoid(tiles):
	def __init__(self, window, X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "void"
		self.passable = False
		self.img = pygame.image.load("tiles/void.png").convert()
		self.j = j



class sea(tiles):
	def __init__(self, window, X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "sea"
		self.passable = False
		self.img = pygame.image.load("tiles/sea.png").convert()
		self.j = j
		self.typeOfMaterial = ["water"]


class reef(tiles):
	def __init__(self, window, X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "reef"
		self.passable = False
		self.img = pygame.image.load("tiles/reef.png").convert()
		self.j = j
		self.typeOfMaterial = ["water", "stone"]

class island(tiles):
	def __init__(self, window, X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "island"
		self.passable = True
		x = random.randint(0, 100)
		if (x < 34):
			self.img = pygame.image.load("tiles/island.png").convert()
		elif (x < 67):
			self.img = pygame.image.load("tiles/island2.png").convert()
		else:
			self.img = pygame.image.load("tiles/island3.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.ForestSize = random.randint(15, 50)
		self.MountainSize = random.randint(15, 50)
		self.FieldSize = 100 - self.ForestSize - self.MountainSize
		self.typeOfMaterial = ["wood", "stone"]

class island_ocean(tiles):
	def __init__(self, window, X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "island_ocean"
		self.passable = True
		x = random.randint(0, 100)
		if (x < 34):
			self.img = pygame.image.load("tiles/island_ocean.png").convert()
		elif (x < 67):
			self.img = pygame.image.load("tiles/island_ocean2.png").convert()
		else:
			self.img = pygame.image.load("tiles/island_ocean3.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.ForestSize = random.randint(15, 50)
		self.MountainSize = random.randint(15, 50)
		self.FieldSize = 100 - self.ForestSize - self.MountainSize
		self.typeOfMaterial = ["wood", "stone"]


class ocean(tiles):
	def __init__(self, window, X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "ocean"
		self.passable = False
		self.img = pygame.image.load("tiles/ocean.png").convert()
		self.j = j
		self.typeOfMaterial = ["water"]


class iceberg(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "iceberg"
		self.passable = False
		self.img = pygame.image.load("tiles/iceberg.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["water", "ice"]

class colline(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "colline"
		self.passable = True
		self.ForestSize = random.randint(15, 50)
		self.FieldSize = 100 - self.ForestSize
		self.img = pygame.image.load("tiles/colline.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["stone"]


class forest(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "forest"
		self.ForestSize = random.randint(80, 100)
		self.FieldSize = 100 - self.ForestSize
		self.img = pygame.image.load("tiles/forest.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.img_normal = pygame.image.load("tiles/forest.png").convert()
		self.img_destroyed = pygame.image.load("tiles/burned_forest.png").convert()
		self.img_being_destroyed = pygame.image.load("tiles/burning_forest.png").convert()
		self.j = j
		self.typeOfMaterial = ["wood"]

class jungle(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "jungle"
		self.ForestSize = random.randint(80, 100)
		self.FieldSize = 100 - self.ForestSize
		self.img = pygame.image.load("tiles/jungle.png").convert()
		x = random.randint(0, 100)
		if (x < 10):
			self.img = pygame.image.load("tiles/jungle2.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["water", "wood"]

class tundra(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "tundra"
		self.ForestSize = random.randint(80, 100)
		self.FieldSize = 100 - self.ForestSize
		self.img = pygame.image.load("tiles/tundra.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["land", "ice"]

class taiga(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "taiga"
		self.ForestSize = random.randint(80, 100)
		self.FieldSize = 100 - self.ForestSize
		self.img = pygame.image.load("tiles/taiga.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["wood", "ice"]

class swamp(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "swamp"
		self.ForestSize = random.randint(0, 10)
		self.FieldSize = random.randint(0, 10)
		self.img = pygame.image.load("tiles/marais.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["water", "wood"]

class desert(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "desert"
		self.ForestSize = 0
		self.FieldSize = 100 - self.ForestSize
		self.color = "#"
		self.img = pygame.image.load("tiles/desert.png").convert()
		x = random.randint(0, 100)
		if (x < 2):
			self.img = pygame.image.load("tiles/oasis.png").convert()
		self.j = j
		self.typeOfMaterial = ["desert"]

class savanah(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "savanah"
		self.ForestSize = random.randint(0, 10)
		self.FieldSize = 100 - self.ForestSize
		self.color = "#"
		self.img = pygame.image.load("tiles/savanah.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["wood", "desert"]



class lake(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "lake"
		self.ForestSize = random.randint(0, 20)
		self.FieldSize = 100 - self.ForestSize
		self.color = "#"
		self.img = pygame.image.load("tiles/lac.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["water"]

class land(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "land"
		self.ForestSize = random.randint(0, 20)
		self.FieldSize = 100 - self.ForestSize
		self.color = "#"
		self.img = pygame.image.load("tiles/land.png").convert()
		self.img_normal = pygame.image.load("tiles/land.png").convert()
		self.img_destroyed = pygame.image.load("tiles/burned_land.png").convert()
		self.img_being_destroyed = pygame.image.load("tiles/burning_forest.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["land"]

class colline_enneige(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "colline_enneige"
		self.ForestSize = 0
		self._fieldSize = 10
		self.img = pygame.image.load("tiles/colline_neige.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["stone", "ice"]

class mountain(tiles):
	def __init__(self, window,  X, Y, sizeX, j):
		tiles.__init__(self,  X, Y, sizeX, j)
		self.tileName = "mountain"
		self.ForestSize = 0
		self.passable = False
		self.img = pygame.image.load("tiles/mountain.png").convert()
		self.img = pygame.transform.rotate(self.img, rotation_random())
		self.j = j
		self.typeOfMaterial = ["stone", "ice"]
