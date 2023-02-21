from flask_restx import Namespace, Resource

from app.dao.model.director import DirectorSchema
from app.container import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors)

@director_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director)