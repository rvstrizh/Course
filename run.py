from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.movie import movie_ns
from app.views.director import director_ns
from app.views.genre import genre_ns



def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def register_extensions(app):
    db.init_app(app) # init_app работает именно с этим приложением
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    # api.add_namespace(user_ns)
    # api.add_namespace(auth_ns)


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)  # конфигурация приложения
    app.run(host="localhost", port=10001, debug=True)