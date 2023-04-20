import requests as rq
from datetime import datetime
import datetime


class SpotifyAPI(object):
    def __init__(self, args=None):
        self._client_secret = args.client_secret
        self._client_id = args.client_id
        self._access_token = None
        self._account_base = args.account_api_base
        self._api_base = args.api_base
        self._api_version = args.api_version

    def get_access_token(self):
        request_url = f'{self._account_base}/api/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }
        resp = rq.post(url=request_url, params=data, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def get_recents_song(self, limit=50):
        input_variables = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {token}".format(token=self._access_token)
        }

        today = datetime.now()
        yesterday = today - datetime.timedelta(days=1)
        yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

        data = {
            'limit': limit,
            'after': yesterday_unix_timestamp
        }

        # Download all songs you've listened to "after yesterday", which means in the last 24 hours
        rq_url = f'{self._api_base}/{self._api_version}/me/player/recently-played'
        resp = rq.get(url=rq_url, headers=input_variables, params=data)
        resp.raise_for_status()
        return resp.json()
