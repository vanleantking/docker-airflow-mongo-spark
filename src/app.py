import argparse
import sys
from pkg.initialize_app_context import initialize_app_context
from pkg.common.utils import get_env_data_as_dict
from pkg.spotify.api import spotify_api
from pkg.pipelines.recent_plays_songs import download_recent_songs


def main(args=None, env=None):
    """
    - first run will download all report exist
    - then wait until next date to run download report yesterdate
    """
    print('args, ', args)

    fb_app = initialize_app_context(args=args, env=env)

    print('-----------run once at start app-----------, ', fb_app)
    download_recent_songs(app=fb_app)

    print('not support')


if __name__ == '__main__':
    # setup logger
    env = get_env_data_as_dict('./.env')
    arg_parser = argparse.ArgumentParser(sys.argv[0])
    arg_parser.add_argument(
        '--client_id',
        type=str,
        help='fb application name',
        default=env['SpotifyClientID'])

    arg_parser.add_argument(
        '--client_secret',
        type=str,
        help='fb application name',
        default=env['SpotifyClientSecret'])
    arg_parser.add_argument(
        '--account_api_base',
        type=str,
        help='graph fb base url',
        default=env['SpotifyAccountBase'])
    arg_parser.add_argument(
        '--api_base',
        type=str,
        help='graph fb version',
        default=env['SpotifyAPIBase'])
    arg_parser.add_argument(
        '--api_version',
        type=str,
        help='spotify version used',
        default=env['SpotifyVersion'])

    arg_parser.add_argument(
        '--application_name',
        type=str,
        help='app name',
        default=env['ApplicationName'])

    arg_parser.add_argument(
        '--application_logger',
        type=str,
        help='app logger',
        default=env['ApplicationLogger'])
    arg_parser.add_argument(
        '--top_secret_access_token',
        type=str,
        help='app logger',
        default=env['SpotifySecretAccessToken'])

    print(env)

    args = arg_parser.parse_args()

    main(args, env)
