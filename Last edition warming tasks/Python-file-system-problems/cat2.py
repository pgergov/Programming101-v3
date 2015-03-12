import sys

def main():
    for i in range(1,len(sys.argv)):
        content = open(sys.argv[i], 'r')
        print(content.read())
        content.close()
        if i+1 < len(sys.argv):
            print()

if __name__ == '__main__':
    main()