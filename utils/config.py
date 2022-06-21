"""
Load templates stored in json to python dictionary.
"""

import json


class Config:

    @staticmethod
    def load_json(file_name):
        """
        Method that will convert json objects python dictionaries or lists.
        :return: dict/list
        """
        with open(file_name, "r") as configFile:
            return json.load(configFile)

