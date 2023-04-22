import datetime


class SpotifyAccessToken(object):
    access_token = "access_token"
    token_type = "token_type"
    expires_in = "expires_in"
    expires_at = "expires_at"

    def __init__(self, access_token, token_type, expire):
        print('access_token, token_type, expire, ', access_token, token_type, expire)
        self.access_token = access_token
        self.tk = token_type,
        print('after assign, ', self.tk, token_type)
        self.expires_in = expire
        self.expires_at = datetime.datetime.today() + datetime.timedelta(seconds=self.expires_in)

