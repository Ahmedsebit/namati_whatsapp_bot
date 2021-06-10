import os
from namati.app import create_app


config_name = os.getenv('APP_SETTINGS')

APP = create_app(config_name)


if __name__ == '__main__':
    APP.secret_key = "secret_key"
    APP.run()