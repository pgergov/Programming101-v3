f = open("level1.txt", 'r')
content = f.read()
f.close()


with open("level1.txt", 'r') as f:
    text = f.read()
    f.close()

print(text)
