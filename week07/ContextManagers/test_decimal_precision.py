import unittest
from precision import change_precision, ChangePrecision
from decimal import Decimal


class TestValidationOfPrecision(unittest.TestCase):
    def test_if_it_is_not_int(self):
        exc = None

        try:
            precision = ChangePrecision("1.23456")

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Type Error!')
    def test_if_it_is_not_positive_num(self):
        exc = None

        try:
            precision = ChangePrecision(-1)

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Value Error!')

class TestDecimalPrecision(unittest.TestCase):
    def test_if_it_is_work_correctly_without_wtih(self):
        prec = change_precision(2)
        result = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result, Decimal('3.355452132'))

    def test_if_it_is_work_correctly_with_wtih(self):
        prec = change_precision(2)
        with prec:
            result = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result, Decimal('3.4'))

if __name__ == '__main__':
    unittest.main()