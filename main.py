from features.container import Container

"""
            -----
           |  A  |
            -----
            /   \
        -----   -----
       |  B  | |  C  |
        -----   ----- 
          \      /
            -----
           |  D  |
            -----
     Multiple inheritance
"""


print("Please give user input 1 For Admin")
print("Please give user input 2 For Bidder")
print("Please give user input 3 For Officer")
userflag = input("Please give input :- ")

testProcuregenie = Container(userflag)
with testProcuregenie.sync_playwright() as p:
    testProcuregenie.setPlayWrightPage(p)
    testProcuregenie.buildenv()
    testProcuregenie.container()
