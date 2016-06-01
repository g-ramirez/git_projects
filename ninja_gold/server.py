from flask import Flask, render_template, session, request, redirect
from datetime import datetime
from random import randint, choice
app = Flask(__name__)
app.secret_key = 'SomeSecret'

@app.route("/", methods=['GET'])
def play():
    init_count()
    init_actions()
    return render_template('index.html', count=session['count'], activities=session['actions'])

@app.route("/process_money", methods=['POST'])
def process_money():
    building = request.form['building']
    print "You should see the building print", building
    if building == 'farm':
        farm_add()
    elif building == 'cave':
        cave_add()
    elif building == 'house':
        house_add()
    else:
        casion_add()
    return redirect('/')

@app.route("/reset", methods=['POST'])
def reset():
    session.pop('count')
    session.pop('actions')
    return redirect('/')

def init_count():
    try:
        session['count']
    except:
        session['count'] = 0

def init_actions():
    try:
        session['actions']
    except:
        session['actions'] = []
    finally:
        print 'init actions completed successfully'

def get_date_time():
    now = datetime.now()
    return now.strftime('%Y/%m/%d %I:%M%p')

def farm_add():
    print 'this was reached'
    delta = randint(10,20)
    session['count'] += delta
    date = get_date_time()
    session['actions'].append("Earned {} golds from the farm! ({})".format(delta,date))
def cave_add():
    delta = randint(5,10)
    session['count'] += delta
    date = get_date_time()
    session['actions'].append("Earned {} golds from the cave! ({})".format(delta,date))
def house_add():
    delta = randint(2,5)
    session['count'] += delta
    date = get_date_time()
    session['actions'].append("Earned {} golds from the house! ({})".format(delta,date))
def casion_add():
    delta = randint(0,50) * choice([-1,1])
    verb = 'lost'
    exclamation = 'ouch'
    if delta >= 0:
        verb = 'won'
        exclamation = 'awesome'
    session['count'] += delta
    date = get_date_time()
    session['actions'].append("Earned a casino and {} {} golds...{}!.. ({})".format(verb, abs(delta), exclamation, date))

if __name__ == "__main__":
    app.run(debug=True)
