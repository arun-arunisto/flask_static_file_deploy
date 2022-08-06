from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "arunisto"

@app.route("/")
def index():
    flash("what's your name?")
    return render_template("index.html")
@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + ",great to see you!")
    #below line indicates we are fetching data from user
    #request.form["name_input"]
    #name_input that we give name to the input in html
    return render_template("index.html")
