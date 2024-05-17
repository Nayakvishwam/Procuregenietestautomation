from .utilities import const, directories
from playwright.sync_api import sync_playwright, expect
from tools.tools import readCsv, \
    logs, \
    getrandomvaluebylist, \
    generate_unique_string, \
    generate_unique_number, \
    getdate
import json
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Common:
    def __init__(self, userFlag):
        self.const = const()
        self.userflag = userFlag
        self.URL = self.const.get("URL")
        self.testURL = ""
        self.apis = self.const.get("apis")
        self.apiURL = ""
        self.expect = expect
        self.apiDATA = None
        self.page = None
        self.browser = None
        self.context = None
        self.sync_playwright = sync_playwright
        self.download_dir = os.path.join(os.getcwd(), 'filesstorage')
        self.roles = self.const.get("roles")
        self.csvData = {}
        self.flag = None
        self.sp = None
        self.unspcs = self.const.get("unspscs")
        self.getunspcs = self.getUnspcs()
        self.getuniqueString = generate_unique_string
        self.getuniqueNumber = generate_unique_number
        self.tommorrowdate = getdate(1, "%B %d, %Y")
        self.getcwdpath = os.getcwd()
        self.dirtectories = directories

    def buildenv(self):
        Path(self.download_dir).mkdir(parents=True, exist_ok=True)
        for path in self.dirtectories:
            path = os.path.join(self.download_dir, path)
            Path(path).mkdir(parents=True, exist_ok=True)

    def setPlayWrightPage(self, sp):
        self.sp = sp

    def setFlag(self, flag):
        self.flag = flag

    def getAPIUrl(self, **awargs):
        self.apiURL = self.const.get("APIURL")
        self.apiURL = self.apiURL+self.apis.get(awargs.get("flag"))
        return self.apiURL

    def getUrl(self, **awargs):
        self.testURL = self.URL+awargs.get("path")
        return

    def getCsvData(self, removeIndex):
        return readCsv(self.csvpath, removeIndex)

    def handle_response(self, response):
        logs.debug(response.url)
        if self.getAPIUrl(flag=self.flag) in response.url:
            self.apiDATA = response

    def handle_request(self, route, request):
        if self.getAPIUrl(flag=self.flag) in request.url:
            route.continue_()
        else:
            route.continue_()

    def getUnspcs(self):
        unspcs = getrandomvaluebylist(self.unspcs)
        return unspcs

    def convertBytestoJson(self, data):
        json_str = data.decode('utf-8')
        data = json.loads(json_str)
        return data

    def getelementByPosition(self, attributeStrIndenity, attributeName, position):
        return self.page.query_selector(
            attributeStrIndenity +
            attributeName +
            ':nth-child(%s)' % (position)
        )
