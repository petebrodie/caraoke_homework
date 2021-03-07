import unittest

from tests.guest_test import TestGuest
from tests.room_test import TestRoom
from tests.song_test import TestSong

class TestRooms (unittest.TestCase):
    def setUp(self):
        self.room_number_1 = Room("Pop")
        self.room_number_2 = Room("Rock")
        self.room_number_3 = Room("Hip-Hop")

        self.guest_1 = Guest("Alice", "Hey Ya!")
        self.guest_2 = Guest("Carol", "Rappers delight")
        self.guest_3 = Guest("Philip", "Livin on a prayer")
    
    def test_check_in_guest(self):
        self.assertEqual(first, second)


    def test_add_song_to_room(self):