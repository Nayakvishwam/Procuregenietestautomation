import os
import json


def const():
    _filepath = str(os.getcwd())+"\const.json"
    data = {}
    with open(_filepath, 'r') as f:
        data = json.load(f)
    return data

directories=["createbid"]