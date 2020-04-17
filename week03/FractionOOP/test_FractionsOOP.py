import unittest
from week3_FractionsOOP import Fraction


class TestFraction(unittest.TestCase):
    def test_cannot_instantiate_fraction_with_zero_denominator(self):
        exception = None

        try:
            Fraction(1, 0)

        except AssertionError as exc:
            exception = exc

        self.assertIsNotNone(exception)

    def test_fractions_string_representation_is_as_expected_one(self):
        fraction1 = Fraction(1, 3)
        fraction2 = Fraction(-1, 3)
        fraction3 = Fraction(2, 4)

        self.assertEqual(str(fraction1), '1/3')
        self.assertEqual(str(fraction2), '-1/3')
        self.assertEqual(str(fraction3), '2/4')

    def test_fractions_equalization_with_equal_fractions(self):
        fraction1 = Fraction(1, 5)
        fraction2 = Fraction(1, 5)

        self.assertTrue(fraction1 == fraction2, 'Fractions are not equal')

    def test_simplified_fraction_is_preserved_after_simplication(self):
        fraction = Fraction(1, 5)
        expected = Fraction(1, 5)

        self.assertEqual(fraction.simplify(), expected)

    def test_fraction_is_simplified_as_expected(self):
        fraction = Fraction(10, 50)

        expected = Fraction(1, 5)

        self.assertEqual(fraction.simplify(), expected)

    def test_addition_fractions_works_correct_for_non_simplifiable_result(self):

            fraction1 = Fraction(1, 9)
            fraction2 = Fraction(1, 3)

            result = fraction1 + fraction2

            self.assertEqual(result, Fraction(12, 27))

    def test_fractions_greater_with_different_factions(self):
            fraction1 = Fraction(2, 5)
            fraction2 = Fraction(1, 5)

            self.assertTrue(fraction1 > fraction2, 'It is not greater ')

    def test_addition_fractions_works_correct_for_non_simplifiable_result_with_equal_denominator(self):
        fraction1 = Fraction(1, 5)
        fraction2 = Fraction(2, 5)

        result = fraction1 + fraction2

        self.assertEqual(result.num, 3)
        self.assertEqual(result.denom, 5)

    def test_addition_fractions_works_correct_for_non_simplifiable_result_with_non_equal_denominator(self):
        fraction1 = Fraction(1, 7)
        fraction2 = Fraction(2, 6)

        result = fraction1 + fraction2

        self.assertEqual(result.num, 10)
        self.assertEqual(result.denom, 21)

    def test_sorting_is_it_sorted(self):
        fraction = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

        are_sorted = True

        result = Fraction.sort_function(fraction)

        for i in range(0, len(result) - 1):
            frac1 = fraction[i]
            frac2 = fraction[i + 1]
            fract1 = Fraction(frac1[0], frac1[1])
            fract2 = Fraction(frac2[0], frac2[1])
            if fract1 > fract2:
                are_sorted = False

        self.assertTrue(are_sorted)


if __name__ == '__main__':
    unittest.main()
