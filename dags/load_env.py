from airflow.models import Variable


def load_env():
    """
    load default variable setting from admin > variables airflow webserver
    :return:
    """
    params = {'SpotifySongHost': Variable.get('SpotifySongHost'), 'SpotifySongPort': Variable.get('SpotifySongPort'),
              'SpotifySongUserName': Variable.get('SpotifySongUserName'),
              'SpotifySongPassword': Variable.get('SpotifySongPassword'),
              'SpotifySongDatabase': Variable.get('SpotifySongDatabase'),
              'application_name': Variable.get('ApplicationName'),
              'application_logger': Variable.get('ApplicationLogger'), 'client_id': Variable.get('SpotifyClientID'),
              'client_secret': Variable.get('SpotifyClientSecret'),
              'account_api_base': Variable.get('SpotifyAccountBase'), 'api_base': Variable.get('SpotifyAPIBase'),
              'api_version': Variable.get('SpotifyVersion'),
              'top_secret_access_token': Variable.get('SpotifySecretAccessToken')}
    # RedirectURL

    return params
