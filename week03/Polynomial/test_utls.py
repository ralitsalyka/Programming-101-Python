import unittest
from utls import find_coefficients 
from utls import power_find
from utls import create_part_derive
from utls import create_list_of_derive


class TestFindCons(unittest.TestCase):
    def test_find_coefficients(self):
        string = '2*x^3'

        result = find_coefficients(string)

        self.assertEqual(result, '2')

    def test_find_coefficients_if_it_is_only_x(self):
        string = 'x'

        result = find_coefficients(string)

        self.assertEqual(result, '1')

    def test_find_power_if_it_bigger_then_one(self):
        string = '2*x^3'

        result = power_find(string)

        self.assertEqual(result, '3')

    def test_find_power_if_it_is_only_x(self):
        string = 'x'

        result = power_find(string)

        self.assertEqual(result, '1')

    def test_find_derive_if_it_is_only_coeficient(self):
        string = '2'

        result = create_part_derive(string)

        self.assertEqual(result, '0')

    def test_find_derive_if_it_is_only_x(self):
        string = 'x'

        result = create_part_derive(string)

        self.assertEqual(result, '1')

    def test_find_derive_if_it_is_x_and_coefficient(self):
        string = '2x'

        result = create_part_derive(string)

        self.assertEqual(result, '2')

    def test_find_derive_if_it_is_x_and_power(self):
        string = 'x^3'

        result = create_part_derive(string)

        self.assertEqual(result, '3x^2')

    def test_find_derive_if_if_is_only_coefficient(self):
        string = '2'

        result = create_part_derive(string)

        self.assertEqual(result, '0')

    def test_find_derive_if_it_is_x_and_cefficient_and_power(self):
        string = '6x^2'

        result = create_part_derive(string)

        self.assertEqual(result, '12x')

    def test_find_derive_if_it_is_sum(self):
        string = '2x+2'

        result = create_list_of_derive(string)

        self.assertEqual(result, ['2', '0'])

    def test_find_if_it_is_only_one_coefficient_in_list(self):
        string = '2'

        result = create_list_of_derive(string)

        self.assertEqual(result, ['0'])


if __name__ == '__main__':
    unittest.main()
