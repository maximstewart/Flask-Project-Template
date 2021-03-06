# Python imports

# Lib imports
from flask import request, render_template
from flask_login import current_user


# App imports
from core import app, logger, oidc, db  # Get from __init__
from core.utils import MessageHandler   # Get simple message processor


msgHandler = MessageHandler()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('pages/index.html')

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')


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
