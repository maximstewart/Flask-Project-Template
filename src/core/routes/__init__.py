"""
    Routes module
"""
from .login_controller import flask_login
from .login_controller import flask_register
from .login_controller import oidc_login
from .login_controller import oidc_register
from .login_controller import controller

from . import routes
from . import htmx_page
