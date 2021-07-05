import os
from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app.app import create_app
from app import models


app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app)
manager = Manager(app)


@manager.command
def create_db():
    os.system('createdb namati')
    os.system('createdb test_db')
    print('Databases created')


@manager.command
def drop_db():
    os.system(
        'psql -c "DROP DATABASE IF EXISTS test_db"')
    os.system(
        'psql -c "DROP DATABASE IF EXISTS namati"')
    print('Databases dropped')


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()