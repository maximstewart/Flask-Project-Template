from core import db


class Table(db.Model):
    # title = db.Column(db.String, nullable=False)
    # icon  = db.Column(db.String, nullable=False)
    # link  = db.Column(db.String, nullable=False)
    id    = db.Column(db.Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)

    def __repr__(self):
        return f"['{self.title}', '{self.icon}', '{self.link}', '{self.id}']"
