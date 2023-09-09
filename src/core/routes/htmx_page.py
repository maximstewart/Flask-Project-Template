# Python imports

# Lib imports
from flask import request
from flask import render_template
from flask_login import current_user

# Application imports
            # Get from __init__
from core import app
from core import oidc
from core import db


@app.route('/htmx-page', methods=['GET', 'POST'])
def htmx_page():
    if request.method == 'GET':
        return render_template('pages/htmx-page.html')

    return render_template('error.html', title = 'Error!',
                            message = 'Must use GET request type...')



@app.route('/load-hello-world', methods=['GET', 'POST'])
def load_hello_world():
    if request.method == 'GET':
        return "<h1>Hello, World!</h1>"

    return 'Must use GET request type...'
