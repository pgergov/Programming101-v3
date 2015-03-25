import sys
from random import randint


def generate_n_numbers(n):
    return [randint(1, 1000) for i in range(n)]


def main():
    numbs = [str(numb) for numb in generate_n_numbers(int(sys.argv[2]))]
    with open(sys.argv[1], 'w') as f:
        f.write(" ".join(numbs))
        f.write("\n")

if __name__ == '__main__':
    main()
