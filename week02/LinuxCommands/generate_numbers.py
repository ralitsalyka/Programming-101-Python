import sys
from random import randint


def generate_numbers():
    with open(sys.argv[1], "w") as f:
        n = int(sys.argv[2])
        while n > 0:
            imput = str(randint(1, 1000))
            f.write(imput)
            f.write(" ")
            n -= 1


def main():
    generate_numbers()


if __name__ == '__main__':
    main()
