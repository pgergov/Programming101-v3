from hero import Hero
from orc import Orc


class Dungeon():

    def __init__(self, dungeon):
        self.dungeon = dungeon

    def print_map(self):
        with open(self.dungeon, "r") as f:
            print(f.read())

    def change_map(self, char):
        new_content = ""
        with open(self.dungeon, 'r') as f:
            content = f.read()
            for i in range(len(content)):
                if i == content.index("S"):
                    new_content += char
                else:
                    new_content += content[i]
        with open(self.dungeon, 'w') as f:
            f.write(new_content)

    def spawn(self, player_name, entity):
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
