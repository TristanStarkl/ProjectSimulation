#from jobs import *
#from humans import *
import random
import time
import threading
from threading import Thread, RLock
import pygame
from extensions_des_villes import *
#from jobs import *
#lock = RLock()

import random

######################### JOBS


class jobs():
	def __init__(self):
		self._agemini = 0
		self._chanceReproduce = 0
		self._name = ""

	def work(self, efficiency):
		return (0)

	def getChanceReproduce(self):
		return (_chanceReproduce)

	def getType(self):
		return (self._name)

class baby(jobs):
	def __init__(self):
		self._name = "baby"
		self._chanceReproduce = -100

class Unemployed(jobs):
	def __init__(self):
		self.name = "unemployed"


class Pregnant(jobs):
	def __init__(self):
		self._name = "pregnant"
		self._chanceReproduce = -100
		self.i = 0

	def work(self, efficiency):
		self.i += 1
		return (self.i)

	def birth(self, efficiency):
		return(__humans__(0, efficiency, baby()))

class Mother(jobs):
	def __init__(self):
		self._name = "mother"
		self._chanceReproduce = -100
		self.i = 0

	def work(self, efficiency):
		self.i += 1
		if (self._chanceReproduce  < 25):
			self._chanceReproduce += 25
		return (self.i)

class Hunter(jobs):
	def __init__(self):
		self._agemini = 12
		self._name = "hunter"
		self._chanceReproduce = 15

	def work(self, efficiency):
		if not (efficiency < 0):
			luckDying = 5 - efficiency
		else:
			luckDying = 5 + efficiency
		if (luckDying < 1):
			luckDying = 1
		i = random.randint(1, 400)
		j = random.randint(0, 50)
		if (i <= luckDying):
			return (-100)
		return (efficiency + j)


class Farmer(jobs):
	def __init__(self):
		self._agemini = 12
		self._name = "farmer"
		self._chanceReproduce = 20

	def work(self, efficiency):
		return (efficiency * 3.35)

class Fisherman(jobs):
	def __init__(self):
		self._agemini = 12
		self._name = "fisherman"
		self._chanceReproduce = 10
		self.nbMonths = 0
		self.nbAway = 0

	def work(self, efficiency):
		if (self.nbAway == 0):
			self.nbAway = random.randint(1, 4)
			self.nbMonths += 1
			self._chanceReproduce = 0

			return (-2)
		elif (self.nbMonths == self.nbAway):
			nbFood = random.randint(3, 20) + efficiency - self.nbAway
			self.nbAway = -1
			self.nbMonths = 0
			self._chanceReproduce = 10

			return (nbFood)
		elif (self.nbAway == -1):
			self.nbAway += 1
			return (-1)
		else:
			self.nbMonths += 1
			return (-100)

class Breeder(jobs):
	def __init__(self):
		self._agemini = 12
		self._name = "breeder"
		self._chanceReproduce = 10

	def work(self, efficiency):
		return (efficiency * 1.65)


class Gatherer(jobs):
	def __init__(self):
		self._agemini = 12
		self._name = "gatherer"
		self._chanceReproduce = 10

	def work(self, efficiency):
		return (efficiency * 1.65)

class Minor(jobs):
	def __init__(self):
		self._chanceDying = 10
		self._name = "minor"
		self._chanceReproduce = 15

	def work(self, efficiency, chanceDying=0):
		i = random.randint(0, 1000)
		self._chanceDying += chanceDying
		if (i <= self._chanceDying):
			return (-1)
		if (i < efficiency):
			return (0)
		return (1)

class Researcher(jobs):
	def __init__(self):
		self._agemini = 12
		self.workProduced = ["hunting", "research", "farming", "medical", "forest", "unusableSpace", "conservation"]
		self.luckEfficiency = 5
		self.quantity = 1
		self._name = "researcher"
		self._chanceReproduce = 5

	def work(self, efficiency):
		i = random.randint(0,100)
		if ((i + efficiency) < self.luckEfficiency):
			j = random.randint(0, len(self.workProduced) - 1)
			choice = self.workProduced[j]
			a = [self.quantity + efficiency, choice]
			return (a)
		else:
			return (None)

class Craftmens(jobs):
	def __init__(self):
		self._agemini = 12
		self.workProduced = 1
		self.foodConsumed = 20
		self._name = "craftmen"
		self._chanceReproduce = 10

	def work(self, quantityOre):
		if (quantityOre > 10):
			i = random.randint(-100, 10)
			if (i < 0):
				i = 0
			return (1 + i)
		return (0)

class Blacksmith(jobs):
	def __init__(self):
		self._name = "blacksmith"
		self._chanceReproduce = 15

	def work(self, quantity):
		if (quantity > 10):
			i = random.randint(-100, 10)
			if (i < 0):
				i = 0
			return (1 + i)
		return (0)

class Soldier(jobs):
	def __init__(self):
		self._name = "soldier"
		self._chanceReproduce = 2

class Trainer(jobs):
	def __init__(self):
		self._name = "trainer"

	def work(self):
		return (1)

class Teacher(jobs):
	def __init__(self):
		self._name = "teacher"

	def work(self):
		return (1)

######################### HUMANS

