import sys


def main():
    f = open(sys.argv[1], 'r')
    s = sum([int(numb) for numb in f.read().split(" ")])
    f.close()
    print(s)

if __name__ == '__main__':
    main()
