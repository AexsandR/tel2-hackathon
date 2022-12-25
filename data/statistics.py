import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

class Statistics(SqlAlchemyBase):
    __tablename__ = "statistics"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True, nullable=True)
    id_users = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"),)
    social = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    messanger = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    gigabyte = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    minutes = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sms = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    internet = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    buying_gigs = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sale_of_gigs = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    id_tariff = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("tariffs.id"),)
