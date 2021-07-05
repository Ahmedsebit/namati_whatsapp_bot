import os
import enum
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy.dialects.postgresql import ENUM
from app.app import db



class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(JSONB)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    phone_number = db.Column(db.String(255))
    
    def __init__(self, phone_number):
        
        self.phone_number = phone_number

    def __repr__(self):
        return "<Users: {}>".format(self.id)
    
    
class UserSessions(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    session_metadata = db.Column(JSONB)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    phone_number = db.Column(db.String(255))
    journey = db.Column(db.String(255))
    status = db.Column(db.String(255), default='Active')
    level = db.Column(db.Integer)
    results = db.Column(db.Boolean, default=True)
    
    def __init__(self, phone_number, level):
        
        self.phone_number = phone_number
        self.level = level

    def __repr__(self):
        return "<UserSessions: {}>".format(self.id)
    