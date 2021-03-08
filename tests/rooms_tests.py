import unittest

from tests.guest_test import TestGuest
from tests.room_test import TestRoom
from tests.song_test import TestSong

class TestRooms (unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Hey Ya!", "Pop")
        self.room_1 = Room(1)


    def test_has_room_number(self):
        self.assertEqual(1, self.room_1.number)

    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))







    #     self.room_number_1 = Room("Pop")
    #     self.room_number_2 = Room("Rock")
    #     self.room_number_3 = Room("Hip-Hop")

    #     self.guest_1 = Guest("Alice", "Hey Ya!")
    #     self.guest_2 = Guest("Carol", "Rappers delight")
    #     self.guest_3 = Guest("Philip", "Livin on a prayer")
    
    # def test_check_in_guest(self):
    #     self.assertEqual(first, second)


    # def test_add_song_to_room(self):