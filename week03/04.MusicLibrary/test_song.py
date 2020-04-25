import unittest
from song import Song

class TestClassSong(unittest.TestCase):
    def test_raises_exception_when_length_of_seconds_are_bigger_than_60(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="03:65")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')

    def test_raises_exception_when_length_of_minutes_are_bigger_than_60(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="65:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')

    def test_raises_exception_when_length_of_seconds_are_bigger_than_60_where_there_is_hours(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:44:64")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')

    def test_raises_exception_when_length_of_minutes_are_bigger_than_60_where_there_is_hours(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:64:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')

    def test_raises_if_length_of_seconds_is_less_than_two_numbers(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:04:4")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')
    def test_raises_if_length_of_minutes_is_less_than_two_numbers(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:4:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')
    def test_raises_if_length_of_hours_is_less_than_two_numbers(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="4:04:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')

    def test_raises_if_count_of_is_more_than_three_elements(self):
        exc = None

        try:
            song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="12:4:04:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input!')

    def test_string_representation(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:44")
        self.assertEqual(str(song), 'Manowar - Odin from The Sons of Odin - 04:44')

    def test_if_two_song_are_equal(self):
        song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:44")
        song2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:44")
        self.assertEqual(song1, song2)

    def test_if_length_return_correctly_all_seconds(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:44")
        result = song.length_of_song(seconds=True)

        self.assertEqual(result, 284)

    def test_if_length_return_correctly_all_seconds_in_three_elements(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="01:01:04")
        result = song.length_of_song(seconds=True)

        self.assertEqual(result, 3664)

    def test_if_length_return_correctly_all_minutes(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="04:44")
        result = song.length_of_song(minutes=True)

        self.assertEqual(result, 4)

    def test_if_length_return_correctly_all_minutes_in_three_elements(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="02:04:44")
        result = song.length_of_song(minutes=True)

        self.assertEqual(result, 124)

    def test_if_length_return_correctly_all_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="02:04:44")
        result = song.length_of_song(hours=True)

        self.assertEqual(result, 2)

    def test_if_return_correctly_string_representation_of_length(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="02:04:44")
        result = song.length_to_string()

        self.assertEqual(result, '02:04:44')



if __name__ == '__main__':
    unittest.main()
