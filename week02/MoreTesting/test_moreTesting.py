import unittest
from moreTesting import my_sort, simplify_fraction, collect_fractions, sort_fractions


class TestSortFunction(unittest.TestCase):

    def test_sorting_function(self):

        iterable = []
        result = my_sort(iterable)

        self.assertEqual(result, iterable)

    def test_sorting_fuction_with_elements_and_asceding_true(self):
        iterable = [1, 2, 3]

        iterable = my_sort(iterable)

        are_sorted = True

        for i in range(0, len(iterable) - 1):
            nextId = i + 1
            if iterable[i] > iterable[nextId]:
                are_sorted = False
                break

        self.assertTrue(are_sorted)

    def test_sorting_fuction_with_elements_and_asceding_false(self):
        iterable = [1, 2, 3]
        ascending = False
        iterable = my_sort(iterable, ascending)

        are_sorted = True

        for i in range(0, len(iterable) - 1):
            nextId = i + 1
            if iterable[i] < iterable[nextId]:
                are_sorted = False
                break

        self.assertTrue(are_sorted)

    def test_dictionaries(self):
        iterable = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        key = 'age'
        ascending = True
        result = my_sort(iterable, ascending, key)

        are_sorted = True

        for i in range(0, len(result) - 1):
            nextId = i + 1
            x = iterable[i].get('age')
            y = iterable[nextId].get('age')
            if x > y:
                are_sorted = False
                break

        self.assertTrue(are_sorted)


class TestSimplifyFraction(unittest.TestCase):

    def test_if_it_is_irreducible_by_default(self):
        fraction = (1, 3)

        result = simplify_fraction(fraction)

        self.assertEqual(fraction, result)

    def test_if_it_is_normal(self):
        fraction = (4, 10)

        result = simplify_fraction(fraction)

        self.assertEqual(result, (2, 5))

    def test_if_if_is_one(self):
        fraction = (1, 1)

        result = simplify_fraction(fraction)

        self.assertEqual(result, (1, 1))

    def test_if_it_is_zero_result(self):
        fraction = (0, 0)

        result = simplify_fraction(fraction)

        self.assertEqual(fraction, result)


class TestCollectFractions(unittest.TestCase):
    def test_sum_of_two_fractions_even(self):
        fractions = [(1, 2), (1, 4)]

        result = collect_fractions(fractions)

        self.assertEqual(result, (3, 4))

    def test_sum_of_two_fractions_odd(self):
        fractions = [(1, 7), (1, 3)]

        result = collect_fractions(fractions)

        self.assertEqual(result, (10, 21))


class TestSortFractions(unittest.TestCase):

    def test_if_it_is_zero_fraction(self):
        fractions = []

        result = sort_fractions(fractions)

        are_equal = True
        if fractions != result:
            are_equal = False

        self.assertTrue(are_equal)

    def test_if_it_is_one_fraction(self):
        fractions = [(1, 2)]

        result = sort_fractions(fractions)

        are_equal = True
        if fractions != result:
            are_equal = False

        self.assertTrue(are_equal)

    def test_sorting_fuction_with_elements_and_asceding_true(self):
        fractions = [(2, 3), (1, 2)]
        ascending = True
        fractions = sort_fractions(fractions, ascending)

        are_sorted = True

        for i in range(0, len(fractions) - 1):
            nextId = i + 1
            first = fractions[i]
            second = fractions[nextId]
            delimF = first[0] / first[1]
            delimS = second[0] / second[1]
            if delimF > delimS:
                are_sorted = False
                break

        self.assertTrue(are_sorted)

    def test_sorting_fuction_with_elements_and_asceding_false(self):
        fractions = [(2, 3), (1, 2)]
        ascending = False
        fractions = sort_fractions(fractions, ascending)

        are_sorted = True

        for i in range(0, len(fractions) - 1):
            nextId = i + 1
            first = fractions[i]
            second = fractions[nextId]
            delimF = first[0] / first[1]
            delimS = second[0] / second[1]
            if delimF < delimS:
                are_sorted = False
                break

        self.assertTrue(are_sorted)

    def test_sorting_fuction_with_elements_and_asceding_more_than_two(self):
        fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        fractions = sort_fractions(fractions)

        are_sorted = True

        for i in range(0, len(fractions) - 1):
            nextId = i + 1
            first = fractions[i]
            second = fractions[nextId]
            delimF = first[0] / first[1]
            delimS = second[0] / second[1]
            if delimF > delimS:
                are_sorted = False
                break

        self.assertTrue(are_sorted)

    def test_sorting_fuction_with_elements_and_asceding_false_more_than_one(self):
        fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        ascending = False
        fractions = sort_fractions(fractions, ascending)

        are_sorted = True

        for i in range(0, len(fractions) - 1):
            nextId = i + 1
            first = fractions[i]
            second = fractions[nextId]
            delimF = first[0] / first[1]
            delimS = second[0] / second[1]
            if delimF < delimS:
                are_sorted = False
                break

        self.assertTrue(are_sorted)

    def test_sorting_fuction_with_elements_with_equal_values(self):
        fractions = [(2, 3), (1, 2), (1, 3)]

        fractions = sort_fractions(fractions)

        are_sorted = True

        for i in range(0, len(fractions) - 1):
            nextId = i + 1
            first = fractions[i]
            second = fractions[nextId]
            delimF = first[0] / first[1]
            delimS = second[0] / second[1]
            if delimF > delimS:
                are_sorted = False
                break

        self.assertTrue(are_sorted)


if __name__ == '__main__':
    unittest.main()
