import sys

def main():
    content = open(sys.argv[1], 'r')
    print(content.read())
    content.close()

if __name__ == '__main__':
    main()