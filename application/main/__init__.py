from flask import Blueprint
from flask import render_template



main_buleprint = Blueprint("main",__name__,template_folder="templates",static_folder='static')



from application.main.controller import *
