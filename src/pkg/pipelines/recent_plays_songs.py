from pkg.etl.load.load_songs_spotify import load_songs_spotify
from pkg.etl.extract.extract import extract_songs
from pkg.etl.transform.transform_df_songs import check_songs_df, transform_df


def download_recent_songs(app):
    load_songs_spotify(app=app)


def get_df_recent_song(app):
    songs_df = extract_songs(app=app)
    print(songs_df)
    if check_songs_df(df=songs_df) is False:
        raise Exception('data response songs invalid')

    songs_df_transformed = transform_df(load_df=songs_df)
    return songs_df_transformed
