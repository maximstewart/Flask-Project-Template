# Python imports

# Lib imports
from flask import request, render_template

# App imports
from core import app, db
from core.MessageHandler import MessageHandler   # Get simple message processor


msgHandler = MessageHandler()
TITLE      = app.config['TITLE']

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',
                                title=TITLE)

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')
