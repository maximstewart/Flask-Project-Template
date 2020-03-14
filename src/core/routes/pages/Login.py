# Python imports

# Lib imports
from flask import request, render_template

# App imports
from core import app, db, LoginForm
from core.MessageHandler import MessageHandler   # Get simple message processor


msgHandler = MessageHandler()
TITLE      = app.config['TITLE']

@app.route('/login', methods=['GET', 'POST'])
def login():
    _form = LoginForm()

    return render_template('login.html',
                            title=TITLE,
                            form=_form)
