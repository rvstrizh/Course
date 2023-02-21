from app.dao.model.movie import Movie
from flask import request

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        movies = self.session.query(Movie)

        if director_id:
            movies = movies.filter(Movie.director_id == director_id)
        elif genre_id:
            movies = movies.filter(Movie.genre_id == genre_id)
        elif year:
            movies = movies.filter(Movie.year == year)

        return movies.all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def get_one(self, mid):
        movie = self.session.query(Movie)
        return movie.get(mid)