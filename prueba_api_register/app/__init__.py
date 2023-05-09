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

from app.routes.register_bp import register_bp


app.register_blueprint(register_bp, url_prefix="/register")



db.create_all() 

