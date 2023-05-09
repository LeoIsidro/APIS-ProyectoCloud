from enum import unique

from sqlalchemy import PrimaryKeyConstraint
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    score = db.relationship('Score', backref='user', lazy='dynamic')

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    points = db.Column(db.String(64), index=True)
    user_username = db.Column(db.String(64), db.ForeignKey('usuario.username'))

db.create_all()    