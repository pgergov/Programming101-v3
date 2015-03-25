import sys
import os


def concat_files():
    result = []
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], 'r') as f:
            content = f.read() + "\n"
            result.append(content)

    try:
        with open("MEGATRON.txt", 'a') as text:
            if os.stat("MEGATRON.txt").st_size > 0:
                text.write("\n")
            text.write("\n".join(result))
    finally:
        text.close()


def main():
    concat_files()

if __name__ == '__main__':
    main()
