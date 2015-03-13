import sys
from random import randint

def main():
    f = open(sys.argv[1], 'w')
    for i in range(int(sys.argv[2])):
        f.write(str(randint(1,1000)))
        if i + 1 < int(sys.argv[2]):
            f.write(" ")
    f.close()

    f = open(sys.argv[1], 'r')
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()