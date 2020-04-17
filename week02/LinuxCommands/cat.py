import sys


def cat():
    with open(sys.argv[1], "r") as f:
        print(f.read())


def main():
    cat()


if __name__ == '__main__':
    main()
