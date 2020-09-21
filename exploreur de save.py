


file = "./save/dkom.json"
new_file = "./save/new/dkom.json"
with open(file, "r") as f:
	with open(new_file, "a+") as n:
		content = f.read()
		new_string = content.replace(", \"", ",\n\"")
		n.write(new_string)

