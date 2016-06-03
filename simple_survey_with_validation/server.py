from flask import Flask,render_template, request, flash, session, redirect
app = Flask("__name__")
app.secret_key = "topsecret"

@app.route("/", methods=["GET"])
def return_index():
    return render_template('index.html')

@app.route("/results", methods=["POST"])
def return_results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(name) < 1:
        flash("name")
        if len(comment) > 250:
            flash("comment")
        return redirect("/")
    if len(comment) > 250:
        flash("comment")
        return redirect("/")
    return render_template('results.html', name=name, location=location, language=language, comment=comment)

if __name__ == "__main__":
    app.run(debug=1)
