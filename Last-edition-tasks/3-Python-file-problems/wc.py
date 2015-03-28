import sys

def chars():
    counter = 0
    f = open(sys.argv[2], 'r')
    content = f.read()
    f.close()
    for char in content:
        counter += 1
    return counter

def words():
    counter = 0
    file_words = []
    f = open(sys.argv[2], 'r')
    file_words = f.read().replace("\n", " ").split(" ")
    f.close()
    for word in file_words:
        if word != "":
            counter += 1
    return counter

def lines():
    f = open(sys.argv[2], 'r')
    counter = sum(1 for line in f)
    f.close()
    return counter

def main():
    if sys.argv[1] == "words":
        print(words())
    elif sys.argv[1] == "chars":
        print(chars())
    elif sys.argv[1] == "lines":
        print(lines())

if __name__ == '__main__':
    main()