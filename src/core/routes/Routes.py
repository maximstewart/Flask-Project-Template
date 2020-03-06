from flask import request, render_template
from core import app, db                         # Get from __init__

from core.models import Table                    # Get db models
from core.MessageHandler import MessageHandler   # Get simple message processor


# Python imports


msgHandler = MessageHandler()


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html',
                                title=':::APP TITLE:::')

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')
