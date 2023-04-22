from pkg.etl.load.load_songs_spotify import load_songs_spotify


def download_recent_songs(app):
    load_songs_spotify(app=app)
