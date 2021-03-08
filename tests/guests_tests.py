import unittest

from tests.guest_test import TestGuest
from tests.room_test import TestRoom
from tests.song_test import TestSong

class GuestTest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Pete")

    def test_guest_name(self):
        self.assertEqual("Pete")

    def test_add_guest_to_room(self):
        self.room_1.add_guest(self.guest)
        self.assertEqual(1, len(self.room_1.songs))