class __humans__():
	def __init__(self,age, city, job):
		self._age = age
		self._sex = random.choices(["male", "female"])
		self._sex = self._sex[0]
		self._educated = 0
		self._city = city
		self._job = job
		self._oldJob = None
		self._pv = 10
		self._maxpv = 10

	def getGender(self):
		return (self._sex)

	def getPregnant(self):
		self._oldJob = self._job
		self._job = Pregnant()

	def beMother(self):
		self._oldJob = self._job
		self._job = Mother()

	def stopBeingMother(self):
		self._job = self._oldJob

	def eat(self):
		if (self._city.getFood() > 1):
			self._city.removeFood(1)
			self.heal(1)
		else:
			self.heal(-5)

	def chooseJob(self):
		try:
			placeHunter = (self._city._forestSize * self._city._huntingEfficiency) - self._city.Hunter[-1] - ((self._city.Gatherers[-1] + 1) / 2)  #Il n'y a plus de place pour des hunter
			placeHunter = placeHunter * self._city.trending_food()
		except Exception as E:
			print("There as been an exception in placeHunter!, ", E)
			placeHunter = 0
		if (placeHunter < 0):
			placeHunter = 0
		#----------------
		try:
			placeFisherman = (self._city._waterUsable * self._city._fishingEfficiency) - self._city.Fishermans[-1]  #Il n'y a plus de place pour des Fisherman
			placeFisherman = placeFisherman * self._city.trending_food()
		except Exception as E:
			print("There as been an exception in placeFisherman!, ", E)
			placeFisherman = 0
		if (placeFisherman < 0):
			placeFisherman = 0
		#----------------
		try:
			placeGatherer = (self._city._forestSize) - self._city.Hunter[-1] - ((self._city.Gatherers[-1] + 1) / 2)  #Il n'y a plus de place pour des placeGatherer
			placeGatherer = placeGatherer * self._city.trending_food()
		except Exception as E:
			print("There as been an exception in placeGatherer!, ", E)
			placeGatherer = 0
		if (placeGatherer < 0):
			placeGatherer = 0

		#----------------
		try:
			placeFarmer = (self._city._fieldsSize * self._city._farmingEfficiency) - self._city.Farmers[-1]  #Il n'y a plus de place pour des placeFarmer
			placeFarmer = placeFarmer * self._city.trending_food()
		except Exception as E:
			print("There as been an exception in farming!, ", E)
			placeFarmer = 0
		if (placeFarmer < 0):
			placeFarmer = 0
		#----------------
		try:
			placeBreeder = (self._city._liveStockSize * self._city._liveStockEfficiency) - self._city.Breeder[-1]  #Il n'y a plus de place pour des placeBreeder
			placeBreeder = placeBreeder * self._city.trending_food()
		except Exception as E:
			print("There as been an exception in placeBreeder!, ", E)
			placeBreeder = 0
		if (placeBreeder < 0):
			placeBreeder = 0
		#----------------
		try:
			placeResarcher = (self._city._labSpace) - self._city.Researcher[-1]  #Il n'y a plus de place pour des placeMinor
		except Exception as E:
			print("There as been an exception in placeResarcher!, ", E)
			placeResarcher = 0
		if (placeResarcher < 0):
			placeResarcher = 0
		#----------------
		try:
			placeMinor = (self._city._mountainSize) - self._city.Miner[-1]  #Il n'y a plus de place pour des placeMinor
		except Exception as E:
			print("There as been an exception in placeMinor!, ", E)
			placeMinor = 0
		if (placeMinor < 0):
			placeMinor = 0
		#----------------
		try:
			placeCraftmens = (self._city._artisanSpace) - self._city.Craftmens[-1]  #Il n'y a plus de place pour des placeCraftmens
		except Exception as E:
			print("There as been an exception in placeCraftmens!, ", E)
			placeCraftmens = 0
		if (placeCraftmens < 0):
			placeCraftmens = 0
		#----------------
		try:
			placeBlacksmith = (self._city._artisanSpace) - self._city.Blacksmith[-1]  #Il n'y a plus de place pour des placeBlacksmith
		except Exception as E:
			print("There as been an exception in placeBlacksmith!, ", E)
			placeBlacksmith = 0
		if (placeBlacksmith < 0):
			placeBlacksmith = 0
		#----------------
		try:
			placeSoldier = (self._city._soldierSpace) - self._city.Soldier[-1]  #Il n'y a plus de place pour des placeSoldier
		except Exception as E:
			print("There as been an exception in placeSoldier!, ", E)
			placeSoldier = 0
		if (placeSoldier < 0):
			placeSoldier = 0
		total = placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + placeMinor + placeCraftmens + placeBlacksmith + placeSoldier
		print(total, placeHunter , placeFisherman , placeGatherer , placeFarmer , placeBreeder , placeResarcher , placeMinor, placeCraftmens , placeBlacksmith , placeSoldier)
		if total <= 0: # On a plus de place nulle part!
			print("Je suis devenu un chômeur!")
			self._job = Unemployed()
			return
		i = random.randint(0, round(total))
		if (i < placeHunter):
			self._job = Hunter()
			print("Je suis devenu un chasseur!")
			return
		elif (i < (placeHunter + placeFisherman)):
			self._job = Fisherman()
			print("Je suis devenu un Fisherman!")
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer)):
			self._job = Gatherer()
			print("Je suis devenu un Gatherer!")
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer)):
			self._job = Farmer()
			print("Je suis devenu un Farmer!")
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder)):
			self._job = Breeder()
			print("Je suis devenu un Breeder!")
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher)):
			self._job = Researcher()
			print("Je suis devenu un Researcher!")
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + 
		placeMinor)):
			self._job = Minor()
			print("Je suis devenu un Minor!")
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + 
		placeMinor + placeCraftmens)):
			self._job = Craftmens()
			print("Je suis devenu un Craftmens!")
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + 
		placeMinor + placeCraftmens + placeBlacksmith)):
			self._job = Blacksmith()
			print("Je suis devenu un Blacksmith!")
			return
		elif (i <= total):
			print("Je suis devenu un Soldier!")
			self.jobs = Soldier()
				
	def heal(self, pv):
		self._pv += pv
		if (self._pv >= self._maxpv):
			self._pv = self._maxpv

	def getPv(self):
		return (self._pv)

	def getJob(self):
		return (self._job)

	def getAge(self):
		return (self._age)

	def age(self, nb):
		self._age += nb

	def setType(self, t):
		self._type = t

	def work(self, efficiency):
		if (self._job is not None):
			return (self._job.work(efficiency))


