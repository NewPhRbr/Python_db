from flask import Flask, url_for, request, render_template, redirect, g
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return f"Hello, {request.form['username']}!"
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''

def valid_login(username, password):
    if username == password:
        return True
    else: return False

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

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

@app.cli.add_command
def add_db(exception):
    db = g.pop('db', None)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))