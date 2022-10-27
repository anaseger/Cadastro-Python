from flask import Flask, request, render_template, redirect, url_for
from db import add_text, get_data
app = Flask(__name__)

@app.route("/")
def index():
    all_text = get_data()
    return render_template('index.html', all_text = all_text)

@app.route("/inicio")
def inicio():
    return render_template("index2.html")
    
@app.route("/add_text", methods=["POST", "GET"])
def AddText():
    if request.method == "POST":
        name = request.form["textv"]
        idade = request.form["textu"]
        add_new = add_text(name, idade)
        return redirect(url_for('index'))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)