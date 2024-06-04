from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        # DATABASE = path
    )

    from . import routes

    return app

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dev' # For development only - new key using secrets

# from xoxcharts import routes