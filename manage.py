from aligator.app import App
from aligator.config import config
from aligator.log import log
from aligator.db import db
import ssl

# Disable certificate verification globally
ssl._create_default_https_context = ssl._create_unverified_context

from logging import basicConfig, Handler
from dotenv import load_dotenv
load_dotenv()
import os
import sys



if __name__ == '__main__':
    app = App(config=config, log=log, db=db)
    app.run()
    # app.test()
