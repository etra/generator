from typing import List
from aligator.config import Config
import logging
import sys
import os


class App:
    config: Config = None
    log: logging = None


    def __init__(self, config: Config, log: logging):
        self.config = config
        self.log = log

    @property
    def is_debug(self):
        return self.config.DEBUG

    def run(self, **kwargs):
        self.log.info(f"Starting the app... in {'debug' if self.is_debug else 'non debug'} mode")

