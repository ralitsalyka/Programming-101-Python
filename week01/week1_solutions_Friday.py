
def anagram(word2, word1):
    a = [word1[x] for x in range(0, len(word1))]
    b = [word2[x] for x in range(0, len(word2))]

    x = len(word1)
    y = len(word2)
    errors = 0
    if x < y or x > y:
        return False

    for i in range(0, len(a)):
        n = b.count(a[i])
        if n != 1:
            errors += 1

    if errors >= 1:
        return False
    else:
        return True

# word1 = input("word1: ")
# word2 = input("word2: ")
# print(anagram("TOP_CODER", "COTO_PRODE"))
# print(anagram("kilata", "cvetelina_yaneva"))
# print(anagram("BRADE", "BEARD"))
# print(anagram(word1, word2))


def is_credit_card_valid(number):
    temp = number
    len_of_num = 0
    a = []
    while temp > 0:
        len_of_num += 1
        digit = temp % 10
        a.append(digit)
        temp //= 10
    if len_of_num % 2 == 0:
        return False
    a = a[::-1]

    print(a)
    for i in range(0, len(a)):
        if i % 2 == 1:
            n = a[i] * 2
            newNum = 0
            while n > 0:
                newNum = newNum + n % 10
                n //= 10
            a[i] = newNum
    print(a)

    Sum = sum(a)
    print(Sum)
    if(Sum % 10 == 0):
        return True
    else:
        return False


# print(is_credit_card_valid(79927398713))
# print(is_credit_card_valid(79927398715))


def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count > 0:
        return False
    else:
        return True


def goldbach(n):
    primes = []
    tupples = []
    for i in range(1, n):
        if(prime(i)):
            primes.append(i)

    for i in range(0, len(primes) - 1):
        for j in range(i, len(primes)):
            Sum = primes[i] + primes[j]
            if(Sum == n):
                tupple = (primes[i], primes[j])
                tupples.append(tupple)

    return tupples
# print(goldbach(100))
