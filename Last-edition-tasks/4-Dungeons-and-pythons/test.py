with open("basic_dungeon.txt", "r") as f:
    content = [f.read()]
print(content)

# [['H.##......'],
#  ['#.##..###.'],
#  ['#.###.###.'],
#  ['#.....###.'],
#  ['###.#####O']]
new_content = ""
# if direction = left:
try:
    if content[content[0].index("H") + 1] != "#":
        for i in range(len(content)):
            if i == content[0].index("H"):
                content[i] = "."
            elif i == content[0].index("H") + 1:
                content[i] = "H"
except:
    pass
print(content)

# def search(x, y):
#     if content[x][y] == "O":
#         print('found at %d,%d' % (x, y))
#         return True
#     elif content[x][y] == "#":
#         print('wall at %d,%d' % (x, y))
#         return False
#     # elif content[x][y] == 3:
#     #     print 'visited at %d,%d' % (x, y)
#     #     return False
#     print('visiting %d,%d' % (x, y))
#     content[x][y] = "#"

#     try:
#         if ((y > 0 and search(x, y - 1))
#             or (x > 0 and search(x - 1, y))
#             or (y < len(content) - 1 and search(x, y+1))
#             or (x < len(content) - 1 and search(x + 1, y))):
#             return True
#     except:
#         return False

# search(0, 0)
