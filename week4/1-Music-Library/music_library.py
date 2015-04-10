import datetime
import random
from prettytable import PrettyTable
import json
import mutagen
import os


class Song:

    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def title(self):
        return self.__title

    def artist(self):
        return self.__artist

    def album(self):
        return self.__album

    def to_seconds(self):
        if len(self.time) == 2:
            return self.time[0]*60 + self.time[1]
        return self.time[0]*3600 + self.time[1]*60 + self.time[2]

    def to_minutes(self):
        if len(self.time) == 2:
            return self.time[0] + self.time[1]
        return self.time[0]*60 + self.time[1]

    def to_hours(self):
        if len(self.time) == 3:
            if self.time[1] >= 60:
                return self.time[0] + 1
            return self.time[0]
        return 0

    def length(self, seconds=False, minutes=False, hours=False):
        self.time = [int(x.strip()) for x in self.__length.split(":")]
        if seconds:
            return self.to_seconds()
        elif minutes:
            return self.to_minutes()
        elif hours:
            return self.to_hours()
        return self.__length

    def __str__(self):
        return "{} - {}({}) : {}".format(
            self.artist(), self.title(), self.album(), self.length())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title() == other.title() and \
               self.artist() == other.artist() and \
               self.album() == other.album() and \
               self.length() == other.length()

    def __hash__(self):
        return hash(self.__str__())


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.fresh_playlist = True
        self.current_song = None
        self.played_songs = set()

    def has_song(self, song):
        return song in self.songs

    def add_song(self, song):
        if isinstance(song, Song):
            if self.fresh_playlist:
                self.current_song = song
                self.fresh_playlist = False
            self.songs.append(song)
        else:
            raise TypeError("The song in not instance of class Song")

    def remove_song(self, song):
        if self.has_song(song):
            self.songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        total_seconds = sum([song.length(seconds=True) for song in self.songs])
        return str(datetime.timedelta(seconds=total_seconds))

    def artists(self):
        result = {}
        for song in self.songs:
            if song.artist() in result:
                result[song.artist()] += 1
            else:
                result[song.artist()] = 1
        return result

    def next_song(self):
        if self.fresh_playlist:
            raise Exception("No songs in the playlist!")
        if self.shuffle:
            song = random.choice(self.songs)
            while song in self.played_songs:
                song = random.choice(self.songs)
            self.played_songs.add(song)
            if len(self.played_songs) == len(self.songs):
                self.played_songs = set()
            self.current_song = song
            return self.current_song
        if self.current_song != self.songs[len(self.songs) - 1]:
            self.current_song = \
                self.songs[self.songs.index(self.current_song) + 1]
            return self.current_song
        else:
            if self.repeat:
                self.current_song = self.songs[0]
                return self.current_song
            else:
                raise Exception("Playlist reached the end.")

    def pprint_playlist(self):
        table = PrettyTable(["Artist", "Song", "Length"])
        for song in self.songs:
            table.add_row([song.artist(), song.title(), song.length()])
        print(table)

    def generate_json_name(self):
        dasherized_name = self.name.replace(" ", "-") + ".json"
        return dasherized_name

    def save(self):
        data = {
               "name": self.name,
               "songs": [song.__dict__ for song in self.songs]
               }
        with open(self.generate_json_name(), 'w') as f:
            f.write(json.dumps(data, indent=True))

    @staticmethod
    def load(file_name):
        with open(file_name, 'r') as f:
            content = json.load(f)
            playlist = Playlist(content["name"])
            for song in content["songs"]:
                new_song = Song(
                    artist=song["_Song__artist"], title=song["_Song__title"], album=song["_Song__album"], length=song["_Song__length"])
                playlist.add_song(new_song)
            return playlist


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def get_data(self, data):
        song_data = {}
        try:
            song_data["artist"] = data["TPE1"].text[0]
        except:
            song_data["artist"] = "Unknown Artist"
        try:
            song_data["album"] = data["TALB"].text[0]
        except:
            song_data["album"] = "Unknown Album"
        try:
            song_data["title"] = data["TIT2"].text[0]
        except:
            song_data["title"] = "Unknown Title"
        try:
            song_data["length"] = str(
                datetime.timedelta(seconds=data.info.length//1))[2:]
        except:
            song_data["length"] = "Unknown"
        return song_data

    def generate_playlist(self, name):
        playlist = Playlist(name)
        songs = [mp3 for mp3 in os.listdir(self.path) if mp3.endswith(".mp3")]
        for song in songs:
            data = mutagen.File(self.path + song)
            song_data = self.get_data(data)
            new_song = Song(
                artist=song_data["artist"], title=song_data["title"], album=song_data["album"], length=song_data["length"])
            playlist.add_song(new_song)
        return playlist
