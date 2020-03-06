from flask import request, render_template

from core import app, db


@app.route('/login', methods=['GET', 'POST'])
def login():
    return "<h1>Login Page Stub...</h1>"
