
class Frame:
    def __init__(self, first_chance=0, second_chance=0):
        self.validation_of_chances(first_chance, second_chance)
        self.first_chance = first_chance
        self.second_chance = second_chance

    def get_first_chance(self):
        return self.first_chance

    def get_second_chance(self):
        return self.second_chance

    def __eq__(self, other):
        return self.first_chance == other.first_chance and self.second_chance == other.second_chance

    def __str__(self):
        if self.first_chance == 10:
            return f'Strike'
        if self.first_chance + self.second_chance == 10:
            return f'Spare'
        if self.first_chance + self.second_chance < 10:
            return f'Open Frame'

    def __repr__(self):
        return f'[{self.first_chance}, {self.second_chance}]'

    @staticmethod
    def validation_of_chances(first_chance, second_chance):
        if not isinstance(first_chance, int):
            raise TypeError('Incorrect input!')
        if not isinstance(second_chance, int):
            raise TypeError('Incorrect input!')
        if first_chance < 0:
            raise ValueError('Incorrect input!')
        if second_chance < 0:
            raise ValueError('Incorrect input!')
        if first_chance > 10:
            raise ValueError('Incorrect input!')
        if second_chance > 10:
            raise ValueError('Incorrect input!')
