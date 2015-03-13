import sys

def main():
    content = open(sys.argv[1], 'r')
    numbers = content.read().split(" ")
    content.close()

    s = 0
    for numb in numbers:
        s += int(numb)
    print(s)

if __name__ == '__main__':
    main()