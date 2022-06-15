"""
Load templates stored in json to python dictionary.
"""

import json


class Config:
    all_templates = {}

    @staticmethod
    def load_json():
        with open("config/config_email_template.json", "r") as configFile:
            Config.all_templates = json.load(configFile)

