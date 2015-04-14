import datetime
import random
from prettytable import PrettyTable
import json
import mutagen
import os


class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_album(self):
        return self.album

    def to_seconds(self, time):
        if len(time) == 2:
            return time[0]*60 + time[1]
        return time[0]*3600 + time[1]*60 + time[2]

    def to_minutes(self, time):
        if len(time) == 2:
            return time[0] + time[1]
        return time[0]*60 + time[1]

    def to_hours(self, time):
        if len(time) == 3:
            if time[1] >= 60:
                return time[0] + 1
            return time[0]
        return 0

    def get_length(self, seconds=False, minutes=False, hours=False):
        if seconds or minutes or hours:
            time = [int(x.strip()) for x in self.length.split(":")]
        if seconds:
            return self.to_seconds(time)
        elif minutes:
            return self.to_minutes(time)
        elif hours:
            return self.to_hours(time)
        return self.length

    def __str__(self):
        return "{} - {} ({}) : {}".format(
            self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.get_title() == other.get_title() and \
               self.get_artist() == other.get_artist() and \
               self.get_album() == other.get_album() and \
               self.get_length() == other.get_length()

    def __hash__(self):
        return hash(self.__str__())


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.songs_location = {}
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

    def add_location(self, song, location):
        self.songs_location[song] = location

    def remove_song(self, song):
        if self.has_song(song):
            self.songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        total_seconds = sum([song.get_length(seconds=True) for song in self.songs])
        return str(datetime.timedelta(seconds=total_seconds))

    def artists(self):
        result = {}
        for song in self.songs:
            if song.get_artist() in result:
                result[song.get_artist()] += 1
            else:
                result[song.get_artist()] = 1
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
            table.add_row([song.get_artist(), song.get_title(), song.get_length()])
        print(table)

    def generate_json_name(self):
        return self.name.replace(" ", "-") + ".json"

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
                    artist=song["artist"], title=song["title"], album=song["album"], length=song["length"])
                playlist.add_song(new_song)
            return playlist


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def get_info(self, data):
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
            data = mutagen.File(self.path + "/" + song)
            info = self.get_info(data)
            new_song = Song(
                artist=info["artist"], title=info["title"], album=info["album"], length=info["length"])
            playlist.add_song(new_song)
            playlist.add_location(new_song, self.path + "/" + song)
        return playlist
