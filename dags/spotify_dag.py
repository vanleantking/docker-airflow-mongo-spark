from pkg.initialize_app_context import initialize_app_context
from load_env import load_env
from pkg.pipelines.recent_plays_songs import get_df_recent_song

import datetime as dt
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine

from airflow.utils.dates import days_ago


def start_spotify_etl():
    app = initialize_app_context()