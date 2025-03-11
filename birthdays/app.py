import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session,url_for

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")
myDB=[]

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
def addBirthDay():
    name=request.form.get("name")
    month=request.form.get("month")
    day=request.form.get("day")
    return name,month,day
@app.route("/delete", methods=["GET", "POST"])
def delete():
    global myDB
    if request.method == "POST":
        record_id=request.form.get("id")
        db.execute("DELETE FROM birthdays WHERE id = ?", (record_id,))
        return redirect("/")
    else:
        return  render_template("index.html")



@app.route("/", methods=["GET", "POST"])
def index():
    global myDB
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name,month,day=addBirthDay()
        if not name:
            redirect("/")
        if not month:
            redirect("/")
        if not day:
            redirect("/")
        db.execute("INSERT INTO birthdays (name,month,day) VALUES(?,?,?)",name,month,day)
        return redirect("/")

    else:
    #  TODO: Display the entries in the database on index.html
        birthdays=db.execute("SELECT * FROM birthdays")
        return render_template("index.html",birthdays=birthdays)

if __name__ == '__main__':
    app.run(debug=True)
