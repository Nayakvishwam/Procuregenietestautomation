import string
import pandas as pd
import json
import logging
import random
import time
from datetime import datetime, timedelta
import os

logging.basicConfig(level=logging.DEBUG)

logs = logging


def readCsv(path, index=False):
    return pd.read_csv(path, index_col=index)


def writeJsonFile(data, path):
    with open(path, "w") as json_file:
        json.dump(data, json_file)


def writeCsvJson(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)


def getrandomvaluebylist(data):
    return random.choice(data)


def objectFromdict(dict):
    return type('reCondition', (object,), dict)()


def generate_unique_string():
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(7))


def generate_unique_number():
    timestamp = int(time.time())
    additional_value = "123"
    unique_string = "%s%s" % (timestamp, additional_value)
    return unique_string


def getdate(numberdays, formate, todayafter=True):
    presentday = datetime.now()
    daydate = None
    if todayafter:
        daydate = presentday+timedelta(numberdays)
    else:
        daydate = presentday-timedelta(numberdays)
    return daydate.strftime(formate)


def listfilesfromDir(path):
    dir_list = os.listdir(path)
    return dir_list
