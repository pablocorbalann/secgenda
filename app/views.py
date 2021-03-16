# This file is part of: github.com/pablocorbalann/secgenda
"""
The views module (from the app package), contains all the
viws and pages of the application, you can learn more about the structure of 
the views in the file "pages.txt". In this module the flask server
instance is also initialiced.
"""
from errors import ViewsError
from data import load_logs

try:
    from flask import Flask, render_template, url_for, redirect
except ImportError as e:
    e = ViewsError("004", e, "Can't import flask, try to install it using pip")
    e.display()

app = Flask(__name__)

# Now we can declarate every route from here to the end of the file, if you need more information 
# about the routes structure check the file pages.txt
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/wellcome")
def wellcome():
    return render_template("wellcome.html")

@app.route("/logs/old")
def oldlogs():
    return render_template("logs.txt", title="Logs Old version", logs=load_logs())

def run(DEBUG, HOSTNAME, PORT):
    """
    This function actually runs the application using some
    configuration variables located at the config module. 
    This function has to be runned from the run.py file
    """
    app.run(host=HOSTNAME, debug=DEBUG, port=PORT)
