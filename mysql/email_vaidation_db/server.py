from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from validate_email import validate_email

app = Flask(__name__)
app.secret_key = "some_secret"
mysql = MySQLConnector(app, 'email_db')

@app.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    if not email:
        flash("You didn't enter anything!")
        return redirect('/')
    if not validate_email(email):
        flash("You didn't enter a valid email! Try again")
        return redirect('/')
    insert_user(email)
    return redirect('/success')

@app.route("/success", methods=['GET'])
def show_emails():
    return render_template("success.html", emails=get_emails())

def insert_user(email):
    query = 'INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW());'
    data = { "email_address" : email}
    mysql.query_db(query,data)

def get_emails():
    query = "SELECT * FROM emails;"
    return mysql.query_db(query)

if __name__ == "__main__":
    app.run(debug=1)
