import sys


def wc():
    with open(sys.argv[2], "r") as f:
        lines = 0
        words = 0
        characters = 0
        for line in f:
            wordslist = line.split()
            lines = lines + 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)

    if sys.argv[1] == 'words':
        print(words)
    if sys.argv[1] == 'lines':
        print(lines)
    if sys.argv[1] == 'chars':
        print(characters)


def main():
    wc()


if __name__ == '__main__':
    main()
