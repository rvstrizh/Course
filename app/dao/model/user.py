from app.database import db
from marshmallow import Schema, fields
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String())
    password = Column(String())
    name = Column(String())
    surname = Column(String())
    favorite_genre = Column(String(), ForeignKey("genre.name"))
    genre = relationship("Genre")


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
