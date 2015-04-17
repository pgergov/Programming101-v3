# with open("level1.txt", 'r') as f:
#     content = f.readlines()
#     for line in content[:]:
#         print(line)

with open("level1.txt", 'r') as f:
    content = f.read()
    lines = content.split("\n")
    mapp = [list(line) for line in lines]
    for roll in mapp:
        # print("".join(roll))
        print(roll)
