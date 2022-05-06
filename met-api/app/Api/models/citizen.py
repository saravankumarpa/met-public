from flask.app import Flask
from sqlalchemy.sql.schema import ForeignKey
from .db import  db, ma
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import text

class Citizen(db.Model):
    # Name of the table in our database
    __tablename__ = 'citizen'
    
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50))
    email_id = db.Column(db.String(50))
    contact_number = db.Column(db.String(50), nullable=True)
    created_date = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    updated_date = db.Column(db.DateTime, onupdate=datetime.datetime.now)
  