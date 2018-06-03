# https://realpython.com/blog/python/python-web-applications-with-flask-part-iii/#.Uu-xVnddUp9
import os
import pymongo
import logging

log = logging.getLogger(__name__)


class BaseConfiguration(object):
    APP_ENV = os.environ.get("APP_ENV")
    WTF_CSRF_ENABLED = False
    DEBUG = os.environ.get("DEBUG_MODE") == "True"

    """
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGO_DB_NAME"),
        'host': os.environ.get("MONGO_URL")
    }
    """
    RQ_DEFAULT_URL = os.environ.get("REDIS_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ASYNC_RQ = os.environ.get("ASYNC_RQ", True)


def get_facebook_db():
    FACEBOOK_MONGO_URL = os.environ.get("FACEBOOK_MONGO_URL", "mongodb://localhost/facebook")
    facebook_client = pymongo.MongoClient(FACEBOOK_MONGO_URL)
    return facebook_client.get_default_database()