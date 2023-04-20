from mysql.connector import pooling


def connect_mysql(dct):
    """
    connect mysql database adserver
    Args:
        dct:

    Returns:

    """
    return pooling.MySQLConnectionPool(
        pool_name="python-instance-pooling",
        pool_size=3,
        host=dct["AdServerMySQLHost"],
        user=dct["AdServerMySQLUserName"],
        database=dct["AdServerMySQLDatabase"],
        passwd=dct["AdServerMySQLPassword"],
        port=dct["AdServerMySQLPort"])


def connect_mysqls(env):
    """
    connect into all mysql env exist from environment settings
    Args:
        env:

    Returns:

    """
    mysql_env = initialize_connect_env(env=env)
    dbs = {}
    for key, env in mysql_env.items():
        dbs[key] = connect_mysql(env)
    return dbs


def initialize_connect_env(env):
    """
    default setting mysql env [prod, dev]
    Args:
        env:

    Returns:

    """
    mysql_env = {
        'development': {
            'AdServerMySQLHost': env['DevAdServerMySQLHost'] if 'DevAdServerMySQLHost' in env else env[
                'AdServerMySQLHost'],
            'AdServerMySQLUserName': env['DevAdServerMySQLUserName'] if 'DevAdServerMySQLUserName' in env else env[
                'AdServerMySQLUserName'],
            'AdServerMySQLDatabase': env['DevAdServerMySQLDatabase'] if 'DevAdServerMySQLDatabase' in env else env[
                'AdServerMySQLDatabase'],
            'AdServerMySQLPassword': env['DevAdServerMySQLPassword'] if 'DevAdServerMySQLPassword' in env else env[
                'AdServerMySQLPassword'],
            'AdServerMySQLPort': env['DevAdServerMySQLPort'] if 'DevAdServerMySQLPort' in env else env[
                'AdServerMySQLPort'],
        }
    }
    prod_host = env['ProdAdServerMySQLHost'] if 'ProdAdServerMySQLHost' in env else ''
    prod_user_name = env['ProdAdServerMySQLUserName'] if 'ProdAdServerMySQLUserName' in env else ''
    prod_database = env['ProdAdServerMySQLDatabase'] if 'ProdAdServerMySQLDatabase' in env else ''
    prod_password = env['ProdAdServerMySQLPassword'] if 'ProdAdServerMySQLPassword' in env else ''
    prod_port = env['ProdAdServerMySQLPort'] if 'ProdAdServerMySQLPort' in env else 3306

    # if already exist prod env
    if prod_host + prod_user_name + prod_password != "":
        mysql_env['production'] = {
            'AdServerMySQLHost': prod_host,
            'AdServerMySQLUserName': prod_user_name,
            'AdServerMySQLDatabase': prod_database,
            'AdServerMySQLPassword': prod_password,
            'AdServerMySQLPort': prod_port,
        }
    return mysql_env
