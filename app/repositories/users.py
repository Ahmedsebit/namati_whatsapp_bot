import json
from datetime import datetime
from sqlalchemy import exc, desc
from app.app import db
from app.models.user_sessions import Users


def add_user(phone_number):
    
    user = Users(
        phone_number = phone_number
    )
    db.session.add(user)
    db.session.commit()


def get_user(phone_number):
    
    user = Users.query.filter_by(phone_number = phone_number).first()
    response = None
    if user:
        response = dict(
            id = user.id,
            created_at = user.created_at,
            phone_number = user.phone_number
        )
    return response
    
