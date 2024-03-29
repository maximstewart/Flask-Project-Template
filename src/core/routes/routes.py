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


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('pages/index.html')

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')

# NOTE: Normaly should sanitize logs or remove PII, etc.
@app.route('/log-client-exception', methods=['GET', 'POST'])
def ui_failure_exception_tracker():
    if request.method == 'POST':
        DATA = str(request.values['exception_data']).strip()
        logger.debug(DATA)
        return json_message.create("success", "UI Exception logged...")

    return json_message.create("danger", "Must use POST request type...")


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return render_template('pages/about.html')

    return render_template('error.html', title = 'Error!',
                            message = 'Must use GET request type...')


@app.route('/protected-zone', methods=['GET', 'POST'])
def protected_zone():
    if request.method == 'GET':
        msg = "Log in to see the secret!"
        if current_user.is_authenticated or oidc.user_loggedin:
            msg = "There is no secret! It was all a lie!"

        return render_template('pages/protected.html', secret = msg)

    return render_template('error.html', title = 'Error!',
                            message = 'Must use GET request type...')
