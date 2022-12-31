import os
import re


def CrawlCodes():
    # fetch the list occupation
    os.system('node downloadCodes.js')
	

    with open(r"../codes.html","r") as codes:
        all_codes = codes.read()
        all_codes = all_codes.replace("\n","")
        regxBetweenTags = re.findall(r'<div style="overflow-x:auto;">(.*?)<div  class="vc_col-sm-3 wpb_column', all_codes)
        regx_find_codes = re.findall("<a href=https://www.anzscosearch.com/(.*?) title", "".join(regxBetweenTags))
        regx_find_codes.sort()
        print("\n {} Codes has been Downloaded!".format(str(len(regx_find_codes))))
        with open("../codes.txt","w") as WCodes:
            WCodes.write("\n".join(regx_find_codes))

CrawlCodes()
os.remove(r"../codes.html")
print("""\ndone!They saved in in codes.txt\n\n   tip: now you can run downloadPages.py""")
