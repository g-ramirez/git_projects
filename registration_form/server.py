from flask import Flask, render_template, session, redirect, request, flash
from datetime import datetime

app = Flask("__name__")
app.secret_key = "Some_Key"

@app.route("/", methods=['GET'])
def get_index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit_data():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    date = request.form['bday']
    if element_is_empty([first_name,last_name,password,confirm_password,date]):
        flash("One or more of the fields is empty!", "empty-element")
        return redirect('/')
    if not password == confirm_password:
        flash("Passwords do not match")
        return redirect('/')
    if not password_is_valid(password):
        flash("Password must have at least 1 uppercase letter and 1 numeric value")
        return redirect('/')
    if not date_is_valid(date):
        flash("Please enter a day that occurs in the past!")
        return redirect('/')
    return redirect('/success')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

def password_is_valid(password):
    #Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.
    hasNumber = False
    hasUpper = False
    print 'Method starting...'
    for ch in password:
        if ch.isdigit():
            hasNumber = True
        if ch.isupper():
            hasUpper = True
        if hasNumber and hasUpper:
            return True
    return False

def date_is_valid(date):
    #Add a birth-date field that must be validated as a valid date (and must be from the past).
    #convert unicode to list with form [year,month,day]
    date_array = [eval(x) for x in date.split('-')]
    date = datetime(year=date_array[0], month=date_array[1], day=date_array[2])
    if date < datetime.now():
        return True
    else:
        return False

def element_is_empty(form_data):
    for item in form_data:
        if item == "":
            return True
    return False

if __name__ == "__main__":
    app.run(debug=1)
