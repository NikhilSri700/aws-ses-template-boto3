"""
Load templates stored in json to python dictionary.
"""

import json


class Config:
    all_templates = {}

    @staticmethod
    def load_json():
        """
        Method that will load all the templates from 'config_template.json' to a python dictionary (all_templates).
        :return: None
        """
        with open("config/config_template.json", "r") as configFile:
            Config.all_templates = json.load(configFile)

