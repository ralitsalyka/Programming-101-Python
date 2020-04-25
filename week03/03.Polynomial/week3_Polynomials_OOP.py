from utls import create_part_derive
from utls import create_list_of_derive
import sys


class Term:

    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __str__(self):
        return f'{self.string}'

    def __repr__(self):
        return f'{self.string}'

    def __getitem__(self, index):
        return self.string[index]

    def create_Terms_of_derives(self):
        word = Term(self.string)
        list_of_terms = create_list_of_derive(word)
        empty_list = []
        n = len(list_of_terms)
        for i in range(0, n):
            if list_of_terms[i] != '0':
                empty_list.append(list_of_terms[i])
        n = len(empty_list)
        return empty_list


class Polynomial:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f'{self.string}'

    def __len__(self):
        return len(self.string)

    def __str__(self):
        return f'The derivative of f(x) = {self.string} is:'

    def __getitem__(self, index):
        return self.string[index]

    def create_list_of_terms(self):
        word = Polynomial(self.string)
        list_of_terms = Term.create_Terms_of_derives(word)
        Derive = ""
        n = len(list_of_terms)
        if list_of_terms == []:
            Derive = '0'
        else:
            for i in range(0, n - 1):
                Derive = Derive + list_of_terms[i] + '+'
            Derive = Derive + list_of_terms[n - 1]
        Derive = "f'(x)=" + Derive
        return Derive


def main():
    word = Polynomial(sys.argv[1])
    print(word)
    print(Polynomial.create_list_of_terms(word))


if __name__ == '__main__':
    main()
