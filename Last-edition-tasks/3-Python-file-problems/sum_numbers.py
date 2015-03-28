import sys


def sum_numbers():
    f = open(sys.argv[1], 'r')
    s = sum([int(numb) for numb in f.read().split(" ")])
    f.close()

    return s


def main():
    print(sum_numbers())

if __name__ == '__main__':
    main()
