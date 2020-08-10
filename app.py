import os
from flask import Flask
from flask_cors import CORS
import config
import logging
import api

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
    os.getpid()), datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config')
    api.api.init_app(app)

    @app.route('/')
    def InitApp():
        return 'App Init'
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
