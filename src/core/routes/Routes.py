# Python imports

# Lib imports
from flask import request, render_template

# App imports
from core import app, db                         # Get from __init__
from core.models import Table                    # Get db models
from core.MessageHandler import MessageHandler   # Get simple message processor


msgHandler = MessageHandler()
TITLE      = app.config['TITLE']


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html',
                                title=TITLE)

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')
