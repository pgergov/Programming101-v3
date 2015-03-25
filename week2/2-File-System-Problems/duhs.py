import sys
import os

size = 0


def duhs(path):

    for item in os.listdir(path):
        directory = path + "/" + item
        if os.path.isdir(directory):
            duhs(directory)
        else:
            global size
            size += os.path.getsize(directory)
    return size


def main():
    print(duhs(sys.argv[1]))

if __name__ == '__main__':
    main()
