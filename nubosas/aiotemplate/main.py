from logging import getLogger

from aiohttp import web
from aiopg.sa import create_engine

from .models import dsn
from .routes import setup_routes
from .settings import config

LOG = getLogger(__name__)


async def init_db(app):
    app['engine'] = await create_engine(dsn)


async def close_db(app):
    LOG.debug('closing engine')
    engine = app['engine']
    engine.close()
    await engine.wait_closed()


def app():
    _app = web.Application()
    _app['config'] = config
    setup_routes(_app)
    _app.on_startup.append(init_db)
    _app.on_cleanup.append(close_db)
    return _app


def run():
    the_app = app()
    web.run_app(the_app)
