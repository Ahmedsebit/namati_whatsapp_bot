import json
from datetime import datetime
from sqlalchemy import exc, desc
from app.app import db
from app.models.user_sessions import UserSessions


def add_session(phone_number, level):
    
    user_session = UserSessions(
        phone_number = phone_number,
        level = level
    )
    db.session.add(user_session)
    db.session.commit()


def get_user_session(phone_number):
    
    user_session = UserSessions.query.filter_by(phone_number = phone_number).order_by(desc(UserSessions.created_at)).first()
    response = None
    if user_session:
        response = dict(
            id = user_session.id,
            session_metadata = user_session.session_metadata,
            created_at = user_session.created_at,
            updated_at = user_session.updated_at,
            phone_number = user_session.phone_number,
            journey = user_session.journey,
            level = user_session.level,
            results = user_session.results,
            status = user_session.status
        )
    return response
    
    
def update_level_session(phone_number, results):
    
    user_session = UserSessions.query.filter_by(phone_number = phone_number).order_by(desc(UserSessions.created_at)).first()
    user_session.updated_at = datetime.now()
    user_session.level = user_session.level + 1
    user_session.results = results
    db.session.add(user_session)
    db.session.commit()
    

def update_journey_session(phone_number, journey):
    
    user_session = UserSessions.query.filter_by(phone_number = phone_number).order_by(desc(UserSessions.created_at)).first()
    user_session.updated_at = datetime.now()
    user_session.journey = journey
    db.session.add(user_session)
    db.session.commit()
    
    
def end_session(phone_number):
    
    user_session = UserSessions.query.filter_by(phone_number = phone_number).order_by(desc(UserSessions.created_at)).first()
    user_session.updated_at = datetime.now()
    user_session.status = 'Inactive'
    db.session.add(user_session)
    db.session.commit()