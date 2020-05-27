import unittest
from bill import Bill


class TestBillClass(unittest.TestCase):
    def test_raises_exception_when_amount_is_not_int(self):
        exc = None

        try:
            bill = Bill('10')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Amount must be integer!')

    def test_raises_exception_when_amount_is_not_positive(self):
        exc = None

        try:
            bill = Bill(-10)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Amount must be positive!')

    def test_string_representation(self):
        bill = Bill(10)

        self.assertEqual(str(bill), 'A 10$ bill')

    def test_if_two_bills_are_equal(self):
        bill1 = Bill(10)
        bill2 = Bill(10)

        self.assertEqual(bill1, bill2)

    def test_int_representation_of_bill(self):
        bill1 = Bill(10)

        self.assertEqual(int(bill1), 10)

    def test_hash_dunder_bill(self):
        bill = Bill(10)

        self.assertEqual(hash(bill), 10)


if __name__ == '__main__':
    unittest.main()
