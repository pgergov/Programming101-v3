import sys


def main():
    with open(sys.argv[1], 'r') as f:
        text = f.read()

    print(text)

if __name__ == '__main__':
    main()
