import unittest
from SI507project_tools import getArtistSongs, Song, Artist, Genre

class TestFunctions(unittest.TestCase):

    def test_getArtistSongs(self):
        # Test if object returned is a list of song dictionaries
        self.assertEqual( type([]), type(getArtistSongs('Ariana Grande')) )
        self.assertEqual( type({}), type(getArtistSongs('Ariana Grande')[0]))

    def test_Song(self):
        itunesResult = getArtistSongs('Ariana Grande')
        song_query = '7 rings'

        # Test if data received from API is correct
        for d in itunesResult:
            if d['trackName'] == song_query:
                title = d['trackName']
                artist = d['artistName']
                genre = d['primaryGenreName']
                artworkUrl = d['artworkUrl100']
                previewUrl = d['previewUrl']

        song = Song(title=title, artworkUrl=artworkUrl, previewUrl=previewUrl, artist_name=artist, genre_name=genre)

        # Test variable instances for class Song
        self.assertEqual( song.title, '7 rings' )
        self.assertEqual( song.artworkUrl, 'https://is3-ssl.mzstatic.com/image/thumb/Music114/v4/ee/7b/f4/ee7bf4cc-a3a4-406d-3367-6d871d54a87f/source/100x100bb.jpg' )
        self.assertEqual( song.artist_name, 'Ariana Grande' )
        self.assertEqual( song.genre_name, 'Pop' )

    def test_Artist(self):
        itunesResult = getArtistSongs('dvsn')
        song_query = 'Body Smile'

        # Test if data received from API is correct
        for d in itunesResult:
            if d['trackName'] == song_query:
                name = d['artistName']

        # Test variable instances for class Artist
        artist = Artist(name=name)

        self.assertEqual(artist.name, 'dvsn')

    def test_Artist(self):
        itunesResult = getArtistSongs('dvsn')
        song_query = 'Body Smile'

        # Test if data received from API is correct
        for d in itunesResult:
            if d['trackName'] == song_query:
                name = d['primaryGenreName']

        # Test variable instances for class Genre
        genre = Genre(name=name)

        self.assertEqual(genre.name, 'R&B/Soul')


if __name__ == '__main__':
    unittest.main()
