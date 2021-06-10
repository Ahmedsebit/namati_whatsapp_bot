import json
import logging
import re
import os
from datetime import datetime
from flask_api import FlaskAPI, status
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config
from flask_swagger_ui import get_swaggerui_blueprint
import os
from celery import Celery
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

celery = Celery(__name__, backend=os.getenv('CELERY_BACKEND'), broker=os.getenv('CELERY_BROCKER'))
db = SQLAlchemy()
migrate = Migrate(db)


### swagger specific ###
API_URL = '/static/swagger.json'
URL_PREFIX = '/namati/v1'
URL_PREFIX_V2 = '/namati/v2'
  

logger = logging.getLogger(__name__)


def create_app(config_name):
    '''
    Wraps the creation of a new Flask object, and returns it after it's loaded up
    with configuration settings using app.config and connected to the DB using
    '''
    
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 10
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 120
    app.config['SQLALCHEMY_POOL_PRE_PING'] = True
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_IDENTITY_CLAIM'] = 'jti'
    
    jwt = JWTManager(app)
    
    app.app_context().push()
    log_level = logging.INFO
    app.logger.setLevel(log_level)
    
    import namati.api.v1.messages as api_v1
    
    db.init_app(app)
    
    celery.conf.update(app.config)
    
    app.register_blueprint(api_v1.namati_v1_api_bp, url_prefix=URL_PREFIX)
    
    @app.teardown_request
    def teardown_request(exception):
        if exception:
            db.session.rollback()
        db.session.remove()

    return app
