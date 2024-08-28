import os
from markupsafe import escape
import functools

from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

import flaskr.db as db

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

    @app.route('/', methods=['POST', 'GET'])
    def index():
        database = db.get_db()
        keys = ('early_toxicity', 'ray_therapy', 'ray_therapy_comp', 'sex', 'event', 'main_request', 'deauville_score', 'anat_request', 'groups', 'protocol', 'stage', 'histologic', 'b_symptoms', 'region', 'e_impact',
                'bm_damage_myelogram', 'bm_damage_kt', 'request_pat', 'start_therapy_date', 'end_therapy_date', 'event_date', 'last_date', 'birth_date', 'leykocytes', 'hemoglobin', 'trombocytes', 'ldh', 'ebv', 'esr', 'init_val', 'tumor_val')
        data = ()
        str_insert = ()
        for key in keys:
            get_data = request.form.get(key)
            if get_data is None:
                get_data = 'null'
            data += (str(get_data),)
            str_insert += ('?', )
        if request.method == 'POST':
            str_val = ', '
            keys = str("(" + str_val.join(keys) + ")")
            str_insert = str("(" + str_val.join(str_insert) + ")")
            print(keys)
            print(data)
            database.execute(
                "INSERT INTO person " + keys + " VALUES" + str_insert, data)
            database.commit()
            return f"{data}"
        return render_template('form.html')

    @app.route('/test')
    def test():
        database = db.get_db()
        users: list[tuple] = database.execute(
            "SELECT * FROM person").fetchall()
        print(users)
        for row in users:
            print(f"User ID: {row[0]}")
        if users is None:
            return "None"
        else:
            return f"{users[0][1]}!"

    def valid_login(username, password):
        if username == password:
            return True
        else:
            return False

    def log_the_user_in(username):
        redirect('/user/<' + username + '>')

    @ app.route('/login', methods=['POST', 'GET'])
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

    @ app.route('/user/<username>')
    def profile(username):
        return f'{username}\'s profile'

    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='John Doe'))

    db.init_app(app)
    return app
