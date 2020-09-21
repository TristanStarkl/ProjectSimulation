import jobs
import humans

class cities():
	def __init__(self, name, size, forestSize, fieldsSize, populationSize):
		_size = size
		_urbanisation = 10
		_forestSize = forestSize
		_fieldsSize = fieldsSize
		_populationSize = populationSize
		_citiesSpace = int(_populationSize / _urbanisation)
		_unusableSpace = _size - _forestSize - _fieldsSize - _citiesSpace
		_farmingEfficiency = 1
		_huntingEfficiency = 1
		_researchEfficiency = 1
		_medicalEfficiency = 1
		_quantityFood = populationSize * 12
		_FoodWhenResearch = 10
		_quantityBaby = 1.3
		
		populations = []

	def initializePopulation():
		nbFarmers = int((self._fieldsSize / (self._forestSize + self._fieldsSize)) * self._populationSize)
		for i in range(nbFarmers):
			a = __humans__(random(12, 25), 100, farmer())
			self.populations.append(a)

		nbHunter = self._populationSize - nbFarmers
		for i in range(nbHunter):
			a = __humans__(random(12, 25), 100, hunter())
			self.populations.append(a)

	def getFood():
		return (self._quantityFood)

	def getPopulationSize():
		return (self._populationSize)

	def removeFood(quantity):
		self._quantityFood -= quantity

	def addBaby(baby):
		self.babies.append(baby)
		self.populations.append(baby)

	def turn():
		nbDeath = 0
		for human in populations:
			if (human.getJob.getType() == "researcher"):
				self._quantityFood -= self._FoodWhenResearch
				quantity, typeOfResearch = human.work(self._researchEfficiency)
				if (typeOfResearch == "hunting"):
					self._huntingEfficiency += quantity
				elif (typeOfResearch == "research"):
					self._researchEfficiency += quantity
					if (self._FoodWhenResearch > 2 ):
						self._FoodWhenResearch -= 1
				elif (typeOfResearch == "farming"):
					self._farmingEfficiency += quantity
				elif (typeOfResearch == "medical"):
					self._medicalEfficiency += quantity
				elif (typeOfResearch == "forest"):
					self._forestSize -= quantity
					self.fieldsSize += quantity
					self._huntingEfficiency -= quantity
				elif (typeOfResearch == "unusableSpace"):
					self._unusableSpace -= quantity
					self._forestSize += quantity / 2
					self._fieldsSize += quantity / 2

			elif (human.getJob.getType() == "farmer"):
				self._quantityFood += human.work(self._farmingEfficiency)

			elif (human.getJob.getType() == "hunter"):
				food = hunter.work(self._huntingEfficiency)
				if (food == -100):
					nbDeath += 1
					self.hunters.remove(hunter)
					del hunter
				self._quantityFood += foodty

			elif (human.getJob.getType() == "baby"):
				human.eat()
				human.age(1)
				if (human.getAge() == 12):
					human.chooseJob()
			
			elif (human.getJob.getType() == "pregnant"):
				self.populations.append(human.work())
				human.beMother()

			elif (human.getJob.getType() == "mother"):
				if (human.work() == 10):
					human.stopBeingMother()


			human.eat()
			if (human.getPv() <= 0  or human.getAge() > (random.randint(25, 40) + self._medicalEfficiency)):
				self.populations.remove(human)
				nbDeath	 += 1
				del human

		print("------------------------------------{}-----------------------------------------------------".format(self.name))
		print("Population de {} = {} personnes".format(self.name, str(self.populationSize)))
		print("{} personnes sont mortes ce mois ci".format(str(nbDeath)))
		self.populationSize = self.populationSize - nbDeath

		while ((self._quantityFood > (self.populationSize * self._quantityBaby))):
			for human in self.populations:
				if (human.getGender == "female"):
					i = random.randint(0, 100)
					if (i <= human.getChancePregnant()):
						human.reproduce()

		print("La population totale de {} est {}".foramt(self.name, str(len(self.populations))))
		print("La quantité de nourriture en stock est de {}".format(str(self._quantityFood)))


