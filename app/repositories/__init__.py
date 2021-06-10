from app.models.messages import db
from app.repositories.messages import add_message

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