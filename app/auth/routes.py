from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.auth import bp
from app.models import User
from app import db
from app.auth.forms import RegisterForm, LoginForm

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(form.password.data):
        login_user(user)
        return redirect(url_for('main.index'))
    flash('Invalid credentials')
    return render_template('auth/login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
