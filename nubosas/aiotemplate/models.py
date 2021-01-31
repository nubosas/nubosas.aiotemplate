from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from .settings import config

Base = declarative_base()

dsn = str(URL(**config['database']))


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    field_1 = Column(String, nullable=False)
    field_2 = Column(String)

    __table_args__ = (
        UniqueConstraint('field_1', 'field_2'),
        Index('field_2__index', 'field_2')
    )

    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.root_cause)
