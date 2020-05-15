import os
import asyncio
from logging import getLogger

import psycopg2
from aiopg.sa import create_engine
from alembic import command
from alembic.config import Config
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine as sa_create_engine

from ..models import Base, Test

LOG = getLogger(__name__)

DATABASE = {
    'drivername': 'postgres',
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'username': os.getenv('POSTGRES_USER', 'aiotemplate'),
    'password': os.getenv('POSTGRES_PASSWORD', 'aiotemplate'),
    'database': os.getenv('POSTGRES_DB', 'aiotemplate')
}

dsn = str(URL(**DATABASE))


async def populate():
    tbl = Test.__table__
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            await conn.execute(tbl.insert().values(field_1='field_1_value', field_2='field_2_value'))
            await conn.execute(tbl.insert().values(field_1='another_field_1_value',))
        count = await conn.scalar(tbl.count())
        LOG.info('populated table with {} items'.format(count))


def run():
    LOG.info('recreating database and populating with initial data')
    conn = psycopg2.connect(user=DATABASE['username'], password=DATABASE['password'],
                            host=DATABASE['host'], port=DATABASE['port'], dbname="postgres")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS {}'.format(DATABASE['database']))
    cur.execute('CREATE DATABASE {}'.format(DATABASE['database']))

    engine = sa_create_engine(dsn)
    Base.metadata.create_all(engine)
    engine.dispose()

    # then, load the Alembic configuration and generate the
    # version table, "stamping" it with the most recent rev:
    alembic_cfg = Config("alembic.ini")
    command.stamp(alembic_cfg, "head")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(populate())
