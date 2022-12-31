import os
import re
import sys

if(len(sys.argv)<1):
    print("""  USAGE : python download_codes.py (replace or missing) cookie save 
    cookie ==> give the cookie between 'cookie'
    """)
    sys.exit()


with open(r"../all_pages/codes","r") as codes:
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
    
        
        # except:
        #     continue
        

print("""done !tip: now run occupation.py/unitgroup.py""")
