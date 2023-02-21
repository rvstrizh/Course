from app.dao.model.movie import Movie
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from create_table import db

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///project.db")

session = Session()


def table(data):
    for movie in data['movies']:
        m = Movie(
            id=movie['pk'],
            title=movie['title'],
            description=movie['description'],
            trailer=movie['trailer'],
            year=movie['year'],
            rating=movie['rating'],
            genre_id=movie['genre_id'],
            director_id=movie['director_id'],
        )
        db.add(m)
        db.commit()

    for director in data['directors']:
        d = Director(
            id=director['pk'],
            name=director['name']
        )
        db.add(d)
        db.commit()

    for genre in data['genres']:
        g = Genre(
            id=genre['pk'],
            name=genre['name']
        )
        db.add(g)
        db.commit()