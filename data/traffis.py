import sqlalchemy
from .db_session import *


class Tariffs(SqlAlchemyBase):
    __tablename__ = "tariffs"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True, nullable=True)
    tariff = sqlalchemy.Column(sqlalchemy.TEXT, unique=True, nullable=True)
    social = sqlalchemy.Column(sqlalchemy.BOOLEAN, nullable=True)
    messanger = sqlalchemy.Column(sqlalchemy.BOOLEAN, nullable=True)
    gigabyte = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    minutes = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sms = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    youtube = sqlalchemy.Column(sqlalchemy.BOOLEAN, nullable=True)

