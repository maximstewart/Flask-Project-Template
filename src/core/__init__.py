from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///static/db/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TITLE'] = ':::APP TITLE:::'

# For csrf...change!!
app.config['SECRET_KEY'] = '48e80dcf4ed6ea952ca1b7b564be22d665e6e178f7fda84828fdd5e7cdca097a'

from core.models import db
db.init_app(app)


from core.forms import RegisterForm, LoginForm
from core import routes
