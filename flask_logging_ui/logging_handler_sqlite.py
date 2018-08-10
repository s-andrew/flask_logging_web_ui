import sqlite3
import logging
import time

__version__ = "0.1.0"


initial_sql = """CREATE TABLE IF NOT EXISTS log(
                    TimeStamp TEXT,
                    Source TEXT,
                    LogLevel INT,
                    LogLevelName TEXT,
                    Message TEXT,
                    Args TEXT,
                    Module TEXT,
                    FuncName TEXT,
                    LineNo INT,
                    Exception TEXT,
                    Process INT,
                    Thread TEXT,
                    ThreadName TEXT
               )"""

insertion_sql = """INSERT INTO log(
                    TimeStamp,
                    Source,
                    LogLevel,
                    LogLevelName,
                    Message,
                    Args,
                    Module,
                    FuncName,
                    LineNo,
                    Exception,
                    Process,
                    Thread,
                    ThreadName
               )
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
               """


class SQLiteHandler(logging.Handler):
    """
    Thread-safe logging handler for SQLite.
    """

    def __init__(self, db='app.db'):
        logging.Handler.__init__(self)
        self.db = db
        with sqlite3.connect(self.db) as conn:
            conn.execute(initial_sql)
            conn.commit()
        return

    def format_time(self, record):
        """
        Create a time stamp
        """
        record.dbtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        return

    @staticmethod
    def prepared_params(record):
        d = record.__dict__
        return (
            d['dbtime'],
            d['name'],
            d['levelno'],
            d['levelname'],
            d['msg'],
            str(d['args']),
            d['module'],
            d['funcName'],
            d['lineno'],
            d['exc_text'],
            d['process'],
            str(d['thread']),
            d['threadName']
        )

    def emit(self, record):
        self.format(record)
        self.format_time(record)
        if record.exc_info:  # for exceptions
            record.exc_text = logging._defaultFormatter.formatException(record.exc_info)
        else:
            record.exc_text = ""

        # Insert the log record
        params = self.prepared_params(record)
        with sqlite3.connect(self.db) as conn:
            conn.execute(insertion_sql, params)
            conn.commit()  # not efficient, but hopefully thread-safe
        return