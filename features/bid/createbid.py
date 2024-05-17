from utilities import Common
import os
from tools.tools import objectFromdict, \
    logs, \
    listfilesfromDir, \
    writeCsvJson, \
    writeJsonFile


class createBid(Common):
    def __init__(self, userFlag):
        super().__init__(userFlag)
        self.bidabspath = os.path.dirname(os.path.abspath(__file__))
        self.bidcsvpath = self.bidabspath
        self.docspath = self.bidabspath+"\\docs\\uploaddocs\\"
        self.downloadpath = self.download_dir+"\createbid"
        self.uploadfilesname = listfilesfromDir(self.docspath)
        self.createBidPath = self.const.get("createBidPath")
        self.selectorbid = "mat-list-item[title='Create Bid']"
        self.selectorbidOption = "mat-list-item[title='Bid']"
        self.bidconditions = self.const.get("bidconditions")
        self.requesttype = ".mat-form-field"
        self.requesttypetagdiv = "cdk-overlay-pane"
        self.requesttypetag = "mat-form-field[class='%s']" % (self.requesttype)
        self.requesttypeselect = "div[class='%s']" % (self.requesttypetagdiv)
        self.requesttypetagmaindiv = "mat-select-panel"
        self.tabs = None
        self.requesttypebyids = {
            "RFQ (Request For Quotation)": 1,
            "RFP (Request For Proposal)": 2
        }
        self.evaluationtypes = {
            "Grand Total Wise": 1,
            "Item Wise": 2,
            "Event Wise": 3,
        }
        self.envlopes = {
            "RFQ (Request For Quotation)": [1, 2],
            "RFP (Request For Proposal)": [2]
        }
        self.biddetailsselectclass = "#ng-star-inserted"
        self.biddingtypes = {
            "Domestic": 1,
            "Global": 2
        }
        self.evaluationprogress = {
            "Single Stage": 1,
            "Multi Stage": 2
        }
        self.biddingaccess = {
            "Open": 1,
            "Limited": 2,
            "Single": 3
        }
        self.eventfor = {
            "Purchase": 1,
            "Sell": 2
        }
        self.applicableData = {
            "Applicable": 1,
            "Not Applicable": 2
        }
        self.mapbiddertype = {
            "Event Wise": 2,
            "Item Wise": 3,
            "Lot Wise": 3
        }
        self.bidsData = []
        self.filteredBidsData = []
        self.errors = []

    def deparmentfill(self, bidetailsaccrodino, position):
        deparment = bidetailsaccrodino.query_selector(
            "div.col-sm-6:nth-child(%s)" % (position))
        deparment.click()
        deparmentoption = self.getelementByPosition(
            '.', "multi-select-option", 1)
        deparmentoption.click()

    def bidNofill(self, bidetailsaccrodino, position):
        bidNo = bidetailsaccrodino.query_selector(
            "div.col-sm-6:nth-child(%s)" % (position))
        input_bidNo = bidNo.query_selector("input")
        input_bidNo.fill(self.getuniqueString())

    def officerfill(self, bidetailsaccrodino, position):
        officer = bidetailsaccrodino.query_selector(
            "div.col-sm-6:nth-child(%s)" % (position))
        officer.click()
        officeroption = self.getelementByPosition(
            '.', "mat-option", 1)
        officeroption.click()

    def brieffill(self, bidetailsaccrodino, bid, position):
        brief = bidetailsaccrodino.query_selector(
            "div.col-sm-6:nth-child(%s)" % (position))
        input_brief = brief.query_selector("input")
        input_brief.fill(bid.bidbrief)

    def envolpefill(self, bidetailsaccrodino, bid):
        envolpe = bidetailsaccrodino.query_selector(
            "div.col-sm-6:nth-child(6)")
        envolpe.click()
        choices = self.envlopes.get(bid.requesttype)
        self.page.wait_for_timeout(1000)
        for index in range(len(choices)):
            choice = choices[index]
            self.page.wait_for_timeout(1000)
            matpseudoCheckbox = self.getelementByPosition(
                '.', 'mat-option', choice)
            matpseudoCheckbox.click()
            self.page.wait_for_timeout(3000)
        self.page.press('body', 'Escape')

    def eventfill(self, bidConfiguration):
        event = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(1)")
        input_event = event.query_selector("input")
        input_event.fill(self.getuniqueNumber())

    def projectdurationfill(self, bidConfiguration):
        event = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(2)")
        input_event = event.query_selector("input")
        input_event.fill("12")

    def evaluationfill(self, bidConfiguration, optionNumber):
        evaluation = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(3)")
        evaluation.click()
        evaluationoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        evaluationoption.click()

    def biddingTypefill(self, bidConfiguration, optionNumber):
        bidding = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(4)")
        bidding.click()
        self.page.wait_for_timeout(1500)
        biddingoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        biddingoption.click()

    def evaluationprocessfill(self, bidConfiguration, optionNumber):
        evaluationprocess = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(5)")
        evaluationprocess.click()
        self.page.wait_for_timeout(1000)
        evaluationprocessoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        evaluationprocessoption.click()

    def biddingaccessfill(self, bidConfiguration, optionNumber):
        biddingaccess = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(6)")
        biddingaccess.click()
        self.page.wait_for_timeout(1000)
        biddingaccessoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        biddingaccessoption.click()

    def eventforfill(self, bidConfiguration, optionNumber):
        eventfor = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(7)")
        eventfor.click()
        self.page.wait_for_timeout(1000)
        eventforoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        eventforoption.click()

    def applicablefill(self, bidConfiguration, position, optionNumber):
        self.page.wait_for_timeout(1000)
        applicable = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(%s)" % (position))
        applicable.click()
        self.page.wait_for_timeout(1000)
        applicableoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        applicableoption.click()

    def mapbiddertypefill(self, bidConfiguration, optionNumber):
        mapbiddertype = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(7)")
        mapbiddertype.click()
        self.page.wait_for_timeout(1000)
        mapbiddertypeoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        mapbiddertypeoption.click()

    def workflowrequriedfill(self, bidConfiguration, position, optionNumber):
        workflowrequried = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(%s)" % (position))
        workflowrequried.click()
        self.page.wait_for_timeout(1000)
        workflowrequriedoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        workflowrequriedoption.click()

    def enddatefill(self, Dates, position):
        submissondate = Dates.query_selector(
            "div.col-sm-6:nth-child(%s)" % (position))
        calenbdar = submissondate.query_selector_all(
            "div.mat-form-field-suffix")
        calenbdar = calenbdar[0]
        calenbdar.click()
        self.page.wait_for_timeout(1000)
        date = self.page.query_selector(f'[aria-label="{self.tommorrowdate}"]')
        date.click()
        button = self.page.query_selector("button.mat-stroked-button")
        button.click()

    def gotToCreateBidOption(self, double=False):
        self.page.wait_for_selector(self.selectorbidOption)
        self.page.click(self.selectorbidOption)
        if double:
            self.page.click(self.selectorbidOption)
        self.page.wait_for_selector(self.selectorbid)
        self.page.click(self.selectorbid)
        self.page.wait_for_selector(self.requesttype)

    def submitbid(self):
        maindiv = self.page.query_selector(
            ".mat-horizontal-content-container")
        submit = maindiv.query_selector(".mat-raised-button")
        submit.click()
        self.page.wait_for_timeout(3000)
        submit.click()
        self.page.wait_for_timeout(3000)

    def curreccyBid(self, bidConfiguration, optionNumber):
        curreccyBidrequried = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(9)")
        curreccyBidrequried.click()
        self.page.wait_for_timeout(1000)
        curreccyBidoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        curreccyBidoption.click()
        self.page.press('body', 'Escape')

    def basecurreccyBid(self, bidConfiguration, optionNumber):
        basecurreccyBidrequried = bidConfiguration.query_selector(
            "div.col-sm-6:nth-child(10)")
        basecurreccyBidrequried.click()
        self.page.wait_for_timeout(1000)
        basecurreccyBidoption = self.getelementByPosition(
            '.', "mat-option", optionNumber)
        basecurreccyBidoption.click()

    def uploaddocuments(self, uploaddocumenttab):
        uploadfile = self.page.query_selector('input[type="file"]')
        field_description = self.page.query_selector(
            'input[id="field_description"]')
        saveEntity = self.page.query_selector("button[id='save-entity']")
        for file in self.uploadfilesname:
            uploadfile.set_input_files(self.docspath+file)
            filename = file.split(".")
            field_description.fill(filename[0])
            saveEntity.click()
        buttons = self.page.query_selector_all(".mat-button-wrapper")
        buttons[5].click()
        buttons[7].click()
        uploaddocumenttab.click()
        self.page.wait_for_timeout(1000)
        tablerows = self.page.query_selector_all("tr")
        self.page.wait_for_timeout(1000)
        buttons = tablerows[3].query_selector_all("button")
        removebtn = buttons[1]
        removebtn.click()
        self.context.on('download', lambda download: download.save_as(
            self.download_dir+"createbid"))
        self.page.wait_for_timeout(3000)
        tablerows.pop(3)
        tablerows.pop(0)
        for index in range(len(tablerows)):
            data = tablerows[index]
            file = self.uploadfilesname[index]
            buttons = data.query_selector_all("button")
            dwnbtn = buttons[0]
            dwnbtn.click()
            download = self.page.wait_for_event('download')
            download_file_path = os.path.join(self.downloadpath, file)
            download.save_as(download_file_path)
            self.page.wait_for_timeout(5000)
        self.page.wait_for_timeout(1000)
        data = self.apiDATA.body()
        data = self.convertBytestoJson(data)
        if data.get("status") == 200:
            logs.info(data.get("message"))
        else:
            logs.warning("Document is not download successfully!")
        buttons = self.page.query_selector_all(".mat-button-wrapper")
        self.page.wait_for_timeout(2000)
        buttons[7].click()
        self.page.wait_for_timeout(2000)

    def biddingform(self):
        maindiv = self.page.query_selector(
            ".mat-horizontal-content-container")
        buttons = maindiv.query_selector_all("button")
        buttons[len(buttons)-2].click()
        self.page.wait_for_timeout(2000)

    def createBid(self, bid, index):
        if index != 0:
            self.gotToCreateBidOption(True)
        tag = self.getelementByPosition('.', 'mat-form-field', 1)
        tag.click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector(self.requesttypeselect)
        tag = self.getelementByPosition('.', self.requesttypetagmaindiv, 1)
        tag.wait_for_selector("mat-option")
        tag = tag.query_selector_all("mat-option")
        bid = self.bidconditions[index]
        bid = objectFromdict(bid)
        requesttype = self.requesttypebyids.get(bid.requesttype)
        requesttypeoption = tag[requesttype]
        requesttypeoption.click()
        self.page.wait_for_selector("mat-accordion[class='mat-accordion']")
        form_group = self.page.query_selector_all(".form-group")
        accordinos = form_group[1].query_selector_all(
            ".mat-accordion")
        unspcs = form_group[1].query_selector(
            ".col-6:nth-child(2)")
        input_department = unspcs.query_selector("input")
        input_department.fill(self.getunspcs)
        bidetailsaccrodino = accordinos[0]
        bidetailsaccrodino.click()
        if requesttype == 1:
            self.deparmentfill(bidetailsaccrodino, 1)
            self.bidNofill(bidetailsaccrodino, 2)
        elif requesttype == 2:
            self.bidNofill(bidetailsaccrodino, 1)
            self.deparmentfill(bidetailsaccrodino, 2)
        if requesttype == 1:
            self.officerfill(bidetailsaccrodino, 3)
            self.brieffill(bidetailsaccrodino, bid, 4)
        elif requesttype == 2:
            self.brieffill(bidetailsaccrodino, bid, 3)
            self.officerfill(bidetailsaccrodino, 4)
        self.envolpefill(bidetailsaccrodino, bid)
        bidConfiguration = accordinos[1]
        bidConfiguration.click()
        self.eventfill(bidConfiguration)
        self.projectdurationfill(bidConfiguration)
        evaluationoption = self.evaluationtypes.get(bid.evaluationtype)
        self.evaluationfill(bidConfiguration, evaluationoption)
        biddingtypeoption = self.biddingtypes.get(bid.biddingtype)
        self.biddingTypefill(bidConfiguration, biddingtypeoption)
        evaluationprogressoption = self.evaluationprogress.get(
            bid.evaluationprogress)
        self.evaluationprocessfill(
            bidConfiguration, evaluationprogressoption)
        biddingaccessoption = self.biddingaccess.get(
            bid.biddingaccess)
        self.biddingaccessfill(
            bidConfiguration, biddingaccessoption)
        eventforoption = self.eventfor.get(
            bid.eventfor)
        self.eventforfill(
            bidConfiguration, eventforoption)
        bidWithdrawaloption = self.applicableData.get(
            bid.bidWithdrawal)
        bidWithdrawalposition = 9
        if bid.biddingtype == "Global":
            currecyposition = 2
            self.curreccyBid(bidConfiguration, currecyposition)
            currecyposition = 1
            self.basecurreccyBid(bidConfiguration, currecyposition)
            bidWithdrawalposition += 2
        if bid.mapbiddertype and bid.biddingaccess != "Open":
            bidWithdrawalposition += 1
        if bid.mapbiddertype:
            mapbidderposition = self.mapbiddertype.get(bid.mapbiddertype)
            self.mapbiddertypefill(bidConfiguration, mapbidderposition)
        self.applicablefill(
            bidConfiguration, bidWithdrawalposition, bidWithdrawaloption)
        prebidmeetingoption = self.applicableData.get(
            bid.prebidmeeting)
        prebidmeetingposition = bidWithdrawalposition+1
        self.applicablefill(
            bidConfiguration, prebidmeetingposition, prebidmeetingoption)
        workflowposition = prebidmeetingposition+1
        self.workflowrequriedfill(
            bidConfiguration, workflowposition, 2)
        bidConfiguration.click()
        datesaccrodino = accordinos[2]
        datesaccrodino.click()
        self.enddatefill(datesaccrodino, 1)
        self.page.wait_for_timeout(1000)
        self.submitbid()
        self.page.wait_for_timeout(8000)
        data = self.apiDATA.body()
        data = self.convertBytestoJson(data)
        if data.get("status") == 200:
            self.filteredBidsData.append(
                {
                    k: v for k, v in data.get("result").items()
                    if v is not None
                }
            )
            logs.info(data.get("message"))
            self.page.wait_for_timeout(5000)
            return True
        else:
            logs.error("Bid Not added successfully")
            self.page.wait_for_timeout(12000)
            return False

    def newBid(self):
        try:
            self.gotToCreateBidOption()
            for index in range(len(self.bidconditions)):
                self.getAPIUrl(flag="createbidapi")
                self.setFlag("createbidapi")
                self.page.route(self.apiURL, self.handle_request)
                self.page.on("response", self.handle_response)
                bid = self.bidconditions[index]
                # Create Bid Tab Process Finish
                nextprocess = self.createBid(bid, index)
                if nextprocess:
                    maintab = self.page.query_selector_all(
                        ".mat-horizontal-stepper-header-container")
                    maintab = maintab[0]
                    self.tabs = maintab.query_selector_all("mat-step-header")
                    uploaddocumenttab = self.tabs[1]
                    uploaddocumenttab.click()
                    self.getAPIUrl(flag="downloadapi")
                    self.setFlag("downloadapi")
                    # Upload Documents Tab Process Finish
                    self.uploaddocuments(uploaddocumenttab)
                    biddingformtab = self.tabs[2]
                    biddingformtab.click()
                    self.page.wait_for_timeout(1000)
                    # Bidding Form Tab Process Finish
                    self.biddingform()
                else:
                    data = self.apiDATA.body()
                    data = self.convertBytestoJson(data)
                    self.errors.append(data)
                    continue
            writeCsvJson(self.filteredBidsData,
                         self.bidcsvpath+"\demoBidinfo.csv")
        except Exception as err:
            writeJsonFile({"errors": self.errors},
                          self.bidcsvpath+"\demoBiderrors.json")