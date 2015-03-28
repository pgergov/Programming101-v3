import sys
from random import randint


def generate_numbers():
    numbs = []
    for i in range(int(sys.argv[2])):
        numbs.append(str(randint(1, 1000)))

    with open(sys.argv[1], 'w') as f:
        f.write(" ".join(numbs))


def main():
    generate_numbers()

if __name__ == '__main__':
    main()
