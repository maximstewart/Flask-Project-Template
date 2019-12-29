from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///static/db/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .models import db
db.init_app(app)

from . import routes
