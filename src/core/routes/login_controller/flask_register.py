# Python imports

# Lib imports
from flask import flash
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

# Application imports
            # Get from __init__
from core import app
from core import bcrypt
from core import db
from core import current_user
from core import RegisterForm

from core.models import User
from core.utils import MessageHandler   # Get simple message processor



msgHandler = MessageHandler()


@app.route('/app-register', methods=['GET', 'POST'])
def app_register():
    if current_user.is_authenticated or app.config["REGISTER_DISABLED"]:
        return redirect(url_for("home"))

    _form = RegisterForm()
    if _form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(_form.password.data).decode("utf-8")
        user = User(username = _form.username.data, email = _form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for("login"))

    return render_template('pages/register.html',
                            form  = _form)
