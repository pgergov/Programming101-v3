class Histogram:
    def __init__(self):
        self.__servers = []

    def add(self, server):
        self.__servers.append(server)

    def count(self, server):
        if self.__servers.count(server) == 0:
            return None
        return self.__servers.count(server)

    def items(self):
        servers = set(self.__servers)
        return [(server, self.count(server)) for server in servers]

    def get_dict(self):
        return {key: value for key,value in self.items()}


if __name__ == '__main__':
    h = Histogram()

    h.add("Apache")
    h.add("Apache")
    h.add("nginx")
    h.add("IIS")
    h.add("nginx")

    print(h.count("Apache"))
    print(h.count("nginx"))
    print(h.count("IIS"))
    print(h.count("IBM Web Server") is None)

    for key, count in h.items():
        print("{}: {}".format(key, count))

    print(h.get_dict())
