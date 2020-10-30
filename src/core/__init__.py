# Python imports
import os, secrets
from datetime import timedelta


# Lib imports
from flask import Flask
    #OIDC Login path
from flask_oidc import OpenIDConnect
    # Flask Login Path
from flask_bcrypt import Bcrypt
from flask_login import current_user, login_user, logout_user, LoginManager


# Apoplication imports



# Configs and 'init'
ROOT_FILE_PTH = os.path.dirname(os.path.realpath(__file__))
# This path is submitted as the redirect URI in certain code flows.
# Change localhost%3A6969 to different port accordingly or change to your domain.
REDIRECT_LINK = "http%3A%2F%2Flocalhost%3A6969%2F"

app = Flask(__name__)
app.config.update({
                "TITLE": ':::APP TITLE:::',
                'DEBUG': False,
                'LOGIN_PATH': "FLASK_LOGIN",  # Value can be OIDC or FLASK_LOGIN
                'SECRET_KEY': secrets.token_hex(32), # For csrf and some other stuff...
                'PERMANENT_SESSION_LIFETIME': timedelta(days = 7).total_seconds(),
                'SQLALCHEMY_DATABASE_URI': "sqlite:///static/db/database.db",
                'SQLALCHEMY_TRACK_MODIFICATIONS': False,
                'APP_REDIRECT_URI': REDIRECT_LINK,
                'OIDC_CLIENT_SECRETS': ROOT_FILE_PTH + '/client_secrets.json',
                'OIDC_ID_TOKEN_COOKIE_SECURE': True, # Only set false in development setups...
                'OIDC_REQUIRE_VERIFIED_EMAIL': False,
                'OIDC_USER_INFO_ENABLED': True,
                'OIDC_VALID_ISSUERS': [
                                        'http://localhost:8080/auth/realms/apps',
                                        'https://localhost:443/auth/realms/apps'
                                        ],
                'OIDC_TOKEN_TYPE_HINT': 'access_token'
                })

oidc          = OpenIDConnect(app)
login_manager = LoginManager(app)
bcrypt        = Bcrypt(app)


from core.models import db, User
with app.app_context():
    db.create_all()


from core.forms import RegisterForm, LoginForm
from core import routes
