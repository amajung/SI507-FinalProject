import requests
import json
from IPython.display import Audio, Image

# Function gets data from user input of artist name
def getArtistSongs(artistName):
    r = requests.get('https://itunes.apple.com/search', params = {
        'term': artistName,
        'entity': 'song'
    })
    return json.loads(r.text)

# Class for songs
class Song():
    def __init__(self, d):
        self.d = d
        self.artworkURL = d['artworkUrl100']
        self.trackName = d['trackName']
        self.previewURL = d['previewUrl']
        self.artist = d['artistName']

    # Displays image artwork, trackname, and audio preview
    def displaySong(self):
        display(Image(self.artworkURL))
        display('"{}" by {}'.format(self.trackName, self.artist))
        display(Audio(self.previewURL))

    # Get dictionary for song
    def serialize(self):
        return self.d

    # Print statement
    def __str__(self):
        return '"{}" by {}'.format(self.trackName, self.artist)

# Class for playlist
class Playlist():
    def __init__(self):
        self.songs = []

    # Adds song to playlist
    def addSong(self, song):
        self.songs.append(song)

    # DIsplays songs in playlist
    def displayPlaylist(self):
        for song in self.songs:
            song.displaySong()

    # Write to cache file
    def writeToFile(self, filename):
        f = open(filename, 'w')
        f.write(json.dumps(self.serialize()))
        f.close()

    # Puts information of all songs into list
    def serialize(self):
        return [ song.serialize() for song in self.songs ]
