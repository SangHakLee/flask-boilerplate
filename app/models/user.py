from . import db

class User(db.model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)