print("User commands: \n take <name> <price> \n status \n save \n listt \n load <number> \n finish")
command = [x for x in input("Enter command> ").split()]
orders = {}

def take():
    print("Hi")
    if command[1] in orders:
        orders[command[1]] += int(command[2])
    else:
        orders[command[1]] = int(command[2])
    return orders

def status():
    pass

def main():
    print(locals()[command[0]]())
