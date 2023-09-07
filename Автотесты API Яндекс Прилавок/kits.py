import requests

import configuration
import data
import helper


def create_new_user():
    return requests.post (configuration.URL + configuration.CREATE_NEW_USER, json=data.CREATE_NEW_USER_BODY)

def create_kit(token, body):
    return requests.post (configuration.URL + configuration.CREATE_KIT, json = body,
        headers = {"Authorization": "Bearer "+ token})



