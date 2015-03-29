new_content = ""
with open("basic_dungeon.txt", 'r') as f:
    content = f.read()
try:
    content.index("S")
    for i in range(len(content) + 1):
        if i == content.index("S"):
            print("asd")
            new_content += "H"
        else:
            new_content += content[i]
except:
    pass
with open("basic_dungeon.txt", 'w') as f:
    f.write(new_content)

print(new_content)
print(content)
