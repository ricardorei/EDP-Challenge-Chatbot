# manage.py
import sys
from flask import url_for
from flask_script import Manager, Command, Option, Server

import logging
logging.info("Starting Logger for EDP-Challenge Chatbot")

from chatbot import create_app

app = create_app()
manager = Manager(app)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

        
if __name__ == "__main__":
    manager.run()