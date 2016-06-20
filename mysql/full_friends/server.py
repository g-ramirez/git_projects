from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "some_secret"
mysql = MySQLConnector(app, 'full_friends')

@app.route('/', methods=['GET'])
def show_index():
    return render_template('index.html', friends=get_friends())

@app.route('/friends', methods=['POST'])
def create():
    #If either form is empty, flash message and go back to index
    if not (request.form['first-name'] and request.form['last-name']):
        print 'if loop was reached'
        flash("One of the names is empty.  Please ensure all fields are non-empty")
        return redirect('/')
    insert_friend(request.form['first-name'], request.form['last-name'])
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    return render_template('edit.html', friend=get_friend(id)[0])

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    #If either form is empty, flash message and go back to index
    if not (request.form['first-name'] and request.form['last-name']):
        flash("One of the names is empty.  Please ensure all fields are non-empty")
        return redirect('/friends/{}/edit'.format(id))
    update_friend(id, request.form['first-name'], request.form['last-name'])
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    delete_friend(id)
    return redirect('/')

def get_friends():
    query = "SELECT * from friends;"
    return mysql.query_db(query)

def get_friend(id):
    query = "SELECT * from friends where id = {};".format(id)
    return mysql.query_db(query)

def delete_friend(id):
    query = "DELETE from friends where id = {};".format(id)
    mysql.query_db(query)

def update_friend(id, first_name, last_name):
    query = "UPDATE friends set first_name = '{}', last_name = '{}', updated_at = {} where id = {};".format(first_name, last_name, "NOW()", id)
    mysql.query_db(query)

def insert_friend(first_name, last_name):
    query = "INSERT into friends (first_name, last_name, created_at, updated_at) VALUES (:first_name, :last_name, NOW(), NOW());"
    data = {"first_name" : first_name,
            "last_name" : last_name
            }
    mysql.query_db(query,data)

if __name__ == "__main__":
    app.run(debug=1)
