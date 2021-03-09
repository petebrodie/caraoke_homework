import unittest

from classes.songs import Song

class TestSong (unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Hey Ya!", "Pop")

    def test_song_has_name(self):
        self.assertEqual("Hey Ya!", self.song_1.song)

    def test_song_has_genre(self):
        self.assertEqual("Pop", self.song_1.genre)
        
        
        
        
        
        