from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genre = self.session.query(Genre)
        return genre.all()

    def get_one(self, gid):
        genre = self.session.query(Genre)
        return genre.get(gid)