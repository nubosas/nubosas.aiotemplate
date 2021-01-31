from aiohttp import web

from .models import Test
from .version import version


async def health_check(request):
    """Return version hash."""

    data = {"version": version}

    return web.json_response(data)


async def list_view(request):
    body = ''

    conn = await request.app['engine'].acquire()

    proxy = await conn.execute(Test.__table__.select())

    async for row in await proxy.fetchall():
        body += '<p>{}: {} | {}</p>\n'.format(row.id, row.field_1, row.field_2)
    return web.Response(body=body.encode())
