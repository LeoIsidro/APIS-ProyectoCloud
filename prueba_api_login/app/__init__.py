from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models

from app.routes.login_bp import login_bp


app.register_blueprint(login_bp, url_prefix="/login")



db.create_all() 

