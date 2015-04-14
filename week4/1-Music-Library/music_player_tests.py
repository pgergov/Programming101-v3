import unittest
from music_library import Song, Playlist, MusicCrawler


class MusicPlayerTest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.playlist = Playlist("The sex and the city")

    def test_str(self):
        self.assertEqual(str(
            self.song), "Manowar - Odin (The Sons of Odin) : 3:44")

    def test_adding_song_in_playlist(self):
        self.playlist.add_song(self.song)
        self.assertTrue(self.playlist.has_song(self.song))

    def test_removing_song(self):
        self.playlist.add_song(self.song)
        self.playlist.remove_song(self.song)
        self.assertFalse(self.playlist.has_song(self.song))

    def test_total_length(self):
        song = Song("Baby", "J.Beiber", "Gay Album", "3:50")
        self.playlist.add_songs([self.song, song])
        self.assertEqual(self.playlist.total_length(), "0:07:34")

    def test_artists(self):
        song = Song("Baby", "J.Beiber", "Gay Album", "3:50")
        self.playlist.add_songs([self.song, song])
        self.assertEqual(
            self.playlist.artists(), {'Manowar': 1, "J.Beiber": 1})

    def test_play_next_song_in_empty_playlist(self):
        with self.assertRaises(Exception):
            self.playlist.next_song()

    def test_play_next_song_if_there_is_only_one_with_repeat_False(self):
        self.playlist.add_song(self.song)
        with self.assertRaises(Exception):
            self.playlist.next_song()

    def test_next_songs_with_repeat_False(self):
        random_song = Song("Random", "Manowar", "The Sons of Odin", "1:30:44")
        another_song = Song("Anther", "Manowar", "The Sons of Odin", "1:30:44")
        self.playlist.add_songs([self.song, random_song, another_song])
        self.assertEqual(self.playlist.next_song(), random_song)
        self.assertEqual(self.playlist.next_song(), another_song)
        with self.assertRaises(Exception):
            self.playlist.next_song()

    def test_next_songs_with_repeat_True(self):
        random_song = Song("Random", "Random", "The Sons of Odin", "3:44")
        another_song = Song("Anther", "Kanye West", "Heartless", "4:20")
        song = Song("Baby", "J.Beiber", "Gay Album", "3:50")
        p = Playlist("p", repeat=True)
        p.add_songs([self.song, random_song, another_song, song])
        self.assertEqual(p.next_song(), random_song)
        self.assertEqual(p.next_song(), another_song)
        self.assertEqual(p.next_song(), song)
        self.assertEqual(p.next_song(), self.song)

    def test_generate_json_name(self):
        self.assertEqual(
            self.playlist.generate_json_name(), "The-sex-and-the-city.json")

    def test_save_load(self):
        song = Song("Baby", "J.Beiber", "Gay Album", "3:50")
        self.playlist.add_songs([self.song, song])
        self.playlist.save()

        g = Playlist.load("The-sex-and-the-city.json")
        self.assertEqual(self.playlist.songs, g.songs)
        self.assertEqual(g.name, "The sex and the city")

    def test_crawler_generate_ability(self):
        crawler = MusicCrawler("/home/hdimitrova/Music/Linkin Park - Meteora")
        playlist = crawler.generate_playlist("Meteora")
        self.assertEqual(playlist.total_length(), '0:36:41')

    def test_crawlered_playlist_save(self):
        crawler = MusicCrawler("/home/hdimitrova/Music/Linkin Park - Meteora")
        playlist = crawler.generate_playlist("Linkin Park - Meteora")
        playlist.save()
        playlist.pprint_playlist()

if __name__ == '__main__':
    unittest.main()
