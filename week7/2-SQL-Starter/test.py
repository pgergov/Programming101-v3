
def asd(x):
    print("it workds!")

commands = {
           "asd": asd
           }

def main():
    nam = input()
    commands[nam](2)

if __name__ == '__main__':
    main()
