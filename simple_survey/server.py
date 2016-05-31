from flask import Flask,render_template, request

app = Flask("__name__")

@app.route("/", methods=["GET"])
def return_index():
    return render_template('index.html')

@app.route("/results", methods=["POST"])
def return_results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('results.html', name=name, location=location, language=language, comment=comment)

if __name__ == "__main__":
    app.run(debug=1)
