import os
from markupsafe import escape
import functools
from sqlalchemy.orm import Session
from sqlalchemy import select
from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import init_app, engine, User, Base, Sex

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    sex = SelectField('Sex', choices={(1, 'Male'), (2, 'Female')})


bp = Blueprint('auth', __name__, url_prefix='/auth')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/submit', methods=['GET', 'POST'])
    def submit():
        form = MyForm()
        if form.validate_on_submit():
            with Session(engine) as session:
                person = User(name=form.name.data, sex=form.sex.data)
                session.add(person)
                session.commit()
            return redirect('/select')
        return render_template('submit.html', form=form)

    @app.route('/select')
    def select_name():
        session = Session(engine)
        stmt = select(User).join(Sex.sex)
        return render_template('success.html', persons=session.scalars(stmt))

    def valid_login(username, password):
        if username == password:
            return True
        else:
            return False

    def log_the_user_in(username):
        redirect('/user/<' + username + '>')

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None
        if request.method == 'POST':
            if valid_login(request.form['username'],
                           request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'
        return '''
            <form method="post" action="/login">
                <p><input type=text name=username>
                <p><input type=text name=password>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/user/<username>')
    def profile(username):
        return f'{username}\'s profile'

    with app.test_request_context():
        # print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='John Doe'))

    init_app(app)
    Base.metadata.create_all(engine)
    return app
