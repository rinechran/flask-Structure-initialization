from application.main import *
from flask import render_template



@main_buleprint.route("/")
def index():
    return render_template("index.html")
