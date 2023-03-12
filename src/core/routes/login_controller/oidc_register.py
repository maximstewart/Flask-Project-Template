# Python imports

# Lib imports
from flask import flash
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

# Application imports
            # Get from __init__
from ... import app
from ... import oidc
from ... import db

from ...utils import MessageHandler   # Get simple message processor



msgHandler = MessageHandler()


@app.route('/oidc-register', methods=['GET', 'POST'])
def oidc_register():
    if oidc.user_loggedin or app.config["REGISTER_DISABLED"]:
        return redirect("/home")

    _form = RegisterForm()
    if _form.validate_on_submit():
        # TODO: Create...
        # NOTE: Do a requests api here maybe??
        flash("Account created successfully!", "success")
        return redirect("/login")

    return render_template('pages/register.html', form  = _form)
