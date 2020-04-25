import unittest
from frame import Frame
from bowlingGame import BowlingGame


class TestBowlingGameClass(unittest.TestCase):
    def test_raises_exception_if_it_is_not_list(self):
        exc = None

        try:
            list_of_pins = BowlingGame("123456")

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')

    def test_raises_exception_for_less_than_ten(self):
        exc = None
        try:
            len_of_list_of_pins = BowlingGame([1, 2, 3, 45])

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')


    def test_raises_exception_for_more_than_twenty(self):
        exc = None
        try:
            len_of_list_of_pins = BowlingGame([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7, 8])

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')
    
    def test_check_is_it_correctly_create_frames_list_full_of_10(self):
        game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

        result = game.create_frames()

        self.assertEqual(result, [Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0)])

    def test_check_is_it_correctly_create_frames_list(self):
        game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])

        result = game.create_frames()

        self.assertEqual(result, [Frame(1, 4), Frame(4, 5), Frame(6, 3), Frame(5, 1), Frame(1, 0), Frame(1, 7), Frame(3, 6), Frame(4, 3), Frame(2, 1), Frame(6, 2)])

    def test_calculate_function_only_with_strikes(self):
        game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        game.create_frames()
        result = game.calculate_game_points()
        self.assertEqual(result, 300)

    def test_calculate_function_only_with_open_frames(self):
        game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
        game.create_frames()
        result = game.calculate_game_points()
        self.assertEqual(result, 65)

    def test_calculate_function_only_with_zero(self):
        game = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        game.create_frames()
        result = game.calculate_game_points()
        self.assertEqual(result, 0)

    def test_calculate_function_only_with_spares(self):
        game = BowlingGame([1, 9, 4, 6, 6, 4, 5, 5, 1, 9, 1, 9, 3, 7, 4, 6, 2, 8, 6, 4])
        game.create_frames()
        result = game.calculate_game_points()
        self.assertEqual(result, 122)



if __name__ == '__main__':
    unittest.main()
