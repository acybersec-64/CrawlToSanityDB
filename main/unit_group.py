import hashlib
import re
import os
import threading
from slugify import slugify
from python_translator import Translator


class translate(object):
    
    def to_persian(self,english):

        translator = Translator()
        if(isinstance(english,str)):
            persian = translator.translate("{}".format(english), "persian", "english")
            return persian
        if(isinstance(english,list)):
            persian_word = []
            for i in range(len(english)):
                
                persian_word.append(translator.translate("'{}'".format(english[i]), "persian", "english"))
            
            return persian_word
        
       

class leak_unit_group(object):
    
    def __init__(self):
        with open("codes","r") as codes:
            all_codes = codes.read()
        all_codes = all_codes.replace('"', '')
        self.regx_find_codes = re.findall("<a href=https://www.anzscosearch.com/(.+?) title", all_codes)

        self.unit_groups_without_duplicates = []

    def page_per_page(self):
        

        
        with open("{}".format(self.current_code),"r") as page:
            raw_page = str(page.read())
        self.no_qout_page = ((raw_page.replace('"','')).replace("'","")).replace("\\","")
        

       
       
        self.skill_level = self.Skill_level_func()


        self.unit_group_code = self.current_code[0:4]             
        
        
        self.export_new_unit_groups()



    def Title(self):
        
        title = re.findall("margin:30px 0px; border: 1px solid #525252; padding:10px 0px; text-align:center; border-radius:5px; color: #000000;><b>(.*?)</b>",self.no_qout_page)
        
        title = (title[0]).split(":") 
        self.title = list(title[1])
        del self.title[0]
        out_str = ""
        self.title = (out_str.join(self.title))
        return self.title       


    #   possible visa option should add 
        
    def Skill_level_func(self):

        
        self.skill_level = re.findall("font-size:15px; background-color: #0068ea; color: white; padding: 2px 7px; border-radius: 25px;>(.*?)</span></p>",self.no_qout_page)
        
        self.skill_level = (((str(self.skill_level[0])).replace(")","")).replace(".","")).replace(" ","")
        
        return self.skill_level
    # get all html from #tab-tab3 page



    
        
    def Description(self):
        self.description = re.findall("padding: 20px; background-color: #e8e8e8; color: #2d2d2d; margin: 30px 0px; border-radius:5px;>(.*?)</p>",self.no_qout_page)

        return self.description[0]

    def Task(self):

            #<ul style='padding-top:10px; padding-bottom:10px;' class='padding20'><li>
            alltask = re.findall("<ul style=padding-top:10px; padding-bottom:10px; class=padding20>(<li>.*?)</ul> ",self.no_qout_page)
            self.tasklist = re.findall("<li>(.*?)</li>",alltask[0])
            # if there is no task :
            for each in self.tasklist:
                no_task = re.search("<a",each)
                if (no_task):
                    self.task = re.findall("margin-top:15px; margin-bottom:5px; text-align:center;><i>(.*?)</i></p>",self.no_qout_page)
                    self.task = ['']
                    
                    return self.task
                    
                else:
                    return self.tasklist



    def export_new_unit_groups(self):

        self.description = self.Description()
        self.task = self.Task()
        self.title = self.Title()
        if(self.unit_group_code in self.unit_groups_without_duplicates):
            pass
        
        else:
            self.unit_groups_without_duplicates.append(self.unit_group_code)
            result = hashlib.md5(self.unit_group_code.encode('utf-8'))
            hash_value = result.hexdigest()
            slug = slugify(self.title)

            ndjson_sanity = ('''{{"_createdAt":"2022-11-13T13:09:36Z","_id":"{}","_rev":"dy074TCuBZeOysjuEOARqm","_type":"unit_group","_updatedAt":"2022-11-13T13:40:32Z","code":{},"description":{{"en":"{}"}},"skill_level":"{}","tasks":{{"en":{}}},"title":{{"en":"{}"}},"slug": {{"_type": "slug","current": "{}"}}}}'''.format(hash_value,self.unit_group_code,self.description,self.skill_level,self.task,self.title,slug)).replace("'",'"')
            
            with open("unitgroup.ndjson","a") as write:
                write.write(ndjson_sanity+"\n")



    def loop_over(self) :
        for i in range(len(self.regx_find_codes)):
           
            
            self.current_code = str(self.regx_find_codes[i])

            threads= list()   
            x = threading.Thread(target=self.page_per_page(), args=(1))
            threads.append(x)
            x.start()    
if os.path.exists("unitgroup.ndjson"):
        os.remove("unitgroup.ndjson")

unit_group = leak_unit_group()
unit_group.loop_over()

