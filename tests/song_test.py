import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Invisible Touch", "Genesis")

    def test_song_has_artist(self):
        self.assertEqual("Genesis", self.song.artist)
