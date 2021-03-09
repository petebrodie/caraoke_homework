import unittest

from classes.guests import Guest


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Pete")

    def test_guest_name(self):
        self.assertEqual("Pete", self.guest.name)

    


