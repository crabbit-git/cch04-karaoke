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
    
    def test_room_is_empty(self):
        self.assertEqual(0, len(self.room.patrons))
    
    def test_room_can_check_in_guest(self):
        self.room.check_in(self.group)
        self.assertEqual(4, len(self.room.patrons))
        self.assertEqual(self.group, self.room.patrons)
