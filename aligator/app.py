from typing import List
from aligator.config import Config
from aligator.db import DB
from aligator.scenario import get_scenario
import logging
import sys
import os


class App:
    config: Config = None
    log: logging = None
    db: DB = None

    def __init__(self, config: Config, log: logging, db: DB):
        self.config = config
        self.log = log
        self.db = db

    @property
    def is_debug(self):
        return self.config.DEBUG

    def run(self, **kwargs):
        # scenario = get_scenario('custom', self, {'name': 'custom_scenerio'})
        scenario = get_scenario('early_expansion', self, {'name': 'custom_scenerio'})
        scenario.run_scenario()
        # scenario = ScenarioOne(self.app)
        #
        # scenario = ScenarioCustom(self.app, paramas={
        #     'start_date': '2024-01-01',
        #     'end_date': '2024-12-31',
        #     'users': {
        #         'statr_with': 1,
        #         'increase by': 0.1%,
        #         'max': 1000
        #         '....'
        #     },
        #     ''
        # })



        self.log.info(f"Starting the app... in {'debug' if self.is_debug else 'non debug'} mode")

