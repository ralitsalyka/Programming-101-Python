from bill import Bill
from batchBill import BatchBill


class CashDesk:
    def __init__(self):
        self.desk = {}
        self.current_money = 0

    def take_money(self, money):
        if isinstance(money, Bill):
            self.current_money += int(money)
            bill = money
            if bill in self.desk:
                self.desk[bill] += 1
            else:
                self.desk[bill] = 1
        if isinstance(money, BatchBill):
            for bill in money:
                self.current_money += int(bill)
                if bill in self.desk:
                    self.desk[bill] += 1
                else:
                    self.desk[bill] = 1

    def total(self):
        return self.current_money

    def sort_desk(self):
        print(self.desk)
        sorted_list = sorted(self.desk)
        return sorted_list

    def inspect(self):
        result = f'We have a total of {self.current_money}$ in the desk'
        result += "\nWe have the following count of bills, sorted in ascending order:"
        for bill in self.sort_desk():
            count = self.desk.get(bill)
            result += f'\n{int(bill)}$ bills - {count}'
        return result


def main():
    pass


if __name__ == '__main__':
    main()
