import json
from datetime import datetime
from sqlalchemy import exc, desc
from app.app import db
from app.app import logger
from app.models.messages import MessageReceived
from app.app import celery


def add_message(message_metadata, status, response):
    
    try:
        message = MessageReceived(
            message_metadata = message_metadata, 
            status = status, 
            response = response
        )
        logger.info(f'{datetime.now()} - Info - Namati_Bot - new message received')
        db.session.add(message)
        db.session.commit()
        return dict(
            message_metadata = message_metadata, 
            status = status, 
            response = response
        )
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f'{datetime.now()} - Error - Namati_Bot - receiving new message failed due to {e}')
        return []
    else:
        db.session.rollback()
        logger.error(f'{datetime.now()} - Error - Namati_Bot - receiving new message failed')
        return []
    finally:
        db.session.close()