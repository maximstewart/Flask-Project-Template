# Python imports
from flask import Flask, request, render_template

# Application imports
from utils import DBConnect, MessageHandler


app        = Flask(__name__)
msgHandler = MessageHandler()
db         = DBConnect()


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html',
                                title=':::APP TITLE:::')
    elif request.method == 'POST':
        return render_template('error.html',
                                title='Error!',
                                message='Must use GET request type...')
    else:
        msg = "Must use GET/POST request type..."
        return msgHandler.createMessageJSON("alert-danger", msg)
