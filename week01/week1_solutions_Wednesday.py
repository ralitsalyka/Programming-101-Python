
def gas_stations(distance, tank_size, stations):
    closest_stations = []
    if distance < 0:
        return "Invalid input"
    if tank_size < 0:
        return "Invalid input"
    startPosition = 0
    while(startPosition < distance):
        startPosition = startPosition + tank_size
        for i in range(0, len(stations)):
                if stations[i] >= startPosition:
                    before = i - 1
                    closest_stations.append(stations[before])
                    break

    closest_stations.append(stations[i])
    return closest_stations

# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
# print( gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


def is_number_balanced(n):
    string = str(n)
    list = []
    sum1 = 0
    sum2 = 0
    for i in string:
        list.append(i)
    n = len(string)
    half = n // 2
    for i in range(0, len(list) - half):
        sum1 = sum1 + int(list[i])

    for i in range(half, len(list)):
        sum2 = sum2 + int(list[i])

    return sum1 == sum2

# print(is_number_balanced(9))
# print(is_number_balanced(4518))
# print(is_number_balanced(28471))
# print(is_number_balanced(1238033))


def increasing(list_of):
    for i in range(0, len(list_of) - 1):
        j = i + 1
        if list_of[i] >= list_of[j]:
            return False
    return True


def decreasing(list_of):
    for i in range(0, len(list_of) - 1):
        j = i + 1
        if list_of[i] <= list_of[j]:
            return False
    return True


def increasing_or_decreasing(seq):
    if increasing(seq):
        msg = "Up!"
        return msg
    elif decreasing(seq):
        msg = "Down!"
        return msg
    else:
        return False

# print(increasing_or_decreasing([1,2,3,4,5]))
# print(increasing_or_decreasing([5,6,-10]))
# print(increasing_or_decreasing([1,1,1,1]))
# print(increasing_or_decreasing([9,8,7,6]))


def palindrome(st):
    n = st
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return st == rev


def get_largest_palindrome(n):
    temp = n - 1
    while temp > 0:
        if(palindrome(temp)):
            break
        temp -= 1
    return temp

# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754649))


def sum_of_numbers(input_string):
    temp = "0"
    Sum = 0
    for ch in input_string:
        if (ch.isdigit()):
            temp += ch
        else:
            Sum += int(temp)
            temp = "0"
    return Sum + int(temp)

# print(sum_of_numbers("1ab125cd3"))
# print(sum_of_numbers("ab"))
# print(sum_of_numbers("1101"))
# print(sum_of_numbers("1111O"))
# print(sum_of_numbers("1abc33xyz22"))
# print(sum_of_numbers("0hfabnek"))


def birthday_ranges(birthdays, ranges):
    born_people = []
    for i in ranges:
        x = i[0]
        y = i[1]
        Sum = 0
        while y >= x:
            s = birthdays.count(y)
            Sum = Sum + s
            y -= 1
        born_people.append(Sum)
    return born_people


print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))
