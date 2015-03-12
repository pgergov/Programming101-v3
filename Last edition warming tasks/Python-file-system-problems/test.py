from sys import argv

script, filename = argv

file = open(filename, "w")

contents = ["Python is awesome.", "Check it out!", ]

file.write("\n".join(contents))

file.close()
