import os
import enum
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy.dialects.postgresql import ENUM
from namati.app import db


class MessageReceived(db.Model):
    '''
    This class represents the lca messages_received table.
    '''
    
    __tablename__ = 'messages'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    message_metadata = db.Column(JSONB)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(255))
    response = db.Column(db.String(255))
    
    def __init__(self, message_metadata, status, response):
        
        self.message_metadata = message_metadata
        self.status = status
        self.response = response

    def __repr__(self):
        return "<MessagesReceived: {}>".format(self.id)
    
    
# class MessageReceived(db.Model):
#     '''
#     This class represents the lca messages_received table.
#     '''
    
#     __tablename__ = 'messages'
#     __table_args__ = {'schema': 'public'}

#     id = db.Column(db.Integer, primary_key=True)
#     message_metadata = db.Column(JSONB)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     status = db.Column(db.String(255))
#     response = db.Column(db.String(255))
    
#     def __init__(self, message_metadata, status, response):
        
#         self.message_metadata = message_metadata
#         self.status = status
#         self.response = response

#     def __repr__(self):
#         return "<MessagesReceived: {}>".format(self.id)
    