from flask import Flask


def create_app():
    app = Flask('test')

    @app.route('/')
    def index():
        return 'hello,world'

    @app.route('/login')
    def login():
        return 'login'

    return app