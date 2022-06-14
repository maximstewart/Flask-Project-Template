# Python imports

# Lib imports
from flask import request, render_template, url_for, redirect, flash

# App imports
from ... import app, oidc, db   # Get from __init__
from ...utils import MessageHandler   # Get simple message processor


msgHandler = MessageHandler()


@app.route('/oidc-register', methods=['GET', 'POST'])
def oidc_register():
    if oidc.user_loggedin:
        return redirect("/home")

    _form = RegisterForm()
    if _form.validate_on_submit():
        # TODO: Create...
        # NOTE: Do a requests api here maybe??
        flash("Account created successfully!", "success")
        return redirect("/login")

    return render_template('pages/register.html', form  = _form)
