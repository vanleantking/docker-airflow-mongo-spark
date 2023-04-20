from pkg.common.rp_logger import set_up_logger
from pkg.common import appcontext
from pkg.common.connect import connect_mongodb
from pkg.common.constants import CHANNEL_FB
from pkg.spotify.api.spotify_api import SpotifyAPI


def initialize_app_context(args, env):
    # setup logger for fb application
    lg = set_up_logger(
        name=args.application_name,
        path=args.application_logger)

    db = connect_mongodb(env)

    spotify = SpotifyAPI(args=args)

    # create app instance for run app
    spotify_app = appcontext.AppContext(
        mysqldbs=None,
        logger=lg,
        api=spotify,
        args=args,
        mongodbs=db,
        platform=CHANNEL_FB)

    return spotify_app
