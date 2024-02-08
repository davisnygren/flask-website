# Contains the routes to authentication-related pages

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import app, db
from app.models import User
from app.auth.forms import LoginForm
from urllib.parse import urlsplit

# Display the login page. Display the index if the user is already logged in.
# Log in the user and redirect if the form is submitted.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        
        # prevent redirects outside of application
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)