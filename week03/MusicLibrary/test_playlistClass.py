import unittest
from song import Song
from playlistClass import Playlist


class TestPlayListFunction(unittest.TestCase):
    def test_if_added_song_works_correctly_in_playist(self):
        playlist = Playlist("For Code", False, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44")]
        song = Song("Metallica", "Nothing Else Matter", "Metallica", "3:44")

        playlist.add_song(song)

        self.assertEqual(playlist.songs, [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Metallica","Nothing Else Matter","Metallica","3:44")])

    def test_added_songs_work_correctly_in_playist(self):
        playlist = Playlist("For Code", False, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44")]
        songs = [Song("Metallica", "Nothing Else Matter", "Metallica", "3:44"), Song("Happy", "Happy", "Happy", "3:45")]

        playlist.add_songs(songs)

        self.assertEqual(playlist.songs, [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Metallica", "Nothing Else Matter", "Metallica", "3:44"), Song("Happy", "Happy", "Happy", "3:45")])

    def test_remove_song_work_correctly_in_playist(self):
        playlist = Playlist("For Code", False, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Metallica", "Nothing Else Matter", "Metallica", "3:44")]
        song = Song("Metallica", "Nothing Else Matter", "Metallica", "3:44")

        playlist.remove_song(song)

        self.assertEqual(playlist.songs, [Song("Odin", "Manowar", "The Sons of Odin", "3:44")])

    def test_total_length_if_it_is_working(self):
        playlist = Playlist("For Code", False, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Metallica", "Nothing Else Matter", "Metallica", "3:44")]

        result = playlist.total_length()
        self.assertEqual(result, "00:07:28")

    def test_artists_if_it_is_working_correctly_for_one_song_for_each_artist(self):
        playlist = Playlist("For Code", False, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Nothing else matter", "Metallica", "Metallica", "3:44")]

        result = playlist.artist()
        self.assertEqual(result, {'Manowar': 1, 'Metallica': 1})

    def test_artists_if_it_is_working_correctly_for_two_sons_of_one_artist(self):
        playlist = Playlist("For Code", False, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Nothing else matter", "Manowar", "Metallica", "3:44")]

        result = playlist.artist()
        self.assertEqual(result, {'Manowar': 2})

    def test_next_song_if_it_is_repeat_False_and_shuffled_False(self):
        playlist = Playlist("For Code", False, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Happy", "Happy", "Happy", "3:44")]

        result = playlist.next_song()
        self.assertEqual(result, Song("Happy", "Happy", "Happy", "3:44"))

    def test_next_song_if_it_is_repeat_Ture_and_shuffled_False(self):
        playlist = Playlist("For Code", True, False)
        playlist.songs = [Song("Odin", "Manowar", "The Sons of Odin", "3:44"), Song("Nothing else matter", "Manowar", "Metallica", "3:44"), Song("Happy", "Happy", "Happy", "3:44")]

        result = playlist.next_song()
        self.assertEqual(result, Song("Nothing else matter", "Manowar", "Metallica", "3:44"))

if __name__ == '__main__':
    unittest.main()