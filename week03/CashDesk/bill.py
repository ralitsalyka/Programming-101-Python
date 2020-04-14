
class Bill:

    def __init__(self, amount):
        self.validate_amount(amount)
        self.amount = amount

    def __str__(self):
        return f'A {self.amount}$ bill'

    def __repr__(self):
        return f"'A {self.amount}$ bill'"

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __gt__(self, other):
        return self.amount > other.amount

    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount, int):
            raise TypeError('Amount must be integer!')
        if amount < 0:
            raise ValueError("Amount must be positive!")
