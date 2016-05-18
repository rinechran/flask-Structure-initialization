from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder=None)

from application.config import *
app.config.from_object(Config)

db = SQLAlchemy(app)




from application.main import main_buleprint
app.register_blueprint(main_buleprint)
