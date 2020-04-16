from song import Song
import random
import json


class Playlist:
    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.playedSongs = []
        self.current_song = None
        self.index_of_song = 0

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.songs.append(song)

    def total_length(self):
        Sum = 0
        for song in self.songs:
            Sum = Sum + song.length_of_song(seconds=True)
        hours = int(Sum // 3600)
        minutes = int((Sum % 3600) / 60)
        seconds = int((Sum % 3600) % 60)
        string_representation = ''
        if len(str(hours)) == 1:
            string_hours = '0' + str(hours)
        else:
            string_hours = str(hours)
        if len(str(minutes)) == 1:
            string_minutes = '0' + str(minutes)
        else:
            string_minutes = str(minutes)
        if len(str(seconds)) == 1:
            string_seconds = '0' + str(seconds)
        else:
            string_seconds = str(seconds)
        string_representation = string_hours + ":" + string_minutes + ":" + string_seconds
        return string_representation

    def artist(self):
        artistDict = {}
        for song in self.songs:
            if song.artist in artistDict:
                artistDict[song.artist] += 1
            else:
                artistDict[song.artist] = 1
        return artistDict

    def next_song(self):
        if self.repeat is True and self.shuffle is False:
            self.current_song = self.songs[self.index_of_song]
            self.index_of_song += 1
            if self.index_of_song == len(self.songs):
                self.index_of_song = 0
                return self.songs[self.index_of_song]
            else:
                return self.songs[self.index_of_song]

        if self.repeat is True and self.shuffle is True:
            shuffled_songs = [self.songs[i] for i in range(len(self.songs))]
            random.shuffle(shuffled_songs)
            self.current_song = shuffled_songs[self.index_of_song]
            self.index_of_song += 1
            if self.index_of_song == len(self.songs):
                self.index_of_song = 0
                return shuffled_songs[self.index_of_song]
            else:
                return shuffled_songs[self.index_of_song]

        if self.repeat is False and self.shuffle is True:
            while len(self.songs) > 0:
                self.current_song = random.choice(self.songs)
                self.songs.remove(self.current_song)
                return self.current_song

        if self.repeat is False and self.shuffle is False:
            self.current_song = self.songs[self.index_of_song]
            self.index_of_song += 1
            return self.songs[self.index_of_song]

    def save(self):
        playlistName = self.name.replace(' ', '-')
        data = {
        "name": self.name,
        "songs": [song.__dict__ for song in self.songs]
        }
        with open(f'playlist-data/{playlistName}.json', 'w') as f:
            json.dump(data, f)

    def load(self, path):
        with open(path, 'r') as f:
            printedPlaylist = json.load(f)
            return printedPlaylist


def main():
    pass


if __name__ == '__main__':
    main()
