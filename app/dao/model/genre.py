from app.database import db
from marshmallow import fields, Schema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer(), primary_key=True)
    name = Column(String())


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()