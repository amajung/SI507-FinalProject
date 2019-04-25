import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

import requests
import json

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./playlist.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

######### Everything above this line is important/useful setup, not problem-solving. #########

class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    artworkUrl = db.Column(db.String(64))
    previewUrl = db.Column(db.String(64))

    # Foreign keys
    artist_name = db.Column(db.Integer, db.ForeignKey('artists.id'))
    genre_name = db.Column(db.Integer, db.ForeignKey('genres.id'))

    # Relationship with other classes
    artist = db.relationship('Artist',backref='Song')
    genre = db.relationship('Genre', backref='Song')

    def __repr__(self):
        return "{}. {} by {}".format(self.id, self.title, self.artist_name)

class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


##### Helper functions #####
### For database additions
### Relying on global session variable above existing
def get_or_create_artist(artist_name):
    artist = Artist.query.filter_by(name=artist_name).first()
    if artist:
        return artist
    else:
        artist = Artist(name=artist_name)
        session.add(artist)
        session.commit()
        return artist

def get_or_create_genre(genre_name):
    genre_name = genre_name.replace('/',' and ')

    genre = Genre.query.filter_by(name=genre_name).first()
    if genre:
        return genre
    else:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()
        return genre

# Function gets data from user input of artist name
def getArtistSongs(artistName):
    r = requests.get('https://itunes.apple.com/search', params = {
        'term': artistName,
        'entity': 'song'
    })
    itunesResult = json.loads(r.text)
    return itunesResult['results'] # Returns list of

##### Set up Controllers (route functions) #####

## Main route
@app.route('/')
def index():
    mySongs = Song.query.all()
    #num_songs = len(songs)
    return render_template('index.html', mySongs=mySongs)

@app.route('/add/song/<artist>/<title>/')
def getSong(title, artist):
    if Song.query.filter_by(title=title).first():
        return "This song already exists in the database."
    else:
        l_songs = getArtistSongs(artist)

        for d in l_songs:
            if d['trackName'] == title:
                artist = get_or_create_artist( artist )
                genre = get_or_create_genre( d['primaryGenreName'] )
                artworkUrl = d['artworkUrl100']
                previewUrl = d['previewUrl']

                song = Song(title=title, artworkUrl=artworkUrl, previewUrl=previewUrl, artist_name=artist.name, genre_name=genre.name)
                session.add(song)
                session.commit()

                return render_template('add_song.html', artworkUrl=song.artworkUrl, previewUrl=song.previewUrl, title=song.title, artist=artist.name, genre=genre.name)

        return "Song not found. Please check spelling and punctuation of song or enter another song."

@app.route('/songs/artist/<artist>')
def see_artist(artist):
    mySongs = Song.query.filter_by(artist_name=artist).all()
    return render_template('artists.html', mySongs=mySongs, artist=artist)

@app.route('/songs/genre/<genre>')
def see_genre(genre):
    mySongs = Song.query.filter_by(genre_name=genre).all()
    return render_template('genres.html', mySongs=mySongs, genre=genre)


if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
