from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "SomeSecret"

@app.route("/", methods=['GET'])
def play():
    create_random()
    if get_state() == 'initial':
        return render_template('play.html')
    elif get_state() == 'lose':
        return render_template('lose.html', lose_val = session['lose_val'])
    else:
        return render_template('win.html', number=session['guess'])

@app.route("/submit", methods=['post'])
def submit():
    try:
        session['guess'] = int(request.form['guess'])
        #for debugging
        #print "Guess is: " + request.form['guess']
        if session['guess'] > session['random']:
            session['state'] = 'lose'
            session['lose_val'] = 'high'
        elif session['guess'] < session['random']:
            session['state'] = 'lose'
            session['lose_val'] = 'low'
        else:
            session['state'] = 'win'
    except:
        pass
    return redirect('/')

@app.route("/playagain", methods=['POST'])
def play_again():
    session.pop('random')
    session.pop('state')
    return redirect('/')

def create_random():
    try:
        session['random']
        #for debugging
        #print 'Winning number is: {}'.format(session['random'])

    except:
        session['random'] = random.randrange(0, 101) #rand from 0-100
        #for debugging
        #print 'Winning number is: {}'.format(session['random'])
def get_state():
    try:
        session['state']
    except:
        session['state'] = 'initial'
    return session['state']
if __name__ == '__main__':
    app.run(debug=True)
