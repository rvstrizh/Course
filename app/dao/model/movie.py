from app.database import db
from marshmallow import Schema, fields
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(245))
    description = Column(String(250))
    trailer = Column(String(250))
    year = Column(Integer())
    rating = Column(Integer())
    genre_id = Column(Integer)
    # genre = relationship("Genre")
    director_id = Column(Integer)
    # director = relationship("Director")

    def __repr__(self):
        return self.title


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()