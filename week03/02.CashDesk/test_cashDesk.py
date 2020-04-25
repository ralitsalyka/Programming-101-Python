import unittest
from bill import Bill
from batchBill import BatchBill
from cashDesk import CashDesk


class Test_CashBill_Class(unittest.TestCase):
    def test_take_money_function_by_using_total_batch_test(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        desk = CashDesk()
        desk.take_money(batch)
        result = desk.total()
        self.assertEqual(result, 180)

    def test_take_money_function_by_using_total_bill_only_test(self):
        bill = Bill(10)
        desk = CashDesk()
        desk.take_money(bill)
        result = desk.total()
        self.assertEqual(result, 10)

    def test_take_money_function_by_using_total_bill_and_batch_test(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        bill = Bill(10)
        desk = CashDesk()
        desk.take_money(bill)
        desk.take_money(batch)
        result = desk.total()
        self.assertEqual(result, 190)

    def test_total_fuction(self):
        desk=CashDesk()
        result=desk.total()
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()