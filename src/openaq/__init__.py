import os
import json
import requests
import openaq.jsonutil as ju
import openaq.API as api

class OpenAQ:

    def __init__(self):
        """
        This class is responsible for making the openAQ calls.
        """
        self.ju = ju.JSONUtil()
        self.apiC = api.API()


    def get_city(self, city=""):
        if city != "":
            params = {'city':city,'limit':'20','page':'145'}

        params = {'limit':'20','page':'148'}

        return self.apiC.retrieve_all_data("cities", params)

    def get_latest(self, parameters={}):
        if parameters == {}:
            parameters = {'limit':'20','page':'20','country':'IN'}
        latest_data = self.apiC.retrieve_all_data("latest", parameters)
        return self.ju.format_latest_json(latest_data)

