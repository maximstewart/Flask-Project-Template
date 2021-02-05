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
from core.utils import Logger


# Configs and 'init'
APP_NAME      = ':::APP TITLE:::'
ROOT_FILE_PTH = os.path.dirname(os.path.realpath(__file__))
# This path is submitted as the redirect URI in certain code flows.
# Change localhost%3A6969 to different port accordingly or change to your domain.
REDIRECT_LINK = "http%3A%2F%2Flocalhost%3A6969%2F"

app = Flask(__name__)
app.config.update({
                "TITLE": APP_NAME,
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
logger        = Logger().get_logger()


def oidc_loggedin():
    return oidc.user_loggedin

def oidc_isAdmin():
    if oidc_loggedin():
        isAdmin = oidc.user_getfield("isAdmin")
        if isAdmin == "yes" :
            return True
    return False


app.jinja_env.globals['oidc_loggedin'] = oidc_loggedin
app.jinja_env.globals['oidc_isAdmin']  = oidc_isAdmin
app.jinja_env.globals['TITLE']         =  APP_NAME


from core.models import db, User
db.init_app(app)
with app.app_context():
    db.create_all()

from core.forms import RegisterForm, LoginForm
from core import routes
