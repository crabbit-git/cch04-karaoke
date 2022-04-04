import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Beat It", "Michael Jackson")
        self.song2 = Song("Hip To Be Square", "Huey Lewis And The News")
        self.song3 = Song("Shake It Off", "Taylor Swift")
        self.song4 = Song("Sunshine On Leith", "The Proclaimers")
        self.playlist = [self.song1, self.song2, self.song3]
        self.guest1 = Guest("Dave")
        self.guest2 = Guest("Pat", self.song2)
        self.guest3 = Guest("Dougray", self.song4)

    def test_guest_is_philistine(self):
        self.assertEqual(None, self.guest1.fav_song)
    
    def test_guest_has_taste(self):
        self.guest2.fav_song = self.song2
        self.assertEqual(self.song2, self.guest2.fav_song)

    def test_guest_is_skint(self):
        self.assertEqual(0, self.guest1.cash)
    
    def test_guest_can_lift_cash(self):
        self.guest1.lift_cash(50)
        self.assertEqual(50, self.guest1.cash)

    def test_guest_can_be_boisterous(self):
        self.assertEqual("YAAAAAAASSSSS!", self.guest2.celebrate(self.playlist))
    
    def test_guest_can_be_disappointed(self):
        self.assertEqual("Aww...", self.guest3.celebrate(self.playlist))
    
    def test_guest_does_not_know_playlist(self):
        self.assertEqual(None, self.guest1.celebrate())
