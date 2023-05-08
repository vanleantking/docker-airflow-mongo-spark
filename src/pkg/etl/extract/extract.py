
def extract_songs(app):
    """
    extract_songs: returm dataframe on request spotify api
    :param app:
    :return:
    """
    df = None
    try:
        df = app.api.get_recents_song()
    except Exception as exp:
        msg = f'Error occurs in extract song api interact {exp}'
        raise Exception(msg)
    return df
