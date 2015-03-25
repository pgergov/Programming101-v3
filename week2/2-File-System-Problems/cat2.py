import sys


def main():
    text = []
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], 'r') as f:
            text.append(f.read())

    print("\n\n".join(text))

if __name__ == '__main__':
    main()
