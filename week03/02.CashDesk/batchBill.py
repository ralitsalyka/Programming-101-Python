from bill import Bill


class BatchBill:
    def __init__(self, Bills):
        self.Bills = Bills

    def __len__(self):
        return len(self.Bills)

    def __getitem__(self, index):
        return self.Bills[index]

    def total(self):
        Sum = 0
        for bill in self.Bills:
            Sum = Sum + int(bill)
        return Sum


def main():
    pass


if __name__ == '__main__':
    main()
