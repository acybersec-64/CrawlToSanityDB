import os
import re
import sys

if(len(sys.argv)<2):
    print("""\n\n  USAGE : python download_codes.py cookie  \n
    cookie ==> give the cookie between quotations like 'cookie'
    """)
    sys.exit()


with open(r"../codes.txt","r") as codes:
    allCodes = codes.read().split("\n")



def page_per_page(current_code):

    # fetch the login page
    os.system('node downloadPages.js {} "{}"'.format(current_code,sys.argv[1]))

for i in range(len(allCodes)):
    current_code = str(allCodes[i])
    
    page_per_page(current_code)
    


print("""\ndone!They saved in all_pages directory\n\n   tip: now you can run occupation.py or unitgroup.py""")
