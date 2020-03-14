# Python imports

# Lib imports
from flask import request, render_template

# App imports
from core import app, db, RegisterForm
from core.MessageHandler import MessageHandler   # Get simple message processor


msgHandler = MessageHandler()
TITLE      = app.config['TITLE']

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        _form = RegisterForm()
        return render_template('register.html',
                                title=TITLE,
                                form=_form)

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')
