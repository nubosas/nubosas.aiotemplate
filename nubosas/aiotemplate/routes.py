from .views import health_check, list_view


def setup_routes(app):
    app.router.add_get('/health_check/', health_check)
    app.router.add_get('/', list_view)
