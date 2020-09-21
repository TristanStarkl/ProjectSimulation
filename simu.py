from Maps import *
from City import *
import random
from timeit import default_timer as timer
import option


def main_boucle(nbyears, popstart, nbcities, sizeX, sizeY):
	start = timer()
	option1 = option.loadFromFile("options")
	_cities = []
	nbDead = 0
	pop = 0
	simu = simulation(option1.nbCasesX, option1.nbCasesY, option1)
	simu.map.start(option1, nbcities, popstart, nbyears)
	simu.map.show()
	duration = timer() - start
	print("Loading duration = ", duration)
	for s in _cities:
		s.kill_city()
	import sys
	sys.exit()

	#for s in _cities:
	#	s.join()

if __name__ == "__main__":
	main_boucle(20000, 100, 1, 80, 80)