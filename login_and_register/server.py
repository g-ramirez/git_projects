from flask import Flask, request, session, render_template, flash, redirect
from myslconnect import MySQLConnector
from flask.ext.bcrypt import Bcrypt
from validate_email import validate_email

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
    session['email'] = request.form['email']
    return render_template("success.html", username=session['email'])


@app.route('/logout', methods=['POST'])
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

if __name__ == "__main__":
    app.run(debug=True)
