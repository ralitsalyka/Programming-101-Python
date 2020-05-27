from frame import Frame


class BowlingGame:
    def __init__(self, pins):
        self.validate_pins(pins)
        self.pins = pins
        self.frames = []
        self.result = 0

    def get_result(self):
        return self.result

    def create_frames(self):
        length = len(self.pins)
        i = 0
        while i < length:
            if self.pins[i] == 10:
                self.frames.append(Frame(self.pins[i], 0))
                i = i + 1
            else:
                self.frames.append(Frame(self.pins[i], self.pins[i + 1]))
                i = i + 2
        if length % 2 != 0:
            if self.pins[i] == 10:
                self.frames.append(Frame(self.pins[i], 0))
                if self.pins[i + 1] == 10:
                    self.frames.append(Frame(self.pins[i + 1], 0))
            else:
                self.frames.append(Frame(self.pins[i], 0))
        return self.frames

    def calculate_game_points(self):
        length_frames = len(self.frames)
        i = 0
        while i < length_frames - 1:
            if str(self.frames[i]) == 'Open Frame':
                self.result += self.frames[i].get_first_chance() + self.frames[i].get_second_chance()
            elif str(self.frames[i]) == 'Strike':
                self.result += self.frames[i].get_first_chance()
                if str(self.frames[i + 1]) == 'Strike':
                    self.result += self.frames[i + 1].get_first_chance()
                    if i + 2 < length_frames:
                        self.result += self.frames[i + 2].get_first_chance()
                else:
                    self.result += self.frames[i + 1].get_first_chance()
                    self.result += self.frames[i + 1].get_second_chance()
            elif str(self.frames[i]) == 'Spare':
                self.result += self.frames[i].get_first_chance()
                self.result += self.frames[i].get_second_chance()
                self.result += self.frames[i + 1].get_first_chance()
            i = i + 1
        if str(self.frames[length_frames - 1]) == 'Open Frame' and str(self.frames[length_frames - 3]) != 'Spare':
            self.result += self.frames[i].get_first_chance() + self.frames[i].get_second_chance()
        if str(self.frames[length_frames - 1]) == 'Strike':
            return self.result - 20
        return self.result

    @staticmethod
    def validate_pins(pins):
        if not isinstance(pins, list):
            raise TypeError('Incorrect input!')
        if len(pins) < 10:
            raise ValueError('Incorrect input!')
        if len(pins) > 21:
            raise ValueError('Incorrect input!')


def main():
    game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    print(game.create_frames())
    print(game.calculate_game_points())


if __name__ == '__main__':
    main()
