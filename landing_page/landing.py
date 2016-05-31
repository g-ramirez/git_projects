from Flask import Flask, render_template

app = Flask('__name__')
@app.route('/', methods=['GET'])
def return_index():
    return render_template(index.html)

@app.route('/ninjas'), methods=['GET'])
def return_ninjas():
    return render_template(ninjas.html)

@app.route('dojo/new', methods=['GET'])
def return_dojo():
    return render_template(dojo.html)        