######################### CITY


class save_city():
	def __init__(self, _size, _populationSize , name, _nbYears, j = 0, _urbanisation = 0, _forestSize = 0, _mountainSize = 0,
	 _fieldsSize = 0, _citiesSpace = 0, _extensions = [], _farmingEfficiency = 1, _huntingEfficiency = 1, _researchEfficiency = 1, 
	 _medicalEfficiency = 1, _quantityFood = 0, _FoodWhenResearch = 10, _quantityBaby = 23, _conservationEfficiency = 1, 
	 hasSeaAccess = False, wealth = 0, _quantityOre = 0, _quantityHorse = 0, _quantityTools = 0, _historyHorse = [], historyOre = [],
	  historyWealth = [], FoodStockpile = [], Deaths = [], Fishermans = [], Babies = [], Farmers = [], Hunter = [], Pregnant = [], 
	  Mother = [], Researcher = [], Craftmens = [], Gatherers = [], StockBreeder = [], Miner = [], Soldier = [], Doctor = [], Teacher = [], 
	  Blacksmith = [], Trainer = [], OldAge = [], HunterDied = [], historyFarmingEfficiency = [], historyHuntingEfficiency = [], 
	  historyResearchEfficiency = [], historyMedicalEfficiency = [], PopulationControl = [], Heal = [], populations = []):
		self._size = _size
		self._populationSize = _populationSize
		self.name = name
		self._nbYears = _nbYears
		self.j = j
		self._urbanisation = _urbanisation
		self._forestSize = _forestSize
		self._mountainSize = _mountainSize
		self._fieldsSize = _fieldsSize
		self._citiesSpace = _citiesSpace
		self._extensions = _extensions
		self._farmingEfficiency = _farmingEfficiency
		self._huntingEfficiency = _huntingEfficiency
		self._researchEfficiency = _researchEfficiency
		self._medicalEfficiency = _medicalEfficiency
		if (_quantityFood == 0):
			self._quantityFood = _populationSize * 20
		self._FoodWhenResearch = _FoodWhenResearch
		self._quantityBaby = _quantityBaby
		self._conservationEfficiency = _conservationEfficiency
		self.hasSeaAccess = hasSeaAccess
		self.wealth = wealth
		self._quantityOre = _quantityOre
		self._quantityHorse = _quantityHorse
		self._quantityTools = _quantityTools
		#history
		self._historyHorse = _historyHorse
		self.historyOre = historyOre
		self.historyWealth = historyWealth
		self.FoodStockpile = FoodStockpile
		self.Deaths = Deaths
		self.Fishermans = Fishermans
		self.Babies = Babies
		self.Farmers = Farmers
		self.Hunter = Hunter
		self.Pregnant = Pregnant
		self.Mother = Mother
		self.Researcher = Researcher
		self.Craftmens = Craftmens
		self.Gatherers = Gatherers
		self.StockBreeder = StockBreeder
		self.Miner = Miner
		self.Soldier = Soldier
		self.Doctor = Doctor
		self.Teacher = Teacher
		self.Blacksmith = Blacksmith
		self.Trainer = Trainer
		self.OldAge = OldAge
		self.HunterDied = HunterDied
		self.historyFarmingEfficiency = historyFarmingEfficiency
		self.historyHuntingEfficiency = historyHuntingEfficiency
		self.historyResearchEfficiency = historyResearchEfficiency
		self.historyMedicalEfficiency = historyMedicalEfficiency
		self.PopulationControl = PopulationControl
		self.Heal = Heal
		#
		self.populations = populations



