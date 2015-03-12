from sys import argv

script, filename = argv

content = open(filename, 'r')
print(content.read())

content.close()