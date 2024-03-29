# Python imports

# Lib imports
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# Apoplication imports
from core import app
from core import login_manager



db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    username = db.Column(db.String, unique=True, nullable=False)
    email    = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    id       = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)

    def __repr__(self):
        return f"['{self.username}', '{self.email}', '{self.password}', '{self.id}']"


db.init_app(app)
with app.app_context():
    db.create_all()
