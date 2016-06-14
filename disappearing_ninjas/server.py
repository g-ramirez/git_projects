from flask import Flask, redirect, render_template

app = Flask("__name__")

@app.route("/", methods=['GET'])
def show_index():
    return render_template("index.html")

@app.route("/ninja", methods=['GET'])
def show_ninjas():
    return render_template("ninjas.html")

@app.route("/ninja/<path>", methods=['GET'])
def show_based_on_path(path):
    print path
    print "This was reached"
    if path.lower() == 'blue':
        return render_template("ninja.html", filename="leonardo.jpg")
    elif path.lower() == 'red':
        return render_template("ninja.html", filename="raphael.jpg")
    elif path.lower() == 'orange':
        return render_template("ninja.html", filename="michelangelo.jpg")
    elif path.lower() == 'purple':
        return render_template("ninja.html", filename="donatello.jpg")
    else:
        return render_template("ninja.html", filename="notapril.jpg")

if __name__ == "__main__":
    app.run(debug=True)
