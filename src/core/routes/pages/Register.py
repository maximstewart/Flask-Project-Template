# Python imports

# Lib imports
from flask import request, render_template, url_for, redirect, flash

# App imports
from core import app, db, RegisterForm
from core.MessageHandler import MessageHandler   # Get simple message processor


msgHandler = MessageHandler()
TITLE      = app.config['TITLE']

@app.route('/register', methods=['GET', 'POST'])
def register():
    _form = RegisterForm()

    if _form.validate_on_submit():
        flash("Account created successfully!", "success")
        return redirect(url_for("home"))

    return render_template('register.html',
                            title=TITLE,
                            form=_form)
