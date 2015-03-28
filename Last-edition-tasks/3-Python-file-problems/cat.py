import sys


def cat():
    with open(sys.argv[1], 'r') as f:
        text = f.read()

    return text


def main():
    print(cat())

if __name__ == '__main__':
    main()
