import os

config = {
    'database': {
        'drivername': 'postgres',
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '5432'),
        'username': os.getenv('POSTGRES_USER', 'aiotemplate'),
        'password': os.getenv('POSTGRES_PASSWORD', 'aiotemplate'),
        'database': os.getenv('POSTGRES_DB', 'aiotemplate')
    },
    'datetime_format': '%Y-%m-%dT%H:%M%SZ',
}
