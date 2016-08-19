from init import db, app


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255))
    key = db.Column(db.String(12))


db.create_all(app=app)
