import json
from datetime import datetime
from sqlalchemy import exc, desc
from namati import db, logger, celery
from namati.models.messages import MessageReceived


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