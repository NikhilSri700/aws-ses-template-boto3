"""
Load templates stored in json to python dictionary.
"""

import json


class Config:
    all_templates = {}
    user_data = []
    destinations = []

    @staticmethod
    def load_template_json():
        """
        Method that will load all the templates from 'config_template.json' to a python dictionary (all_templates).
        :return: None
        """
        with open("config/config_template.json", "r") as configFile:
            Config.all_templates = json.load(configFile)

    @staticmethod
    def load_user_json():
        """
        Method that will load data of all the users from 'user_data.json' to a python list (user_data).
        :return: None
        """
        with open("config/user_data.json", "r") as configFile:
            Config.user_data = json.load(configFile)

    @staticmethod
    def load_destination_json():
        """
        Method that will load all the destinations from 'email_destinations.json' to a python list (destinations).
        :return: None
        """
        with open("config/email_destinations.json", "r") as configFile:
            Config.destinations = json.load(configFile)

    @staticmethod
    def load_jsons():
        Config.load_template_json()
        Config.load_user_json()
        Config.load_destination_json()

