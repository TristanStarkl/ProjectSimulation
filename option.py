import json
from os import listdir
from os.path import isfile, join, exists
import os
import glob

class sauvegarde():
	def __init__(self, name):
		self.name = name

class options(sauvegarde):
	def __init__(self, fullscreen, name, nbCity, nbCasesX, nbCasesY):
		sauvegarde.__init__(self, "options")
		self.fullscreen = fullscreen
		self.name = name
		self.nbCity = nbCity
		self.nbCasesX = nbCasesX
		self.nbCasesY = nbCasesY

def convert_to_dict(obj):
	obj_dict = {
    	"__class__": obj.__class__.__name__,
  	}
	obj_dict.update(obj.__dict__)
	return obj_dict


def dict_to_obj(our_dict):
    if "__class__" in our_dict:
        class_name = our_dict.pop("__class__")
        module_name = our_dict.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj



def saveToFile(obj):
	fileName = "./save/{}.json".format(obj.name)
	with open(fileName, "w+") as f:
		data = json.dumps(obj, default=convert_to_dict,sort_keys=True)
		f.write(data)

def loadFromFile(typeObject):
	file = "./save/{}.json".format(typeObject)
	data = []
	with open(file, "r") as f:
		data.append(json.loads(f.read(), object_hook=dict_to_obj))
	return (data[0])
	
if __name__ == "__main__":
	options = options(True, 10,30,30)
	saveToFile(options)