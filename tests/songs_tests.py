import unittest

from tests.guest_test import TestGuest
from tests.room_test import TestRoom
from tests.song_test import TestSong

class TestSongs (unittest.TestCase):
    def setUp(self):
        song_1 = song("Hey Ya!", "Pop")

    def test_song_has_name(self):
        self.assertEqual("Hay Ya!", self.song_1.name)

    def test_song_has_genre(self):
        self.assertEqual("Pop", self.song_1.genre)
        
        
        
        
        
        
    #     self.song_1 = Song("Wonderwall")
    #     self.song_2 = Song("Mr Brightside")
    #     self.song_3 = Song("Sweet child of mine")

    # def test_add_songs_to_rooms(self):
    #     self.assertEqual("Wonderwall", self.append.room_number_1)