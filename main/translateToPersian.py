import io
import re
from python_translator import Translator
import os

translator = Translator()

class Translate(object):

    def __init__(self) -> None:
                
        with io.open(r"../output/test_occupation24.ndjson","r",encoding='utf8') as r :
            self.english_words = r.read()
        # print(self.english_words)
        self.alternative_title_target = re.findall(r'''"alternative_title": {"en": \[(".*?")\]}''',self.english_words)
        self.NecOccupation_title_target = re.findall(r'"nec_occupation":{"en":\[(.*?)\]},"alternative_title',self.english_words)
        with open("test","w") as w:
            w.write(str(self.NecOccupation_title_target))
        self.Specialisations = re.findall(r'''"specialisations": {"en": \["(.*?)"\]}''',self.english_words)
        self.Desctiption_target = re.findall(r'"description": {"en": "(.*?)"} , "priority_list"',self.english_words)
        self.Title = re.findall(r'"title":{"en":"(.*?) "},"visa_option_section',self.english_words)
         

        
        if os.path.exists("test_occupation24_persian.ndjson"):
            os.remove(r"../output/test_occupation24_persian.ndjson")

           
        if os.path.exists(r"../output/translated.txt"):
            os.remove(r"../output/translated.txt")


    def alterNativ(self):
        print("alternatives")
        if os.path.exists(r"../output/translated.txt"):
            os.remove(r"../output/translated.txt")
        times = 4
        flenght =  (len(self.alternative_title_target))
        devideTO20 = flenght/times
        if(isinstance(devideTO20,float) == True):
            devideTO20 = int(devideTO20)+1
        
        run = True

        for i in range(times and run == True):
            
            for j in range(devideTO20):
                    
                    j = j + (i * devideTO20)        
                    
                    
                    if (j == self.alternative_title_target[-1]):
                        self.translate(self.alternative_title_target[-1])
                        run = False
                    else:
                        self.translate(self.alternative_title_target[j])
        with io.open(r"../output/translated.txt","r",encoding='utf8') as f:
            persian_alter = f.read()
        persian_alter = persian_alter.split('\n')
       
        for i in range(len(persian_alter)):

            
            this = '"alternative_title": {{"en": [{}]}}'.format(self.alternative_title_target[i])
            
            toThis = '"alternative_title": {{"en": [{}] , "fa": [{}]}}'.format(self.alternative_title_target[i],persian_alter[i])
                        
            self.english_words = self.english_words.replace(this,toThis)
        print("alternatives end")   
            # print("stored {} as translated {}".format(persian_alter[i],self.alternative_title_target[i]))
            

    def necOccupation(self):
        print("necOccupation")
        if os.path.exists(r"../output/translated.txt"):
            os.remove(r"../output/translated.txt")
        times  = 20
        flenght =  (len(self.NecOccupation_title_target))
        devideTO20 = flenght/times
        if(isinstance(devideTO20,float) == True):
            devideTO20 = int(devideTO20)+1
        
        run = True

        for i in range( times and run == True):
            
            for j in range(devideTO20):
                    
                    j = j + (i * devideTO20)        
                    
                    
                    if (j == self.NecOccupation_title_target[-1]):
                        self.translate(self.NecOccupation_title_target[-1])
                        run = False
                    else:
                        self.translate(self.NecOccupation_title_target[j])

        with io.open(r"../output/translated.txt","r",encoding='utf8') as f:
            persian_nec  = f.read()    

        persian_nec = (persian_nec.replace("«",'"')).replace("»",'"').replace("،",",")

        persian_nec = persian_nec.split('\n')
        
        
        for i in range(len(persian_nec)):
            
            this = '"nec_occupation":{{"en":[{}]}}'.format(self.NecOccupation_title_target[i])
            
            toThis = '''"nec_occupation" : {{"en": [{}] , "fa": [{}]}}'''.format(self.NecOccupation_title_target[i],persian_nec[i])
                        
            self.english_words = self.english_words.replace(this,toThis)
            
            # print("stored {} as translated {}".format(persian_nec[i],self.NecOccupation_title_target[i]))
        print("necOccupation ends")    

    def DescriptionTranslate(self):
        print("Description")
        if os.path.exists(r"../output/translated.txt"):
            os.remove(r"../output/translated.txt")
        times  = 20
        flenght =  (len(self.Desctiption_target))
        devideTO20 = flenght/times
        if(isinstance(devideTO20,float) == True):
            devideTO20 = int(devideTO20)+1
        

            
        run = True

        for i in range( times and run == True):
            
            for j in range(devideTO20):
                    
                    j = j + (i * devideTO20)        
                    
                    
                    if (j == self.Desctiption_target[-1]):
                        self.translate(self.Desctiption_target[-1])
                        run = False
                    else:
                        self.translate(self.Desctiption_target[j])

        with io.open(r"../output/translated.txt","r",encoding='utf8') as f:
            persian_Description  = f.read()    

        persian_Description = persian_Description.split('\n')

        for i in range(len(persian_Description)):
            
            this = '"description": {{"en": "{}"}}'.format(self.Desctiption_target[i])
            
            toThis = '''"description": {{"en": "{}" , "fa": [{}]}}'''.format(self.Desctiption_target[i],persian_Description[i])
                        
            self.english_words = self.english_words.replace(this,toThis)
            
            # print("stored {} as translated {}".format(persian_Description[i],self.Desctiption_target[i]))
        
        print("Description ends")
            
            # print(toThis)

    def SpecialisationsTranslate(self):
        print("SpecialisationsTranslate")
        if os.path.exists(r"../output/translated.txt"):
            os.remove(r"../output/translated.txt")
        times = 4
        flenght =  (len(self.Specialisations))
        devideTO20 = flenght/times
        if(isinstance(devideTO20,float) == True):
            devideTO20 = int(devideTO20)+1
        
        run = True

        for i in range(times and run == True):
            
            for j in range(devideTO20):
                    
                    j = j + (i * devideTO20)        
                    
                    
                    if (j == self.Specialisations[-1]):
                        print(self.Specialisations[-1])
                        self.translate(self.Specialisations[-1])
                        run = False
                    else:
                        self.translate(self.Specialisations[j])
        with io.open(r"../output/translated.txt","r",encoding='utf8') as f:
            persian_special = f.read()
        persian_special = persian_special.split('\n')


        for i in range(len(persian_special)):

            
            this = '"specialisations": {{"en": ["{}"]}}'.format(self.Specialisations[i])
            
            toThis = '"specialisations": {{"en": ["{}"] , "fa": [{}]}}'.format(self.Specialisations[i],persian_special[i])
                        
            self.english_words = self.english_words.replace(this,toThis)
            
            print("stored {} as translated {}".format(persian_special[i],self.Specialisations[i]))

            
            # print(toThis)
        print("SpecialisationsTranslate ends")

    def translate(self,SourceWord):
        
        while(True):
            os.system("color 0a")
            try:        
                print("translatin")
                
                SourceWord = SourceWord.replace('"',"").replace("«",'"').replace("»",'"')
                SourceWord = SourceWord.split(',')
                newSourceWord = []
                for i in range(len(SourceWord)):
                    
                    if i == len(SourceWord):
                        newSourceWord.append('"{}"'.format(SourceWord[i]))    
                        break
                    newSourceWord.append('"{}",'.format(SourceWord[i]))
               
                newSourceWord = "".join(newSourceWord)

                TranslatedWord = '{}'.format(str((translator.translate(newSourceWord,"fa","english"))))
            
                print("translated from {} to {}".format(newSourceWord,TranslatedWord))

                with io.open(r"../output/translated.txt","a",encoding='utf8') as title:
                    title.write(TranslatedWord+"\n")
                break
            except Exception(KeyboardInterrupt):
                print("getting error in requesting")
                os.system("cls")
                break

    
    def TitleTrans(self):
        print("titles are started")
        if os.path.exists(r"../output/translated.txt"):
            os.remove(r"../output/translated.txt")
        times = 4
        flenght =  (len(self.Title))
        devideTO20 = flenght/times
        if(isinstance(devideTO20,float) == True):
            devideTO20 = int(devideTO20)+1
        
        run = True
        for i in range(times and run == True):
            
            for j in range(devideTO20):
                    
                    j = j + (i * devideTO20)        
                    
                    
                    if (j == self.Title[-1]):
                        self.translate(self.Title[-1])
                        run = False
                    else:
                        self.translate(self.Title[j])

        with io.open(r"../output/translated.txt","r",encoding='utf8') as f:
            persian_Title = f.read()

        persian_Title = persian_Title.split('\n')
        for i in range(len(persian_Title)):
            
            this = '"title":{{"en":"{} "}}'.format(self.Title[i])

            toThis = '"title": {{"en": "{}" , "fa": [{}]}}'.format(self.Title[i],persian_Title[i])

            self.english_words = self.english_words.replace(this,toThis)
        print("ends")                



    def run(self):
        os.system("color 0d")
        self.DescriptionTranslate()     
        self.TitleTrans()
        self.alterNativ()
        self.SpecialisationsTranslate()
        self.necOccupation()
        self.english_words = self.english_words.replace('«','"').replace('»','"').replace('،',',')
        with io.open(r"../output/test_occupation24_persian.ndjson","w",encoding='utf8') as f:
            f.write(self.english_words)

program = Translate()

program.run()