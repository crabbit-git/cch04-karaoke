import unittest

from classes.song import Song
from classes.guest import Guest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Beat It", "Michael Jackson")
        self.song2 = Song("Hip To Be Square", "Huey Lewis And The News")
        self.song3 = Song("Shake It Off", "Taylor Swift")
        self.song4 = Song("Sunshine On Leith", "The Proclaimers")
        self.playlist = [self.song1, self.song2, self.song3]
        self.room = Room(1, 6, 12, self.playlist)
        self.guest1 = Guest("Dave")
        self.guest2 = Guest("Pat", self.song2)
        self.guest3 = Guest("Miley", self.song3)
        self.guest4 = Guest("Dougray", self.song4)
        self.group = [self.guest1, self.guest2, self.guest3, self.guest4]
        self.guest1.lift_cash(10)
        self.guest2.lift_cash(100)
        self.guest3.lift_cash(30)
        self.guest4.lift_cash(80)
    
    def test_room_is_empty(self):
        self.assertEqual(0, len(self.room.patrons))

    def test_room_can_take_money(self):
        self.room.take_money(self.room.fee)
        self.assertEqual(12, self.room.takings)

    def test_room_can_filter_group(self):
        self.assertEqual(3, len(self.room.admit_guests(self.group)))

    def test_room_can_check_in_group_selectively(self):
        self.room.check_in(self.group)
        self.assertEqual(3, len(self.room.admit_guests(self.group)))
        self.assertEqual(3, len(self.room.patrons))
        self.assertEqual((self.room.fee * 3), self.room.takings)
        self.assertEqual(10, self.guest1.cash)
        self.assertEqual(88, self.guest2.cash)
        self.assertEqual(18, self.guest3.cash)
        self.assertEqual(68, self.guest4.cash)
    
    def test_group_has_no_money(self):
        skinflints = [self.guest1]
        self.room.check_in(skinflints)
        self.assertEqual(0, len(self.room.admit_guests(skinflints)))
        self.assertEqual(0, len(self.room.patrons))
        self.assertEqual(0, self.room.takings)
        self.assertEqual(10, self.guest1.cash)
