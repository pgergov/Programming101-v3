from hero import Hero
from orc import Orc


class Dungeon():

    players = []

    def __init__(self, dungeon):
        self.dungeon = dungeon

    def print_map(self):
        with open(self.dungeon, "r") as f:
            print(f.read())

    def change_map(self, char):
        with open(self.dungeon, 'r') as f:
            content = f.read()
        if content.index("S") == 0:
            content = char + content[1:]
        elif content.index("S") == len(content) - 1:
            content = content[:len(content) - 1] + char
        else:
            content = content[:content.index("S")] + char
            + content[content.index("S") + 1:]
        with open(self.dungeon, 'w') as f:
            f.write(content)

    def spawn(self, player_name, entity):
        Dungeon.players.append(player_name)
        if isinstance(entity, Hero):
            char = "H"
        elif isinstance(entity, Orc):
            char = "O"
        with open(self.dungeon, 'r') as f:
            content = f.read()
        try:
            content[content.index("S")]
            self.change_map(char)
        except:
            return False
        return True

def move(player_name, direction):
    pass