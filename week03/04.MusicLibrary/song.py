import json


class Song:

    def __init__(self, title, artist, album, length):
        self.validate_length(length)
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length 

    def __hash__(self):
        return hash(self.title + self.artist + self.album)

    def get_length(self):
        return self.length

    @staticmethod
    def validate_length(length=None):
        list_of_length_elements = length.split(":")
        if len(list_of_length_elements) == 3:
            if len(list_of_length_elements[0]) == 1:
                raise TypeError('Incorrect input!')
            if len(list_of_length_elements[1]) == 1:
                raise TypeError('Incorrect input!')
            if len(list_of_length_elements[2]) == 1:
                raise TypeError('Incorrect input!')
        if len(list_of_length_elements) > 3:
            raise TypeError('Incorrect input!')
        if len(list_of_length_elements) == 3:
            if int(list_of_length_elements[1]) > 60:
                raise TypeError('Incorrect input!')
            if int(list_of_length_elements[2]) > 60:
                raise TypeError('Incorrect input!')
        elif len(list_of_length_elements) == 2:
            if int(list_of_length_elements[0]) > 60:
                raise TypeError('Incorrect input!')
            if int(list_of_length_elements[1]) > 60:
                raise TypeError('Incorrect input!')

    def length_of_song(self, seconds=False, minutes=False, hours=False):
        all_seconds = 0
        split_length = self.length.split(":")
        if len(split_length) == 3:
            all_seconds = int(split_length[0]) * 60 * 60 + int(split_length[1]) * 60 + int(split_length[2])
            all_minutes = int(split_length[0]) * 60 + int(split_length[1])
            all_hours = int(split_length[0])
        elif len(split_length) == 2:
            all_seconds = int(split_length[0]) * 60 + int(split_length[1])
            all_minutes = int(split_length[0])

        if seconds is True:
            return all_seconds
        if minutes is True:
            return all_minutes
        if hours is True:
            return all_hours

    def length_to_string(self):
        return self.length


def main():
    pass
if __name__ == '__main__':
    main()
