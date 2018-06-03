import os
from logging import StreamHandler

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_rq import RQ
from flask_debugtoolbar import DebugToolbarExtension

def create_app(config_object=None, db_name=None):  # pragma: no cover
    app = Flask(__name__)

    from dotenv import load_dotenv
    load_dotenv(".env")
    
    if config_object is None:
        app.config.from_object('config.BaseConfiguration')
    else:
        app.config.from_object(config_object)

    if not app.logger.handlers:
        stream_handler = StreamHandler()
        app.logger.addHandler(stream_handler)

    if app.debug:
        app.logger.setLevel("DEBUG")
        app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
        app.config["DEBUG_TB_PROFILER_ENABLED"] = os.environ.get("PROFILER", "False") == 'True'
        app.config['RQ_DEFAULT_URL'] = os.environ.get("REDIS_URL")
    else:
        app.logger.setLevel("DEBUG")

    RQ(app)
    Bootstrap(app)
    DebugToolbarExtension(app)

    from chatbot.views import chatbot_bp
    app.register_blueprint(chatbot_bp)

    return app
