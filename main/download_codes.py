import os
import re
import sys

if(len(sys.argv)<2):
    print("""\n\n  USAGE : python download_codes.py cookie  \n
    cookie ==> give the cookie between quotations like 'cookie'
    """)
    sys.exit()


with open(r"../codes.html","r") as codes:
    all_codes = codes.read()
    all_codes = all_codes.replace('"', '')
    regx_find_codes = re.findall("<a href=https://www.anzscosearch.com/(.*?) title", all_codes)
    regx_find_codes.sort()

def page_per_page(current_code):

    # fetch the login page
    os.system('node download.js {} "{}"'.format(current_code,sys.argv[1]))

for i in range(len(regx_find_codes)):
    current_code = str(regx_find_codes[i])
    
    page_per_page(current_code)
    


print("""\ndone!They saved in all_pages directory\n\n   tip: now you can run occupation.py or unitgroup.py""")
