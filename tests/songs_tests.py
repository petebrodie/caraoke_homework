import unittest

from tests.guest_test import TestGuest
from tests.room_test import TestRoom
from tests.song_test import TestSong

class TestSongs (unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Wonderwall")
        self.song_2 = Song("Mr Brightside")
        self.song_3 = Song("Sweet child of mine")

    def test_add_songs_to_rooms(self):
        self.assertEqual("Wonderwall", self.append.room_number_1)