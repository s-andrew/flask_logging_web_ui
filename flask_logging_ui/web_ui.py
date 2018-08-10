import sqlite3

from flask import Blueprint, render_template, jsonify


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_logs_from_sqlite(db):
    with sqlite3.connect(db) as conn:
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM log ORDER BY TimeStamp DESC;')
        logs = cursor.fetchall()
        cursor.close()
    return logs


def logging_blueprint_factory(db='app.db'):
    logging_blueprint = Blueprint('log_page', __name__, template_folder='templates', static_folder='static')

    @logging_blueprint.route('/')
    def logs():
        logs = get_logs_from_sqlite(db)
        return render_template('logs.html', logs=logs)

    @logging_blueprint.route('/api')
    def api():
        logs = get_logs_from_sqlite(db)
        return jsonify(logs)

    @logging_blueprint.route('/api/headers')
    def headers():
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM log LIMIT 0;')
            headers = tuple(map(lambda x: x[0], cursor.description))
            cursor.close()
        return jsonify(headers)

    return logging_blueprint
