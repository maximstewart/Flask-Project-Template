from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///static/db/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TITLE'] = ':::APP TITLE:::'


from core.models import db
db.init_app(app)

from core import routes
