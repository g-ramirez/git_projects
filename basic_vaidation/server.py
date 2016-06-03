from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = "TopSecret"

@app.route("/", methods=["GET"])
def return_index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  if len(request.form['name']) < 1:
    flash("Name cannot be empty!")
  else:
    flash("Success! Your name is {}".format(request.form['name']))
  return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
