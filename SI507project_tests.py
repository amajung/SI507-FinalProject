import unittest
from SI507project_tools import getArtistSongs, Song, Playlist

class TestFunctions(unittest.TestCase):
    def test_getArtistSongs(self):
        # Test if object returned is a dictionary
        self.assertEqual(<class 'dictionary'>, type(getArtistSongs('Ariana Grande')))

    def test_Song(self):
        itunesResult = getArtistSongs('Ariana Grande')
        songs = [ Song(d) for d in itunesResult['results'] ]

        # Test class instance of Song
        self.assertEqual(songs[0].artistName, "Ariana Grande")


    def test_Playlist(self):
        itunesResult = getArtistSongs('dvsn')
        songs = [ Song(d) for d in itunesResult['results'] ]

        # Test class instance song
        p = Playlist()
        self.assertEqual(len(p.songs), 0)

        # Test class method addSong and class instance songs
        p.addSong(songs[0])
        self.assertEqual(len(p.songs), 1)


if __name__ == '__main__':
    unittest.main()
