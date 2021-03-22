# This file is part of: github.com/pablocorbalann/secgenda
"""
The views module (from the app package), contains all the
viws and pages of the application, you can learn more about the structure of 
the views in the file "pages.txt". In this module the flask server
instance is also initialiced.
"""
from errors import ViewsError
from .data import load_logs, load_logs_codes
from .db import query, DataHandler, setup_table

try:
    from flask import Flask, render_template, url_for, redirect
except ImportError as e:
    e = ViewsError("004", e, "Can't import flask, try to install it using pip")
    e.show()

app = Flask(__name__)
dh = None

# Now we can declarate every route from here to the end of the file, if you need more information 
# about the routes structure check the file pages.txt
@app.route("/")
def index():
    query("example")
    return render_template("index.html")

@app.route("/wellcome")
def wellcome():
    return render_template("wellcome.html")

@app.route("/about")
def about():
    return render_template("about.html", title="About")
@app.route("/c")
def contact():
    contact = {
        "id": "001",
        "name": "Pablo",
        "surname": "Corbalán de Concepción",
        "email": "pablo.corbalan@protonmail.com",
        "phone": "571-132-141",
        "adress": "C/street1, Spain"
    }
    name = f"{contact['name']} {contact['surname']}"
    return render_template("contact.html", title=name, contact=contact)

@app.route("/c/mail")
def contactmail():
    pass

@app.route("/l")
def logsredirect():
    return redirect(url_for("logs"))

@app.route("/logs")
def logs():
    return redirect(url_for("classiclogs"))

@app.route("/l/c")
def logcodesredirect():
    return redirect(url_for("logcodes"))

@app.route("/logs/codes")
def logcodes():
    return render_template("logs/codes.html", title="Logs error codes", codes=load_logs_codes())

@app.route("/logs/codes/html")
def logcodeshtml():
    return render_template("logs/html/codes.html", title="Logs error codes - Pure HTML", codes=load_logs_codes()) 

@app.route("/logs/classic")
def classiclogs():
    return redirect(url_for("oldlogs"))

@app.route("/logs/old")
def oldlogs():
    return render_template("logs/old.html", title="Logs Old version", logs_content=load_logs())

@app.route("/logs/old/html")
def oldhtmllogs():
    return render_template("logs/html/old.html", title="Logs Old version - Pure HTML", logs_content=load_logs())

def run(DEBUG, HOSTNAME, PORT, SQL_ROUTE):
    """
    This function actually runs the application using some
    configuration variables located at the config module. 
    This function has to be runned from the run.py file
    """
    global dh
    dh = DataHandler(SQL_ROUTE)
    setup_table(dh)
    app.run(host=HOSTNAME, debug=DEBUG, port=PORT)
