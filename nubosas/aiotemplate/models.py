import os

from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE = {
    'drivername': 'postgres',
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'username': os.getenv('POSTGRES_USER', 'aiotemplate'),
    'password': os.getenv('POSTGRES_PASSWORD', 'aiotemplate'),
    'database': os.getenv('POSTGRES_DB', 'aiotemplate')
}

dsn = str(URL(**DATABASE))


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    field_1 = Column(String, nullable=False)
    field_2 = Column(String)

    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.root_cause)
