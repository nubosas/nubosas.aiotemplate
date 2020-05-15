from aiohttp import web

from .models import Test
from .version import version


async def health_check(request):
    """Return version hash."""

    data = {"version": version}

    return web.json_response(data)


async def list_view(request):
    engine = request.app['engine']
    body = ''
    async with engine.acquire() as conn:
        async for row in conn.execute(Test.__table__.select()):
            body += '<p>{}: {} | {}</p>\n'.format(row.id, row.field_1, row.field_2)
    return web.Response(body=body.encode())
