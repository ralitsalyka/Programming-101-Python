
def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

# print(sum_of_digits(123))


def to_list(n):
    to_list = []
    while n > 0:
        x = n % 10
        to_list.append(x)
        n //= 10
    to_list.reverse()
    return to_list

# print(to_list(123))


def to_number(digits):
    s = 0
    for digit in digits:
        s *= 10
        s += digit
    return s

# print(to_number([1,2,3]))


def factoriel(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# print(factoriel(4))


def fact(n):
    sum = 0
    while n > 0:
            x = n % 10
            sum += factoriel(x)
            n //= 10
    return sum

# print(fact(999))


def sum_reverse_of_digits(n):
    temp = n
    s = 0
    while temp > 0:
        digit = temp % 10
        s = s * 10 + digit
        temp = temp // 10
    if(s == n):
        print("True")
    else:
        print("False")

# print(sum_reverse_of_digits(111))


def reverseString(st):
    return st == st[::-1]

# print(reverseString("abba"))


def palindrome(st):
    st_str = str(st)
    return st_str == st_str[::-1]

# print(palindrome('aaa'))
# print(palindrome(121))


def count_vowels(str):
    count = 0
    str = str.lower()
    for i in range(0, len(str)):
        if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'y':
            count += 1
    return count

# print(count_vowels("PYTHON"))
# print(count_vowels("Theistareykjarbunga"))
# print(count_vowels("grrrrgh!"))
# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
# print(count_vowels("A nice day to code!"))


def count_consonants(str):
    count = 0
    str = str.lower()
    consonants = "bcdfghjklmnpqrstvwxz"
    for i in range(0, len(str)):
        if str[i] in consonants:
            count += 1
    return count

# print(count_consonants("Python"))
# print(count_consonants("Theistareykjarbunga"))
# print(count_consonants("grrrrgh!"))
# print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
# print(count_consonants("A nice day to code!"))


def char_histogram(string):
    sets = set(string)
    dictionary = {x: string.count(x) for x in sets}
    return dictionary

# print(char_histogram("Python!"))


def sum_matrix(input):
    my_sum = 0
    for row in input:
        my_sum += sum(row)
    return my_sum

# print(sum_matrix([[1, 2],[3, 4],[5, 6]]))
# print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))



def nan_expand(num):
    msg = "Not a "
    i = 1
    while i <= num:
        print(msg, end=' ')
        i = i + 1
    return ''.join(" NaN")

# print(nan_expand(4))


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    tuplles = [(x, factors.count(x)) for x in factors]

    return tuplles


# print(prime_factors(10))
# print(prime_factors(14))
# print(prime_factors(356))
# print(prime_factors(89))
# print(prime_factors(1000))



def group(list):
    curr_list = []
    result = []
    for x in list:
        if x in curr_list:
            pass
        else:
            if curr_list != []:
                result.append(curr_list)
            curr_list = []
        curr_list.append(x)
    result.append(curr_list)
    return result


# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    new_list = []
    max_it = 0
    for x in items:
        if x in new_list:
            pass
        else:
            if new_list != []:
                n = len(new_list)
                if n > max_it:
                    max_it = n
            new_list = []
        new_list.append(x)
    n = len(new_list)
    if n > max_it:
        max_it = n
    return max_it

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
