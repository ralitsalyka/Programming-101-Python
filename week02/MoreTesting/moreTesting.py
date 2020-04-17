from math import gcd


def my_sort(iterable=None, ascending=True, key=''):
    if iterable is None:
        iterable = []

    if key == '':
        if ascending is True:
            for i in range(0, len(iterable) - 1):
                for j in range(i, len(iterable)):
                    temp = 0
                    if(iterable[i] > iterable[j]):
                        temp = iterable[i]
                        iterable[i] = iterable[j]
                        iterable[j] = temp

        if ascending is False:
            for i in range(0, len(iterable) - 1):
                for j in range(i, len(iterable)):
                    temp = 0
                    if(iterable[i] < iterable[j]):
                        temp = iterable[i]
                        iterable[i] = iterable[j]
                        iterable[j] = temp

    else:
        for i in range(0, len(iterable) - 1):
            for j in range(i, len(iterable)):
                x = iterable[i].get('age')
                y = iterable[j].get('age')
                temp = {}
                if(x > y):
                    temp = iterable[i]
                    iterable[i] = iterable[j]
                    iterable[j] = temp

    return iterable


def simplify_fraction(tup):
    if tup[0] == 0 or tup[1] == 0:
        new_tup = (0, 0)
        return new_tup

    gcd_of_tuple = gcd(tup[0], tup[1])
    x = tup[0]
    y = tup[1]

    if x == 1 or y == 1:
        new_tup = (x, y)
    else:
        while x % gcd_of_tuple == 0 and y % gcd_of_tuple == 0:
            x = x // gcd_of_tuple
            y = y // gcd_of_tuple

        new_tup = (x, y)
    return new_tup


def collect_fractions(fractions):
    temp_f = fractions[0]
    temp_s = fractions[1]

    x = temp_f[0] * temp_s[1] + temp_s[0] * temp_f[1]
    y = temp_s[1] * temp_f[1]

    gcd_of_tuples = gcd(x, y)

    if gcd_of_tuples == 1:
        tup = (x, y)
    else:
        if x == 1 or y == 1:
            tup = (x, y)
            return tup

        else:
            while x % gcd_of_tuples == 0 and y % gcd_of_tuples == 0:
                x = x // gcd_of_tuples
                y = y // gcd_of_tuples

    tup = (x, y)
    return tup


def sort_fractions(fractions, ascending=True):
    if len(fractions) == 1:
        return fractions

    if len(fractions) == 0:
        return fractions

    if ascending is True:
        for i in range(0, len(fractions) - 1):
            for j in range(i, len(fractions)):
                temp = 0
                first = fractions[i]
                second = fractions[j]
                delimF = first[0] / first[1]
                delimS = second[0] / second[1]

                if delimF > delimS:
                    temp = fractions[i]
                    fractions[i] = fractions[j]
                    fractions[j] = temp
    else:
        for i in range(0, len(fractions) - 1):
            for j in range(i, len(fractions)):
                temp = 0
                first = fractions[i]
                second = fractions[j]
                delimF = first[0] / first[1]
                delimS = second[0] / second[1]

                if delimF < delimS:
                    temp = fractions[i]
                    fractions[i] = fractions[j]
                    fractions[j] = temp
    return fractions


def main():
    pass


if __name__ == '__main__':
    main()
