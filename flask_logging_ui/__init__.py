import logging
from .web_ui import logging_blueprint_factory
from .logging_handler_sqlite import SQLiteHandler
from .logging_filter import LogsUrlFilter


def flask_logging_ui(app, db='app.db', url_prefix='/logs', logger=logging.getLogger()):
    logs_url_filter = LogsUrlFilter(name='logs_url_filter', url_prefix=url_prefix)
    handler = SQLiteHandler(db)
    handler.addFilter(logs_url_filter)
    handler.setLevel(0)
    logger.addHandler(handler)
    app.register_blueprint(logging_blueprint_factory(db), url_prefix=url_prefix)
