from app import flask_app_factory


if __name__ == '__main__':
    app = flask_app_factory()
    app.run('localhost', 5000, debug=True)
