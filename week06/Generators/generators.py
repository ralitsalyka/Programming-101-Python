def chain(iterable_one, iterable_two):
    for x in iterable_one:
        yield x
    for x in iterable_two:
        yield x


# print(list(chain(range(0, 4), range(4, 8))))

def compress(iterable, mask):
    i = 0
    for x in iterable:
        if mask[i] is True:
            yield x
        i = i + 1



#(print(list(compress(["Ivo", "Rado", "Panda"], [True, True, True]))))


def cycle(iterable):
    while True:
        for x in iterable:
            yield x


# endless = cycle(range(0, 10))
# for item in endless:
    # print(item)
