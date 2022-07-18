from click import password_option
from .database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'User'
    username = db.Column(db.String, unique=True,primary_key=True)
    password=db.Column(db.String,nullable=False)

class List(db.Model):
    __tablename__ = 'List'
    name = db.Column(db.String, primary_key=True,)
    description = db.Column(db.String)
    user = db.Column(db.String,   db.ForeignKey("User.username"), nullable=False)

class Card(db.Model):
    __tablename__ = 'Card'
    list_name = db.Column(db.String,   db.ForeignKey("List.name"), nullable=False)
    card_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False) 
    title = db.Column(db.String,nullable=False)
    content = db.Column(db.String)
    deadline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    iscomplete = db.Column(db.Boolean, nullable=False, default=False)

