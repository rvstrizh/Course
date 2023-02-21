from flask_restx import Namespace, Resource
from flask import request

from app.dao.model.movie import MovieSchema
from app.container import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        movies = movie_service.get_all()
        return movies_schema.dump(movies)

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieViews(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie)