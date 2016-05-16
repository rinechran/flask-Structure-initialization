from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder=None)
db = SQLAlchemy(app)

from application.config import *
app.config.from_object(Config)


from application.main import main_buleprint
app.register_blueprint(main_buleprint)
