import logging
from .web_ui import logging_blueprint_factory
from .logging_handler_sqlite import SQLiteHandler


def flask_logging_ui(app, db='app.db', url_prefix='/logs'):
    handler = SQLiteHandler(db)
    handler.setLevel(logging.DEBUG)
    logging.getLogger().addHandler(handler)
    app.register_blueprint(logging_blueprint_factory(db), url_prefix=url_prefix)
