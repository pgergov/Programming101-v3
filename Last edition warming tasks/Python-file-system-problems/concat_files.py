import sys
import os 

def main():
    f = open(sys.argv[1], 'a')
    for i in range(2, len(sys.argv)):
        if os.stat(sys.argv[1]).st_size != 0:
            f.write("\n")
        content = open(sys.argv[i], 'r')
        f.write(content.read() + "\n")
        content.close()
        if i + 1 < int(len(sys.argv)) and os.stat(sys.argv[1]).st_size == 0:
            f.write("\n")
    f.close()

if __name__ == '__main__':
    main()