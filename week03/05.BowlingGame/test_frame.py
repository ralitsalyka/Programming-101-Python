import unittest
from frame import Frame


class TestFrameClass(unittest.TestCase):
    def test_raises_exception_for_first_chance(self):
        exc = None

        try:
            frame = Frame(1.5, 2)

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')

    def test_raises_exception_for_second_chance(self):
        exc = None

        try:
            frame = Frame(1, 2.5)

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')

    def test_raises_exception_for_first_chance_if_it_is_negative(self):
        exc = None

        try:
            frame = Frame(-1, 2)

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')

    def test_raises_exception_for_seocnd_chance_if_it_is_negative(self):
        exc = None

        try:
            frame = Frame(1, -2)

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')

    def test_raises_exception_for_first_chance_if_it_is_bigger_than_ten(self):
        exc = None

        try:
            frame = Frame(11, 2)

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')

    def test_raises_exception_for_second_chance_if_it_is_bigger_than_ten(self):
        exc = None

        try:
            frame = Frame(1, 20)

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect input!')

    def test_get_first_chance_fucntion(self):
        frame = Frame(1, 2)

        result = frame.get_first_chance()

        self.assertEqual(result, 1)

    def test_get_second_chance_fucntion(self):
        frame = Frame(1, 2)

        result = frame.get_second_chance()

        self.assertEqual(result, 2)

    def test_if_two_frames_are_equal(self):
        frame1 = Frame(1, 2)
        frame2 = Frame(1, 2)

        self.assertEqual(frame1, frame2)

    def test_string_representation_if_it_strike(self):
        frame = Frame(10, 0)
        self.assertEqual(str(frame), 'Strike')

    def test_string_representation_if_it_is_stroke(self):
        frame = Frame(3, 7)
        self.assertEqual(str(frame), 'Spare')

    def test_string_representation_if_it_is_open_frame(self):
        frame = Frame(3, 4)
        self.assertEqual(str(frame), 'Open Frame')


if __name__ == '__main__':
    unittest.main()
