from utilities import Common
from tools.tools import writeJsonFile, logs
import os
import json


class TestLogin(Common):
    def __init__(self, userFlag):
        super().__init__(userFlag)
        self.abspath = os.path.dirname(os.path.abspath(__file__))
        self.csvpath = self.abspath+"\demoLogininfo.csv"
        self.loginPath = self.const.get("loginPath")

    def testLogin(self):
        self.csvData = self.getCsvData(False)
        self.csvData.set_index('typeuser', inplace=True)
        self.csvData = self.csvData.to_dict(orient="index")
        userData = self.csvData.get(self.roles.get(self.userflag))
        self.browser = self.sp.chromium.launch(headless=False)
        self.context = self.browser.new_context(accept_downloads=True)
        self.page = self.browser.new_page()
        self.getUrl(path=self.loginPath)
        self.getAPIUrl(flag="loginapi")
        self.setFlag("loginapi")
        self.page.route(self.apiURL, self.handle_request)
        self.page.on("response", self.handle_response)
        self.page.goto(self.testURL)
        self.page.fill("#email", userData.get("email"))
        self.page.fill("#password", userData.get("password"))
        self.page.click("#login_submit")
        self.page.wait_for_timeout(5000)
        if self.apiDATA.status == 200:
            data = self.apiDATA.body()
            if data:
                data = self.convertBytestoJson(data)
                if data.get("id_token"):
                    succemessage = " ".join(["Success Login", "JWT TOKEN",
                                             data.get("id_token")])
                    logs.info(succemessage)
                else:
                    logs.warning("Error :- " + data)
            writeJsonFile(data, self.abspath+"\login.json")
        logs.info("Login Task Finish")
        return
