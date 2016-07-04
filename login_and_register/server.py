from flask import Flask, request, session, render_template, flash, redirect
from myslconnect import MySQLConnector
from flask.ext.bcrypt import Bcrypt
from validate_email import validate_email
from datetime import datetime

app = Flask(__name__)
app.secret_key = "some_secret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_and_register')


@app.route("/", methods=['GET'])
def show_index():
    return render_template("index.html")

@app.route("/login", methods=['post'])
def login():
    #ensure fields are not empty
    if not request.form['email'] or not request.form['password']:
        flash("One of the required fields is empty or missing")
        return redirect("/")
    if not user_exists(request.form['email']):
        flash("The specified user does not exist.  Please try again")
        return redirect("/")
    if not bcrypt.check_password_hash( get_user_password(request.form['email']), request.form['password']):
        flash("The entered password does not match the password in our records")
        return redirect("/")
    session['first_name'] = get_first_name(request.form['email'])
    session['user_id'] = get_user_id(request.form['email'])
    return render_template("success.html", first_name=session['first_name'], messages=get_all_messages(), user_id=session['user_id'])

@app.route("/wall", methods=['get'])
def show_wall():
    return render_template("success.html", first_name=session['first_name'], messages=get_all_messages(), user_id=session['user_id'])


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

@app.route("/register", methods=['POST'])
def register():
    if not request.form['email'] or not request.form['password'] or not request.form['first-name'] or not request.form['last-name']:
        flash("One of the required forms is empty or missing")
        return redirect("/")
    if not validate_email(request.form['email']):
        flash("You did not enter a valid email")
        return redirect("/")
    if user_exists(request.form['email']):
        flash("The specified user already exists.  Please try logging in instead.")
        return redirect("/")
    if not password_is_valid(request.form['password']):
        flash("Your password did not meet the requirements of at least 8 characters.  Please try again")
    if not names_are_valid(request.form['first-name'], request.form['last-name']):
        flash("One or more of the specified names are either not longer than 2 characters or contain a digit")
    create_user(request.form['email'], request.form['password'])
    return render_template("success.html", username=request.form['email'])

@app.route("/message", methods=['POST'])
def handle_message():
    write_message_to_db(request.form['user-id'], request.form['message'])
    return redirect("/wall")

@app.route("/comment/<message_id>", methods=['POST'])
def handle_comment(message_id):
    write_comment_to_db(message_id, request.form['user-id'], request.form['comment'])
    return redirect("/wall")

def user_exists(email):
    query = "select * from users where email = '{}';".format(email)
    if mysql.query_db(query):
        return True
    else:
        return False

def get_user_password(email):
    query = "select password from users where email = '{}'".format(email)
    results = mysql.query_db(query)
    return results[0]['password']

def password_is_valid(password):
    if len(password) >= 8:
        return True
    else:
        return False
def encrypt_password(password):
    return bcrypt.generate_password_hash(password)

def create_user(email, password):
    encrypted_password = encrypt_password(password)
    insert_query = "INSERT into users (email, password, created_at, updated_at) VALUES (:email, :password, NOW(), NOW());"
    insert_data = {"email" : email,
                    "password" : encrypted_password }
    mysql.query_db(insert_query, insert_data)

def names_are_valid(first_name, last_name):
    if not (len(first_name) >+2 or len(last_name) >=2):
        return False
    if any(char.isdigit() for char in first_name+last_name):
        return False
    return True

def get_first_name(email):
    query = "select first_name from users where email = '{}';".format(email)
    return mysql.query_db(query)[0]['first_name']

def get_all_messages():
    query = "select * from messages;"
    return mysql.query_db(query)

def get_message_comments(message_id):
    query = "select * from comments where message_id = {};".format(message_id)
    return mysql.query_db(query)

app.jinja_env.globals.update(get_message_comments=get_message_comments)

def get_user_id(email):
    query = "select id from users where email = '{}';".format(email)
    return mysql.query_db(query)[0]['id']

def write_message_to_db(user_id, message):
    query = "insert into messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW());"
    query_data = {"user_id" : user_id,
                  "message" : message }
    mysql.query_db(query, query_data)

def write_comment_to_db(message_id, user_id, comment):
    query = "insert into comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW());"
    query_data = {"message_id" : message_id,
                   "user_id" : user_id,
                   "comment" : comment}
    mysql.query_db(query, query_data)

def get_message_author(user_id):
    query = "select first_name from users where id = {};".format(user_id)
    return mysql.query_db(query)[0]['first_name']
app.jinja_env.globals.update(get_message_author=get_message_author)

def get_comment_author(user_id):
    query = "select first_name from users where id = {};".format(user_id)
    return mysql.query_db(query)[0]['first_name']

app.jinja_env.globals.update(get_comment_author=get_comment_author)

def get_readable_timestamp(timestamp):
    return timestamp.strftime("%B %d %Y")

app.jinja_env.globals.update(get_readable_timestamp=get_readable_timestamp)

if __name__ == "__main__":
    app.run(debug=True)
