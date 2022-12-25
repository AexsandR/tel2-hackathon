import sqlalchemy
from .db_session import SqlAlchemyBase

class Users(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True, nullable=True)
    number = sqlalchemy.Column(sqlalchemy.Integer, unique=True, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
