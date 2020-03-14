from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Table(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)

    def __repr__(self):
        return f"['{self.title}', '{self.icon}', '{self.link}', '{self.id}']"


class User(db.Model):
    username = db.Column(db.String, nullable=False)
    email    = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    id       = db.Column(db.Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)

    def __repr__(self):
        return f"['{self.username}', '{self.email}', '{self.password}', '{self.id}']"
