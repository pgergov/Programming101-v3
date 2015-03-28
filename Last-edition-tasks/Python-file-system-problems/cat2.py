import sys


def cat():
    text = []
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], 'r') as f:
            text.append(f.read())

    return text


def main():
    print("\n\n".join(cat()))

if __name__ == '__main__':
    main()
