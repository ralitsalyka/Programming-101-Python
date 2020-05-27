import unittest
from bill import Bill
from batchBill import BatchBill


class Test_BatchBill_Class(unittest.TestCase):
    def test_string_representation(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        result = len(batch)

        self.assertEqual(result, 4)

    def test_index_of_some_Bill_in_BatchBill(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        index = 3
        result = batch[index]

        self.assertEqual(result, Bill(100))

    def test_total_function(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        result = batch.total()

        self.assertEqual(result, 180)


if __name__ == '__main__':
    unittest.main()
