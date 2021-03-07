import unittest

from classes.guests import guests

class GuestTest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest()

    def test_guest_name(self):
        self.guest.name()
        self.assertEqual()