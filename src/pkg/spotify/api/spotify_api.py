import requests as rq
# from datetime import datetime
import datetime
import base64
from pkg.spotify.models.spotify_access_token import SpotifyAccessToken


class SpotifyAPI(object):
    def __init__(self, args=None):
        self._client_secret = args.client_secret
        self._client_id = args.client_id
        self._access_token = None
        self._account_base = args.account_api_base
        self._api_base = args.api_base
        self._api_version = args.api_version
        # self._redirect_url = args.redirect_url

    def get_access_token(self):
        current_time = datetime.datetime.now()
        # check if not log in yet, or access_token has expired
        if self._access_token is None or current_time > self._access_token.expires_at:
            self.grant_access_token()
        # raise exception if access_token not valid yet
        if self._access_token is None:
            raise Exception("Authorization Error: An unexpected error occurs, please check log")
        return self.get_access_token_str()

    def get_access_token_str(self):
        print('zzzzzzzzzz, ', self._access_token[SpotifyAccessToken.token_type],
              self._access_token[SpotifyAccessToken.access_token])
        return f'{self._access_token[SpotifyAccessToken.token_type]} {self._access_token[SpotifyAccessToken.access_token]}'

    def grant_access_token(self):
        request_url = f'{self._account_base}/api/token'
        base64_encode = self.encode_base64()
        print('base64_encodezzzzzzzz, ', base64_encode)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic OGJkZjYzMzJlNTcwNGE2YzlkYmRlNmU4NjE4MjhiYzI6YTE2YmYzYmZiM2I2NGM0YWIxM2EzMzEzZmRmM2RjMDg='
        }
        data = {
            "grant_type": "client_credentials",
            'scopes': 'user-read-recently-played'
        }
        resp = rq.post(url=request_url, params=data, headers=headers)
        print(resp.json())
        resp.raise_for_status()
        data = resp.json()
        if SpotifyAccessToken.access_token in data:
            self._access_token = data
            return

    def encode_base64(self):
        base64_str = f'{self._client_id}:{self._client_secret}'
        str_byte = base64_str.encode('utf-8')
        print('base64_str, ', base64_str)
        return base64.b64encode(str_byte)

    def get_recents_song(self, limit=50, date_range=1):
        input_variables = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"{self.get_access_token()}"
        }
        print('input_variables, ', input_variables)

        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=date_range)
        yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

        data = {
            'limit': limit,
            'after': yesterday_unix_timestamp
        }

        # Download all songs you've listened to "after yesterday", which means in the last 24 hours
        rq_url = f'{self._api_base}{self._api_version}/me/player/recently-played'
        print('rq url recent songs, ', rq_url, data)
        resp = rq.get(url=rq_url, headers=input_variables, params=data)
        if resp.status_code != 200:
            print('detail response, ', resp.json())
        resp.raise_for_status()
        return resp.json()
