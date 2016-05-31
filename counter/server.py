from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'SomeSecret'

@app.route("/", methods=["GET"])
def return_index():
    increment_one()
    return render_template('index.html', count=session['count'])

@app.route("/reset", methods=['POST'])
def route_reset():
    reset_count()
    print 'this was reached'
    return redirect('/')

@app.route("/plus2", methods=['POST'])
def route_plus2():
    increment_one()
    return redirect('/')

def increment_one():
    try:
        session['count'] += 1
    except:
        session['count'] = 0

def reset_count():
    session['count'] = 0

if __name__ == '__main__':
    app.run(debug=True)
