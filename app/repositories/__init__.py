from app.models.messages import db
from app.repositories.messages import add_message
from app.repositories.user_sessions import get_user_session, update_level_session, add_session, update_journey_session, end_session
from app.repositories.users import add_user, get_user


def healthcheck_db():
    is_database_working = True
    output = 'database is ok'
    try:
        # to check database we will execute raw query
        db.session.execute('SELECT 1')
    except Exception as e:
        output = str(e)
        is_database_working = False

    return is_database_working, output