class cities(Thread):

	def __init__(self, mape, _size, _populationSize, name, _nbYears, window, j = 0, _urbanisation = 0, _forestSize = 0, _mountainSize = 0,
	 _fieldsSize = 0, _citiesSpace = 0, _extensions = [], _farmingEfficiency = 1, _huntingEfficiency = 1, _researchEfficiency = 1, 
	 _medicalEfficiency = 1, _quantityFood = 0, _FoodWhenResearch = 10, _quantityBaby = 23, _conservationEfficiency = 1, 
	 hasSeaAccess = False, wealth = 0, _quantityOre = 0, _quantityHorse = 0, _quantityTools = 0, _historyHorse = [0], historyOre = [0],
	  historyWealth = [0], FoodStockpile = [], Deaths = [], Fishermans = [0], Babies = [0], Farmers = [0], Hunter = [], Pregnant = [0], 
	  Mother = [0], Researcher = [0], Craftmens = [0], Gatherers = [], StockBreeder = [0], Miner = [0], Soldier = [0], Doctor = [0], Teacher = [0], 
	  Blacksmith = [0], Trainer = [0], OldAge = [0], HunterDied = [0], historyFarmingEfficiency = [0], historyHuntingEfficiency = [0], 
	  historyResearchEfficiency = [0], historyMedicalEfficiency = [0], PopulationControl = [0], Heal = [0], populations = [], ):
		Thread.__init__(self)

		self._size = _size
		self._populationSize = _populationSize
		self.name = name
		self._nbYears = _nbYears
		self.paused = False

		self.map = mape 
		self.j = j

		# DEFINITIONS DES EMPLACEMENTS
		self._urbanisation = 500
		self._labSpace = 40
		self._forestSize = _forestSize
		self._mountainSize = _mountainSize
		self._fieldsSize = _fieldsSize
		self._extensions = _extensions
		self._waterUsable = 10
		self._liveStockSize = 10
		self._artisanSpace = 10
		self._soldierSpace = 10


		# EFFICIENCIES 
		self._liveStockEfficiency = 1
		self._farmingEfficiency = _farmingEfficiency
		self._huntingEfficiency = _huntingEfficiency
		self._researchEfficiency = _researchEfficiency
		self._medicalEfficiency = _medicalEfficiency
		self._fishingEfficiency = 1

		if (_quantityFood == 0):
			self._quantityFood = _populationSize * 20

		self._FoodWhenResearch = _FoodWhenResearch
		self._conservationEfficiency = _conservationEfficiency
		self.hasSeaAccess = hasSeaAccess
		self.wealth = wealth
		self._quantityOre = _quantityOre
		self._quantityHorse = _quantityHorse
		self._quantityTools = _quantityTools

		# HISTORY EFFICIENCY
		self.historyFarmingEfficiency = historyFarmingEfficiency
		self.historyHuntingEfficiency = historyHuntingEfficiency
		self.historyResearchEfficiency = historyResearchEfficiency
		self.historyMedicalEfficiency = historyMedicalEfficiency

		#history
		self._historyHorse = _historyHorse
		self.historyOre = historyOre
		self.historyWealth = historyWealth


		self.FoodStockpile = FoodStockpile


		self.totalDeath	= []
		self.Babies = Babies
		self.Deaths = Deaths
		self.OldAge = OldAge
		self.Pregnant = Pregnant
		self.Mother = Mother
		self._quantityBaby = _quantityBaby

		# CONTROLE DES JOBS
		self.Hunter = Hunter
		self.Fishermans = Fishermans
		self.Gatherers = Gatherers
		self.Farmers = Farmers
		self.Breeder = []
		self.Researcher = Researcher
		self.Miner = Miner
		self.Craftmens = Craftmens
		self.Blacksmith = Blacksmith
		self.Soldier = Soldier


		self.Trainer = Trainer


		self.newPregnants = []
		self.newMothers = []
		self.newBabiess = []

		self.HunterDied = HunterDied
		self.PopulationControl = PopulationControl
		self.Heal = Heal
		#
		self.populations = populations
		self.passable = False



		self.isOnDesert = False
		self.tileName = "City {}".format(self.name)
		self.img_village = pygame.image.load("tiles/village.png").convert()
		self.img_village = pygame.transform.rotate(self.img_village, random.choice([0, 90, 180, 270]))
		self.img_city = pygame.image.load("tiles/city.png").convert()
		self.img_city = pygame.transform.rotate(self.img_city, random.choice([0, 90, 180, 270]))
		self.img_motte_castrale = pygame.image.load("tiles/city.png").convert()
		self.img_motte_castrale = pygame.transform.rotate(self.img_city, random.choice([0, 90, 180, 270]))
		self.img_village_d = pygame.image.load("tiles/village_d.png").convert()
		self.img_village_d = pygame.transform.rotate(self.img_village, random.choice([0, 90, 180, 270]))
		self.img_city_d = pygame.image.load("tiles/city_d.png").convert()
		self.img_city_d = pygame.transform.rotate(self.img_city, random.choice([0, 90, 180, 270]))
		self.img_motte_castrale_d = pygame.image.load("tiles/city.png").convert()
		self.img_motte_castrale_d = pygame.transform.rotate(self.img_city, random.choice([0, 90, 180, 270]))
		self.hasLaunched = False
		self.window = window
		self.paused = False
		#self.pause_cond = threading.Condition(threading.Lock())
		self.ended = False
		self.turnNumber = 0
		self.img = self.img_village

	def kill_city(self):
		self.ended = True
		print("Je viens de tuer la cité!")

	def launch(self):
		if (self.hasLaunched == False):
			self.start()
			self.hasLaunched = True
		else:
			self.graph()

	def trending_food(self):
		try:
			before1 = self.FoodStockpile[-3]
		except IndexError:
			try:
				before2 = self.FoodStockpile[-2]
			except IndexError:
				return (1000)
			after = self.FoodStockpile[-1]
			moyenne = before2 / after
			return moyenne
		before2 = self.FoodStockpile[-2]
		after = self.FoodStockpile[-1]
		moyenne1 = (before1 + 1)/ (before2 + 1)
		moyenne2 = (before2 + 1)  / (after + 1)
		moyenne = moyenne1 / moyenne2
		return moyenne


	def placeOnMap(self, map, sizeX, width):
		x = random.randint(2, sizeX-2)
		y = random.randint(2, width-2)
		tiles = map.getTile(x, y)
		choixValide = False
		while(choixValide == False):
			if (tiles == 0):
				x = random.randint(0, sizeX)
				y = random.randint(0, width)
				tiles = map.getTile(x, y)
			elif (tiles.passable == False):
				x = random.randint(0, sizeX)
				y = random.randint(0, width)
				tiles = map.getTile(x, y)
			else:
				choixValide = True

		self.X = x
		self.Y = y
		print(tiles.tileName)
		if (tiles.tileName == "desert"):
			self.img = self.img_city_d
			self.isOnDesert = True
		self._forestSize = tiles.getForestSize()
		self._mountainSize = tiles.getMountainSize()
		self._fieldsSize = tiles.getFieldSize()
		self.j = tiles.j
		map.placeCity(self, x, y)
		self.hasSeaAccess = map.hasSeaAccess(x, y)

	def initializePopulation(self):
		print("forest size= ", self._forestSize, "field size = ", self._fieldsSize)
		nbFarmers = int((self._fieldsSize / (self._forestSize + self._fieldsSize)) * self._populationSize / 2)
		for i in range(nbFarmers):
			a = __humans__(random.randint(12, 25), self, Gatherer())
			self.populations.append(a)
			self.Gatherers.append(nbFarmers)

		nbHunter = self._populationSize - nbFarmers
		for i in range(nbHunter):
			a = __humans__(random.randint(12, 25), self, Hunter())
			self.populations.append(a)
			self.Hunter.append(nbHunter)

	def getFood(self):
		return (self._quantityFood)

	def getPopulationSize(self):
		return (self._populationSize)

	def removeFood(self, quantity):
		self._quantityFood -= quantity

	def rotFood(self):
		try:
			a = self._quantityFood / (self._populationSize * 5)
		except ZeroDivisionError:
			a = 0
		self._quantityFood *= ((95 + self._conservationEfficiency - (a)) / 100)

	def life(self):
		if (self.ended):
			print("La cité est morte!")
			return (True)
		if (self._populationSize != 0):
			return (True)
		return (False)

	def addBaby(baby):
		self.populations.append(baby)

	def getName(self):
		return (self.name)

	def generateGraph(self, nbyears):
		from matplotlib import pyplot, dates
		from csv import reader
		import os

		pyplot.subplot(331)
		pyplot.plot(range(len(self.Farmers)), self.Farmers, "r")
		pyplot.title("Number of farmers (G = green, F = red)")
		pyplot.plot(range(len(self.Gatherers)), self.Gatherers, "g")

		pyplot.subplot(332)
		pyplot.plot(range(len(self.Hunter)), self.Hunter, "r")
		pyplot.title("Number of hunter")
		pyplot.plot(range(len(self.Fishermans)), self.Fishermans, "g")

		pyplot.subplot(333)
		pyplot.plot(range(len(self.Pregnant)), self.Pregnant, "r")
		pyplot.plot(range(len(self.Babies)), self.Babies, "g")
		pyplot.plot(range(len(self.Mother)), self.Mother, "b")

		pyplot.title("{} : Pregnant R, Babies G, Mother, B: population totale {}".format(self.name, str(self._populationSize)))
		pyplot.ylabel("Number of pregnant")

		pyplot.subplot(334)
		pyplot.plot(range(len(self.historyMedicalEfficiency)), self.historyMedicalEfficiency, "r")
		pyplot.title("Efficiency of the jobs")
		pyplot.plot(range(len(self.historyFarmingEfficiency)), self.historyFarmingEfficiency, "g")
		pyplot.plot(range(len(self.historyResearchEfficiency)), self.historyResearchEfficiency, "b")
		pyplot.plot(range(len(self.historyHuntingEfficiency)), self.historyHuntingEfficiency, "r--")
		
		pyplot.subplot(336)
		pyplot.plot(range(len(self.Researcher)), self.Researcher)
		pyplot.title("Number of researcher")
		pyplot.ylabel("Number of researcher")

		pyplot.subplot(337)
		pyplot.plot(range(len(self.Babies)), self.Babies)
		pyplot.title("Number of Kids")
		pyplot.ylabel("Number of Kids")

		pyplot.subplot(338)
		pyplot.plot(range(len(self.FoodStockpile)), self.FoodStockpile)
		pyplot.title("Number of food ")
		pyplot.ylabel("Number of food")
		
		pyplot.subplot(335)
		pyplot.plot(range(len(self.PopulationControl)), self.PopulationControl)
		pyplot.title("Number of pop for the great city of {}".format(self.name))
		pyplot.ylabel("Population")
		pyplot.plot(range(len(self.Babies)), self.Babies, "r--")
		pyplot.plot(range(len(self.Farmers)), self.Farmers, "g--")
		pyplot.plot(range(len(self.Hunter)), self.Hunter,  "b--")


		pyplot.subplot(339)

		pyplot.plot(range(len(self.HunterDied)), self.HunterDied, "r")
		pyplot.plot(range(len(self.totalDeath)), self.totalDeath, "r--")
		pyplot.title("Deaths per year")
		pyplot.ylabel("Deaths")
		pyplot.plot(range(len(self.OldAge)), self.OldAge, "g")
		pyplot.plot(range(len(self.Heal)), self.Heal, "b")

		pyplot.show()

	def get_coordonnes_extensions(self):
		a = [[self.X, self.Y]]
		for ext in self._extensions:
			a.append([ext.X, ext.Y])
		return a

	def get_better_place_extension(self, liste_coordonnees, typeExtension, biome2=None, typeMaterial=None):
		for coordonnees in liste_coordonnees:
			#coordonnees = [X, Y]
			cells = self.map.getAdjacentCells(coordonnees[0], coordonnees[1])
			for cell in cells:
				if typeExtension == None:
					if typeMaterial == None:
						if cell.passable == True:
							return cell.X, cell.Y
					else:
						for material in cell.typeOfMaterial:
							if material == typeMaterial:
								if cell.isExtension == False:
									return cell.X, cell.Y
				elif cell.tileName == typeExtension:
					return cell.X, cell.Y
			for cell in cells:
				if cell.tileName == biome2:
					return cell.X, cell.Y
		return -1,-1

	def addSpace(self):
		last_extension = self._extensions[-1]
		self._urbanisation += last_extension._urbanisation
		self._forestSize += last_extension._forestSize
		self._mountainSize += last_extension._mountainSize
		self._fieldsSize += last_extension._fieldsSize
		self._waterUsable += last_extension._waterSpace
		self._labSpace += last_extension._labSpace
		self._liveStockSize += last_extension._liveStockSize
		self._artisanSpace += last_extension._artisanSpace
		self._soldierSpace += last_extension._soldierSpace




	def create_extensions(self, typeExtension):
		listes_coordonnees_extensions = self.get_coordonnes_extensions()
		if (typeExtension == "docks"):
			x, y = self.get_better_place_extension(listes_coordonnees_extensions, "sea")
		elif (typeExtension == "verger"):
			x, y = self.get_better_place_extension(listes_coordonnees_extensions, "forest")
			if (x == -1 and y == -1):
				x, y = self.get_better_place_extension(listes_coordonnees_extensions, "jungle", biome2="taiga")
		elif (typeExtension == "champs"):
			x, y = self.get_better_place_extension(listes_coordonnees_extensions, None, typeMaterial="land")
		elif(typeExtension == "logement"):
			x, y = self.get_better_place_extension(listes_coordonnees_extensions, None)

		if (x != -1 and y != -1):
			if (typeExtension == "docks"):
				self._extensions.append(dock(x, y, self, 250))
				self.map.map[x][y] = self._extensions[-1]
				print("J'ai créé une extension de dock!")
			elif (typeExtension == "verger"):
				self._extensions.append(orchard(x, y, self, 250))
				print("J'ai créé une extension de verger!")
				self.map.map[x][y] = self._extensions[-1]
			elif (typeExtension == "champs"):
				self._extensions.append(farmland(x, y, self, 250))
				print("J'ai créé une extension de champs!")
				self.map.map[x][y] = self._extensions[-1]
			elif (typeExtension == "logement"):
				self._extensions.append(logement(x, y, self, 500, self.map.map[x][y].typeOfMaterial))
				self.map.map[x][y] = self._extensions[-1]
			self.addSpace()
		else:
			print("Aucune place disponible pour ", typeExtension)


	def turn(self):
		self.turnNumber += 1
		self.oldFood = self._quantityFood
		nbDeath = 0
		nbOldAge = 0
		nbHeal = 0
		nbHunterDied = 0
		nbMinorDead = 0

		nbMother = 0
		nbPregnant = 0
		nbBabies = 0

		nbHunter = 0
		nbFisherman = 0
		nbGatherer = 0
		nbFarmers = 0
		nbBreeder = 0
		nbResearcher = 0
		nbMinor = 0
		nbCraftmens = 0
		nbBlacksmith = 0
		nbSoldier = 0

		newMother = 0
		newBabies = 0
		newPregnant = 0

		if (self._populationSize > 250 and self.isOnDesert == False):
			self.img = self.img_city
		elif self._populationSize < 250 and self.isOnDesert == False:
			self.img = self.img_village
		if (self._populationSize > 250 and self.isOnDesert == True):
			self.img = self.img_city_d
		elif self._populationSize < 250 and self.isOnDesert == True:
			self.img = self.img_village_d
		if (self._populationSize > self._urbanisation):
			self.create_extensions("logement")

		try:
			x = (self._forestSize * self._huntingEfficiency) - self.Hunter[-1] - (self.Gatherers[-1] / 2) # Hunter
			if (x < 0 and self._huntingEfficiency > 0):
				self.create_extensions("verger")
		except Exception as E:
			print(E)
			#print(self.Hunter, self.Gatherers)
		try:
			y = (((self._fieldsSize * self._farmingEfficiency) - self.Farmers[-1]  - (self.Gatherers[-1] / 2))) # Farming
			if (y < 0 and self._farmingEfficiency > 0):
				self.create_extensions("champs")
		except:
			pass
		try:
			z = (((self._waterUsable * self._fishingEfficiency )- self.Fishermans[-1] )) # poiscaille
			if (z < 0 and self._fishingEfficiency > 0):
				self.create_extensions("docks")
		except :
			pass
		for human in self.populations:
			human.age(1)
			dead = False

			if (human.getJob().getType() == "gatherer"):
				self._quantityFood += human.work((self._huntingEfficiency + self._farmingEfficiency) / 2)
				nbGatherer += 1

			elif (human.getJob().getType() == "minor"):
				i = human.work(self._mountainSize)
				if (i == -1):
					self.populations.remove(human)
					nbDeath	 += 1
					del human
					nbMinorDead += 1
				else:
					self._quantityOre += i
					nbMinor += 1

			elif (human.getJob().getType() == "blacksmith"):
				i = human.work(self._quantityOre)
				self._quantityTools += i
				if (i != 0):
					self._quantityOre -= 10
				nbBlacksmith += 1


			elif (human.getJob().getType() == "researcher"):
				nbResearcher += 1
				self._quantityFood -= self._FoodWhenResearch
				a = human.work(self._researchEfficiency)
				if (a != None):
					quantity, typeOfResearch = a[0], a[1]
					if (typeOfResearch == "hunting"):
						self._huntingEfficiency += quantity
						print("Hunting efficiency: ", self._huntingEfficiency)
						if (self._huntingEfficiency > 5):
							self._huntingEfficiency = 5
					elif (typeOfResearch == "research"):
						self._researchEfficiency += quantity
						print("Research efficiency: ", self._researchEfficiency)
						if (self._FoodWhenResearch > 2 ):
							self._FoodWhenResearch -= 1
					elif (typeOfResearch == "farming"):
						self._farmingEfficiency += quantity
						if (self._farmingEfficiency > 5):
							self._farmingEfficiency = 5
						print("Farming efficiency: ", self._farmingEfficiency)
					elif (typeOfResearch == "medical"):
						self._medicalEfficiency += quantity
					elif (typeOfResearch == "forest"):
						if (self._forestSize < quantity):
							self._fieldsSize += quantity - self._forestSize
							self._forestSize = 0
						else:
							self._forestSize -= quantity
							self._fieldsSize += quantity
							self._huntingEfficiency -= quantity
						print("Nous déforestons!")
					elif (typeOfResearch == "conservation"):
						if (self._conservationEfficiency < 4):
							self._conservationEfficiency += quantity



			elif (human.getJob().getType() == "farmer"):
				self._quantityFood += human.work(self._farmingEfficiency)
				nbFarmers += 1

			elif (human.getJob().getType() == "hunter"):
				food = human.work(self._huntingEfficiency)
				nbHunter += 1
				if (food == -100):
					nbDeath += 1
					self.populations.remove(human)
					dead = True
					nbHunter -= 1
					nbHunterDied += 1
				else:
					self._quantityFood += food

			elif (human.getJob().getType() == "fisherman"):
				food = human.work(self._fishingEfficiency)
				if (food == -1):
					human.eat()
					human.eat()
				elif (food == -100):
					pass
				elif (food == -2):
					pass
				else:
					self._quantityFood += food
				nbFisherman += 1

			elif (human.getJob().getType() == "craftmen"):
				self._quantityFood -= human.getJob().foodConsumed
				i = human.work(self._quantityOre)
				self.wealth += i
				if (i != 0):
					self._quantityOre -= 10
				nbCraftmens += 1

			elif (human.getJob().getType() == "baby"):
				nbBabies += 1
				if (human.getAge() == 12 * 12):
					human.chooseJob()
					nbBabies -= 1
			
			elif (human.getJob().getType() == "pregnant"):
				nbPregnant += 1
				nbMonths = human.work(0)
				if (nbMonths == 9):
					self.populations.append(human.getJob().birth(self))
					human.beMother()
					nbPregnant -= 1
					nbMother += 1
					newBabies += 1
				elif (nbMonths <= 3):
					self._quantityFood += 2
				elif (nbMonths > 3 and nbMonths <= 7):
					self._quantityFood += 1.75

			elif (human.getJob().getType() == "mother"):
				nbMother += 1
				nbMonths = human.work(0)
				if (nbMonths == 1):
					newMother += 1
				if (nbMonths == 10):
					human.stopBeingMother()
					nbMother -= 1

			elif (human.getJob().getType() == "breeder"):
				nbBreeder += 1
				self._quantityFood += human.work(self._liveStockEfficiency)

			elif (human.getJob().getType() == "soldier"):
				nbSoldier += 1


			else:
				print(human.getJob().getType())

			if (human.getGender() == "female" and dead == False):
				i = random.randint(0, 100)

				if (i <= human.getJob()._chanceReproduce and 
					((self._quantityFood > (self._populationSize * nbBabies))) and 
					(nbPregnant < (self._populationSize / 1.2) +2)):
					human.getPregnant()
					nbPregnant += 1
					newPregnant += 1


			if (dead == False):
				human.eat()
				if (human.getPv() <= 0):
					self.populations.remove(human)
					nbDeath	 += 1
					del human
					nbHeal += 1

				elif (human.getAge() > (random.randint(45*12, 75*12) + self._medicalEfficiency)):
					self.populations.remove(human)
					nbDeath	 += 1
					del human
					nbOldAge += 1

			else:
				del human


		#print("Population de {} = {} personnes".format(self.name, str(self._populationSize)))
		#print("{} personnes sont mortes cette année là ci".format(str(nbDeath)))
		self._populationSize = len(self.populations)


		self.rotFood()

		if (self._quantityFood <= 0):
			print("FAMINE DANS {}".format(self.name))
		#print("La population totale de {} est {}".format(self.name, str(len(self.populations))))
		#print("La quantité de nourriture en stock est de {}".format(str(round(self._quantityFood, 2))))


		print("Il y a ", newMother, " new Mothers this year ", end = "")
		print("Il y a ", newBabies, " new Babies this year ", end = "")
		print("Il y a ", newPregnant, " new Pregnant this year")
		

		self.newPregnants.append(newPregnant)
		self.newMothers.append(newMother)
		self.newBabiess.append(newBabies)


		self.Hunter.append(round(nbHunter))
		self.Fishermans.append(round(nbFisherman))
		self.Gatherers.append(round(nbGatherer))
		self.Farmers.append(round(nbFarmers))
		self.Breeder.append(round(nbBreeder))
		self.Researcher.append(round(nbResearcher))
		self.Miner.append(round(nbMinor))
		self.Craftmens.append(round(nbCraftmens))
		self.Blacksmith.append(round(nbBlacksmith))
		self.Soldier.append(round(nbSoldier))


		self.FoodStockpile.append(round(self._quantityFood))

		self.totalDeath.append(nbDeath)
		self.HunterDied.append(nbHunterDied)
		self.Heal.append(round(nbHeal))
		self.OldAge.append(round(nbOldAge))

		self.Babies.append(round(nbBabies))
		self.Pregnant.append(round(nbPregnant))
		self.Mother.append(round(nbMother))
	
		self.historyMedicalEfficiency.append(self._medicalEfficiency)
		self.historyHuntingEfficiency.append(self._huntingEfficiency)
		self.historyResearchEfficiency.append(self._researchEfficiency)
		self.historyFarmingEfficiency.append(self._farmingEfficiency)
	
		self.PopulationControl.append(self._populationSize)

		if (self._populationSize == 0):
			return (False)
		else:
			return (True)

	def run(self):
		i = 0
		while (i < self._nbYears and self.life() and self.ended == False):
			while self.paused:
				time.sleep(1)

			self.turn()
			#print("Tour numéro: ", i)
			i += 1



	def graph(self):
		#with lock:
		import option
		a = save_city(self._size, self._populationSize, self.name, self._nbYears, j = self.j, _urbanisation = self._urbanisation,
		 _forestSize = self._forestSize, _mountainSize = self._mountainSize,
 _fieldsSize = self._fieldsSize, _extensions = self._extensions, _farmingEfficiency = self._farmingEfficiency,
  _huntingEfficiency = self._huntingEfficiency, _researchEfficiency = self._researchEfficiency, 
 _medicalEfficiency = self._medicalEfficiency, _quantityFood = self._quantityFood , _FoodWhenResearch = self._FoodWhenResearch,
  _quantityBaby = self._quantityBaby, _conservationEfficiency = self._conservationEfficiency, 
 hasSeaAccess = self.hasSeaAccess, wealth = self.wealth, _quantityOre = self._quantityOre, _quantityHorse = self._quantityHorse,
  _quantityTools = self._quantityTools, _historyHorse = self._historyHorse, historyOre = self.historyOre,
  historyWealth = self.historyWealth, FoodStockpile = self.FoodStockpile, Deaths = self.Deaths, Fishermans = self.Fishermans, 
  Babies = self.Babies, Farmers = self.Farmers, Hunter = self.Hunter, Pregnant = self.Pregnant, 
  Mother = self.Mother, Researcher = self.Researcher, Craftmens = self.Craftmens, Gatherers = self.Gatherers, Miner = self.Miner, Soldier = self.Soldier,
  Blacksmith = self.Blacksmith, Trainer = self.Trainer, OldAge = self.OldAge, HunterDied = self.HunterDied, 
  historyFarmingEfficiency = self.historyFarmingEfficiency, historyHuntingEfficiency = self.historyHuntingEfficiency, 
  historyResearchEfficiency = self.historyResearchEfficiency, historyMedicalEfficiency = self.historyMedicalEfficiency, 
  PopulationControl = self.PopulationControl, Heal = self.Heal, populations = self.populations)
		self.generateGraph(self._nbYears)
		print("{} pop {} ".format(self.getName(),str(self.getPopulationSize())))
		return (a)
		
	def when_pressed(self):
		print("Tour numéro: ", self.turnNumber)
		if (self.paused == False):
			self.paused = True
			print("La cité ", self.name, " est mise en pause")
			print(sum(self.newPregnants), sum(self.newMothers), sum(self.newBabiess))
			return (self.graph())
		self.paused = False
		print("La cité ", self.name, " est remise en route!")
		return (None)

	def pause_the_city(self):
		if (self.paused == False):
			print("La cité ", self.name, " est mise en pause")
			self.paused = True
			return
		self.paused = False
		print("La cité ", self.name, " est remise en route!")

