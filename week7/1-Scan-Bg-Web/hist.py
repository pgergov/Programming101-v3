class Histogram:

    def __init__(self):
        self.info = {}

    def add(self, element):
        if element in self.info:
            self.info[element] += 1
        else:
            self.info[element] = 1

    def count(self, element):
        if element in self.info:
            return self.info[element]
        return None

    def get_dict(self):
        return self.info
