from pkg.etl.extract.extract import extract_songs
from pkg.etl.transform.transform_df_songs import check_songs_df, transform_df
from pkg.common.database import upsert_df_into_db

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"


def load_songs_spotify(app):
    songs_df = extract_songs(app=app)
    print(songs_df)
    if check_songs_df(df=songs_df) is False:
        raise Exception('data response songs invalid')

    songs_df_transformed = transform_df(load_df=songs_df)
    print('songs_df_transformed, ', songs_df_transformed)
    exit(1)
    upsert_songs_df(app=app, df=songs_df_transformed)
    print('process done')


def upsert_songs_df(app, df):
    songs_collections = app.mongodbs['spotfify_app']['songs']
    filter_cl = ['timestamp', 'artist_name']
    upsert_df_into_db(collection=songs_collections, report_detail=df, filter_cl=filter_cl)
