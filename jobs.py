import random

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
		j = random.randint(-4, 50)
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
		self._name = "Breeder"
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
			placeHunter = (self._city._forestSize * self._city._huntingEfficiency) - self._city.Hunter[-1] - (self._city.Gatherers[-1] / 2)  #Il n'y a plus de place pour des hunter
			placeHunter = placeHunter * self._city.trending_food()
		except:
			placeHunter = 0
		if (placeHunter < 0):
			placeHunter = 0
		#----------------
		try:
			placeFisherman = (self._city._waterUsable * self._city._fishingEfficiency) - self._city.Fisherman[-1]  #Il n'y a plus de place pour des Fisherman
			placeFisherman = placeFisherman * self._city.trending_food()
		except:
			placeFisherman = 0
		if (placeFisherman < 0):
			placeFisherman = 0
		#----------------
		try:
			placeGatherer = (self._city._forestSize) - self._city.Hunter[-1] - (self._city.Gatherers[-1] / 2)  #Il n'y a plus de place pour des placeGatherer
			placeGatherer = placeGatherer * self._city.trending_food()
		except:
			placeGatherer = 0
		if (placeGatherer < 0):
			placeGatherer = 0

		#----------------
		try:
			placeFarmer = (self._city._fieldsSize * self._farmingEfficiency) - self._city.Farmers[-1]  #Il n'y a plus de place pour des placeFarmer
			placeFarmer = placeGatherer * self._city.trending_food()
		except:
			placeFarmer = 0
		if (placeFarmer < 0):
			placeFarmer = 0
		#----------------
		try:
			placeBreeder = (self._city._liveStockSize * self._city._liveStockEfficiency) - self._city.Breeder[-1]  #Il n'y a plus de place pour des placeBreeder
			placeBreeder = placeBreeder * self._city.trending_food()
		except:
			placeBreeder = 0
		if (placeBreeder < 0):
			placeBreeder = 0
		#----------------
		try:
			placeResarcher = (self._city._urbanisation) - self._city.Resarcher[-1]  #Il n'y a plus de place pour des placeMinor
		except:
			placeResarcher = 0
		if (placeResarcher < 0):
			placeResarcher = 0
		#----------------
		try:
			placeMinor = (self._city._mountainSize) - self._city.Miner[-1]  #Il n'y a plus de place pour des placeMinor
		except:
			placeMinor = 0
		if (placeMinor < 0):
			placeMinor = 0
		#----------------
		try:
			placeCraftmens = (self._city._artisanSpace) - self._city.Craftmens[-1]  #Il n'y a plus de place pour des placeCraftmens
		except:
			placeCraftmens = 0
		if (placeCraftmens < 0):
			placeCraftmens = 0
		#----------------
		try:
			placeBlacksmith = (self._city._artisanSpace) - self._city.Blacksmith[-1]  #Il n'y a plus de place pour des placeBlacksmith
		except:
			placeBlacksmith = 0
		if (placeBlacksmith < 0):
			placeBlacksmith = 0
		#----------------
		try:
			placeSoldier = (self._city._soldierSpace) - self._city.Soldier[-1]  #Il n'y a plus de place pour des placeSoldier
		except:
			placeSoldier = 0
		if (placeSoldier < 0):
			placeSoldier = 0
		total = placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + placeMinor + placeCraftmens + placeBlacksmith + placeSoldier
		if total <= 0: # On a plus de place nulle part!
			self._job = Unemployed()
			return
		i = random.randint(0, round(total))
		if (i < placeHunter):
			self._job = Hunter()
			return
		elif (i < (placeHunter + placeFisherman)):
			self._job = Fisherman()
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer)):
			self._job = Gatherer()
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer)):
			self._job = Farmer()
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder)):
			self._job = Breeder()
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher)):
			self._job = Researcher()
			return
		elif (i <= (totplaceHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + 
		placeMinor)):
			self._job = Minor()
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + 
		placeMinor + placeCraftmens)):
			self._job = Craftmens()
			return
		elif (i <= (placeHunter + placeFisherman + placeGatherer + placeFarmer + placeBreeder + placeResarcher + 
		placeMinor + placeCraftmens + placeBlacksmith)):
			self._job = Blacksmith()
			return
		elif (i <= total):
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
