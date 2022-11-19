"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    songs = db.relationship('Song',
                            secondary = 'playlists_songs', 
                            backref='playlists')

    def __repr__(self):
        p = self
        return f"<Playlist {p.id} {p.name} {p.description}>"

    
class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    artist = db.Column(db.Text, nullable=False)

    def __repr__(self):
        s= self
        return f"<Song {s.id} {s.title} {s.artist}>"


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    playlist_id = db.Column(db.Integer,
                       db.ForeignKey("playlists.id"))
    song_id = db.Column(db.Integer,
                          db.ForeignKey("songs.id"))
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
