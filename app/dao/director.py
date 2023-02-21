from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        director = self.session.query(Director)
        return director.all()

    def get_one(self, did):
        director = self.session.query(Director)
        return director.get(did)