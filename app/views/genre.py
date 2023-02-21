from flask_restx import Namespace, Resource

from app.dao.model.genre import GenreSchema
from app.container import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreViews(Resource):
    def get(self):
        genre = genre_service.get_all()
        return genres_schema.dump(genre)

@genre_ns.route('/<int:gid>')
class GenresViews(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre)