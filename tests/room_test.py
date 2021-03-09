import unittest

from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestRoom (unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(3)
        self.song_1 = Song("Hey Ya!", "Pop")
        self.guest = Guest("Pete") 

    def test_can_add_song(self):
        self.room_1.can_add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))

        #test can add guest
    def test_can_add_guest(self):
        self.room_1.can_add_guest(self.guest)
        self.assertEqual(1, len(self.room_1.guests))

    def test_can_remove_guest(self):
        self.room_1.can_add_guest(self.guest)
        self.room_1.can_remove_guest(self.guest)
        self.assertEqual(0, len(self.room_1.guests))

