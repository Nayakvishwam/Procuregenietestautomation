from features.bid import createBid
from features.login.login import TestLogin


class Container(TestLogin, createBid):
    def __init__(self, userFlag):
        super().__init__(userFlag)

    def container(self):
        self.testLogin()
        getrole = self.roles.get(self.userflag)
        if (getrole == "Admin"
                or getrole == "Officer"
            ):
            self.newBid()
        elif getrole == "Bidder":
            pass
