import pandas as pd


def check_songs_df(df):
    if len(df) == 0:
        return False

    # Enforcing Primary keys since we don't need duplicates
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        # The Reason for using exception is to immediately terminate the program and avoid further processing
        raise Exception("Primary Key Exception,Data Might Contain duplicates")

    # Checking for Nulls in our data frame
    if df.isnull().values.any():
        raise Exception("Null values found")


def transform_df(load_df):
    # Applying transformation logic
    processed_df = load_df.groupby(['timestamp', 'artist_name'], as_index=False).count()
    processed_df.rename(columns={'played_at': 'count'}, inplace=True)

    # Creating a Primary Key based on Timestamp and artist name
    processed_df["ID"] = processed_df['timestamp'].astype(str) + "-" + processed_df["artist_name"]

    return processed_df[['ID', 'timestamp', 'artist_name', 'count']]
