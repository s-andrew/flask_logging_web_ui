import logging.config
import logging.handlers
import json

from flask import Flask
from flask_cors import CORS

from flask_logging_ui import flask_logging_ui
from busines_logic import BusinesLogic


with open('config/logging.json') as file:
    log_config = json.loads(file.read())
logging.config.dictConfig(log_config)


def flask_app_factory():
    app = Flask(__name__)
    flask_logging_ui(app, db='logs/app.db', url_prefix='/logs')
    CORS(app)
    bl = BusinesLogic()

    @app.route('/')
    def index():
        app.logger.debug('index')
        bl.do(list(range(3)))
        return 'Hello world'

    return app