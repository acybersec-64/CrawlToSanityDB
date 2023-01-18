import string
import random
import os
try:
    import hashlib
except:
    os.system("pip install hashlib")
try:
    from slugify import slugify
except:
    os.system("pip install slugify")
import re
import threading
import io

class beutifull(object):
    def beuty_text(self,ugly_text):
        buty = (((str(ugly_text).replace("'","")).replace("\\","")).replace("[","")).replace("]","")
        return buty

class anzco(object):
 

    def __init__(self):
        with open(r"../codes.txt","r") as codes:
            self.allCodes = codes.read().split("\n")
            
        self.occupation_without_duplicates = []
        global lsc_list
        lsc_list = []
        self.state_territory = []

    def Title(self):
        
        title = re.findall('<title>ANZSCO {}: (.*?) Australia Visa options</title>'.format(current_code),no_qout_page)
        self.title = title[0].replace("|","")
          

        return self.title

    def Alternative_title(self):
    
        self.alternative_title =  re.findall("Alternative Titles -->(.*?)<!-- Specialisations",no_qout_page)
        isThereALternatives = re.search("There are no",str(self.alternative_title))
        if isThereALternatives != None:
            return []
        
        else:
            print(current_code)
            self.alternative_title = re.findall("<ul style=padding-top:10px; class=padding20>(.*?)</ul>",(self.alternative_title[0]))
            self.alternative_title = re.findall("<li>(.*?)</li>",(self.alternative_title[0]))
            return(self.alternative_title)
        

    def Specialisations(self):
        
        self.specialisations = re.findall("<!-- Specialisations -->(.*)<!-- Occupation in NEC category -->",no_qout_page)
        self.specialisations = re.findall("<ul style=padding-top:10px; class=padding20>(.*?)</ul>",self.specialisations[0])
        self.specialisations = re.findall("<li>(.*?)</li>",str(self.specialisations))
        
        if (len(self.specialisations) == 0 or self.specialisations[0] == ""):
            
            return []
        else:
            return(self.specialisations)

    def Description(self):
        self.description = re.findall("padding: 20px; background-color: #e8e8e8; color: #2d2d2d; margin: 30px 0px; border-radius:5px;>(.*?)</p>",no_qout_page)

        return self.description[0]

    def nec(self):
        
        if_title_found_nec = re.findall('<title>ANZSCO {}:(.*?) Australia Visa options</title>'.format(current_code),no_qout_page)
        if_title_found_nec = re.findall('(.*?nec)',(if_title_found_nec[0]).replace('|',""))
        nec_all_list = []
        if (len(if_title_found_nec)!=0):
           
           
            between_nec_tag = re.findall('<!-- Occupation in NEC category -->(.*?)<!-- Skills Priority List -->',no_qout_page)
            self.nec_all = re.findall('<li>(.*?)</li>',between_nec_tag[0])
            
            
            for i in range(len(self.nec_all)):
                nec_all_list.append('"{}"'.format(self.nec_all[i]))
            
            
            self.nec_each = (''',"nec_occupation":{{"en":{}}}'''.format(nec_all_list)).replace("'",'')
            return self.nec_each
        else:
            return ''',"nec_occupation":{"en":['']}'''

    def Skills_Priority(self):

        skills = re.findall("<table style=margin-left:20px !important;margin-top:20px;margin-bottom:0px; width: 95%; class=dataTable>(.*?style=padding-top:10px; class=padding20>)",no_qout_page)
        
        if (len(skills)== 0):
            skills_Priority = ''
            skills_Priority = ('''"ACT": "{}","future_demend": "{}","national": "{}","NSW": "{}","NT": "{}","QLD": "{}","SA": "{}","TAS": "{}","VIC": "{}","WA": "{}"'''.format(skills_Priority,skills_Priority,skills_Priority,skills_Priority,skills_Priority,skills_Priority,skills_Priority,skills_Priority,skills_Priority,skills_Priority)) 
            return skills_Priority
        else:
            skills_Priority = re.findall("<td>(.*?)</td>",skills[0])
            skills_Priority = ('''"ACT": "{}","future_demend": "{}","national": "{}","NSW": "{}","NT": "{}","QLD": "{}","SA": "{}","TAS": "{}","VIC": "{}","WA": "{}"'''.format(skills_Priority[1],skills_Priority[-1],skills_Priority[0],skills_Priority[2],skills_Priority[3],skills_Priority[4],skills_Priority[5],skills_Priority[6],skills_Priority[7],skills_Priority[8]))
            return skills_Priority

    def assesin_auth(self):
        between_tag = re.findall('<div id=print_result>(.*?)<!-- Tabs Start -->',no_qout_page)
        each_in_assesin = re.findall('font-size:12px;color:#333333;font-weight:300; target=_blank href=(.*?<)/a>',between_tag[0])
        each_in_assesin = re.findall('>(.*?)<',str(each_in_assesin))
        each_assesin_group = re.findall('font-size:14px; color:red;(.*?<)/a>',between_tag[0])
        if (len(each_assesin_group)):
            each_assesin_group = re.findall('>(.*?)<',each_assesin_group[0])
            each_assesin_group = each_assesin_group[0].replace("Group ","")
            each_in_assesin[0] = ("{}_{}".format(each_in_assesin[0],each_assesin_group[0]))
            
        return each_in_assesin[0]
    


    def backlog(self):
        

        
        sub_189 = self.eoi_sub_class_189_491f('189')
        sub_491f = self.eoi_sub_class_189_491f('491f')

        eoi_sub_class_190_491 = self.eoi_sub_class_190_491() 
        sub_190 = eoi_sub_class_190_491.export('190')
        sub_491 = eoi_sub_class_190_491.export('491')

        back_log_ndjason = ('''"backlog_section": {{"_type": "backlog_obj"{} {} {} {}}}'''.format(sub_189,sub_190,sub_491,sub_491f))
        return back_log_ndjason
    
    def visa_type(self,lsc):
        global visa_option   
        global visa_types
        visa_option = ""
        visa_types = []
        lsc_list.append(lsc)
        list_lsc = list(set(lsc_list ))


        for i in range(len(list_lsc)):
            result = hashlib.md5(list_lsc[i].encode('utf-8'))
            visa = result.hexdigest()       
            # print("      " +visa + "      " + lsc)
            visa_types.append('''{{  "_key": "19e0a90e189a",  "_type": "visa_option_obj",  "types": {{    "_ref": "{}",    "_type": "reference"}}}}'''.format(visa))

        visa_types = ((str(visa_types).replace("[","")).replace("]","")).replace("'","")
        visa_option = ('''"visa_option_section": [{}]''').format(visa_types)
        
    def randomKeyObjsGen(self):
           
            characterList = ""
            keyGenerated = []

            for i in range(12):

                characterList += string.ascii_letters
                characterList += string.digits

                # Picking a random character from our
                # character list
                
                randomchar = random.choice(characterList)
                
                # appending a random character to password
                keyGenerated.append(randomchar)
            
            return "".join(keyGenerated)



    def territory(self, state):
            global states
            StateEligibity = self.HtmlTabs()
         
            for i in range(len(state)):
                self.state_territory.append('''"territory":{{"_ref":"{}","_type":"reference"}}'''.format(state[i]))
            self.state_territory = list(set(self.state_territory))
            states_ter = ((str(self.state_territory).replace("[","")).replace("]","")).replace("'","")
 
            act = StateEligibity.act()
            nsw = StateEligibity.nsw()
            nt = StateEligibity.nt()
            qld = StateEligibity.qld()
            sa = StateEligibity.sa()
            tas = StateEligibity.tas()
            vic = StateEligibity.vic()
            wa = StateEligibity.wa()
 
                
            keyRandAct = self.randomKeyObjsGen()
            keyRandNsw = self.randomKeyObjsGen()
            keyRandNt = self.randomKeyObjsGen()
            keyRandQld = self.randomKeyObjsGen()
            keyRandSa = self.randomKeyObjsGen()
            keyRandTas = self.randomKeyObjsGen()
            keyRandVic = self.randomKeyObjsGen()
            keyRandWa  = self.randomKeyObjsGen()

            actRef = "90d991b47098ceef3d8283a386cf7e91"
            nswRef = "7fd51c89695b098a88a38f57ae4bfb2d"
            ntRef = "cb48af3e40ab9ec3622c07b8faf27cf3"
            qldRef = "c6f45fe1ff59e2232e252c632252c728"
            saRef = "3dd6b9265ff18f31dc30df59304b0ca7"
            tasRef = "f4e1b83458954d7218793cee79be80b0"
            vicRef = "d48afc599a256e036954100b5cfbe360"
            waRef = "4306a04670067b5b27e766335d3d40fa"

            
            actSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}},'''.format(keyRandAct,act,actRef)
            nswSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}},'''.format(keyRandNsw,nsw,nswRef)
            ntSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}},'''.format(keyRandNt,nt,ntRef)
            qldtSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}},'''.format(keyRandQld,qld,qldRef)
            saSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}},'''.format(keyRandSa,sa,saRef)
            tastSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}},'''.format(keyRandTas,tas,tasRef)
            vicSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}},'''.format(keyRandVic,vic,vicRef)
            waSection  = '''{{"_key": "{}","_type": "territory_obj","html_desc": "{}","territory": {{"_ref": "{}","_type": "reference"}}}}'''.format(keyRandWa,wa,waRef)

            states = ('''"territory_section": [{}{}{}{}{}{}{}{}] '''.format(actSection,nswSection,ntSection,qldtSection,saSection,tastSection,vicSection,waSection))
    class HtmlTabs(object):

        def __init__(self) -> None:
            self.allTabs = re.findall('<!-- TAB 3: STATE ELIGIBILITY DETAILS -->(.*?)<!-- TAB 4: ANZSCO CODE -->',qout_page)
            afterEquelHasQoute = re.findall("(=.+\s)",qout_page)
            # print(afterEquelHasQoute)

        def act(self):
            actTab = re.findall("(<div id='tabs-act'>.*?)<div id='tabs-nsw'>",str(self.allTabs))            
            actTab = (actTab[0]).replace('[','').replace(']','')
            #print(actTab)
            return actTab
      
        def nsw(self):
            nswTab = re.findall("(<div id='tabs-nsw'>.*?)<div id='tabs-nt'>",str(self.allTabs))
            nswTab = (nswTab[0]).replace('[','').replace(']','')
            return nswTab
        
        def nt(self):
            ntTab = re.findall("(<div id='tabs-nt'>.*?)<div id='tabs-qld'>",str(self.allTabs))
            ntTab = (ntTab[0]).replace('[','').replace(']','')
            return ntTab

        def qld(self):
            qldTab = re.findall("(<div id='tabs-qld'>.*?)<div id='tabs-sa'>",str(self.allTabs))
            qldTab = (qldTab[0]).replace('[','').replace(']','')
            return qldTab

        def sa(self):
            saTab = re.findall("(<div id='tabs-sa'>.*?)<div id='tabs-tas'>",str(self.allTabs))
            saTab = (saTab[0]).replace('[','').replace(']','')
            return saTab

        def tas(self):
            tasTab = re.findall("(<div id='tabs-tas'>.*?)<div id='tabs-vic'>",str(self.allTabs))
            tasTab = (tasTab[0]).replace('[','').replace(']','')
            return tasTab

        def vic(self):
            vicTab = re.findall("(<div id='tabs-vic'>.*?)<div id='tabs-wa'>",str(self.allTabs))
            vicTab = (vicTab[0]).replace('[','').replace(']','')
            return vicTab

        def wa(self):
            waTab = re.findall("(<div id='tabs-wa'>.*?)<div id='tabs-allocations'>",str(self.allTabs))
            waTab = (waTab[0]).replace('[',"").replace(']',"")
            return waTab



#   ///////////////////////////     visa sub class 190 - 491 submitted and invited  //////////////////

    class eoi_sub_class_190_491(object): 
        
        def __init__(self):
            self.points_visa_subclass_subs = []
            self.points_visa_subclass_inv = []
            self.submitted_by_state = []
            self.invited_by_state = []
            self.total_eoi_count_subs = []
            self.eoi_count_inv = []
            self.state = []
            self.anz = anzco()
            

            self.between_backlog_tag = re.findall('<!-- TAB 5: BACKLOG -->(.*?)<!-- TAB 6: DAMA -->',no_qout_page)
            
           #____________________________________ACT______________________________NSW_________________________________NT______________________________QLD_______________________________________SA_______________________________TAS______________________________VIC______________________________________WA____________
            self.territories = ["90d991b47098ceef3d8283a386cf7e91","7fd51c89695b098a88a38f57ae4bfb2d","cb48af3e40ab9ec3622c07b8faf27cf3","c6f45fe1ff59e2232e252c632252c728","3dd6b9265ff18f31dc30df59304b0ca7","f4e1b83458954d7218793cee79be80b0","d48afc599a256e036954100b5cfbe360","4306a04670067b5b27e766335d3d40fa"]
            
        #   ///////////////////////////      submitted section in 190 - 491       //////////////////////////////
 
        def submitteds(self,lsc):
            self.state = []
            self.points_visa_subclass_subs = []
            self.submitted_by_state = []
            # to get eoi submitted
            backlog_eoi_data_sub = re.findall('''eoi{}_sub(.*?)eoi{}_inv'''.format(lsc,lsc),self.between_backlog_tag[0])
            is_ther_data = re.search('''No EOI data''',str(backlog_eoi_data_sub))
            if(is_ther_data == None):
               
                backlog_eoi_data_points_subs = re.findall('''EOI Count(.*?)by State''',
                str(backlog_eoi_data_sub))
                # ////////////////////////////////   points  sub ////////////////////////////////////// 
                for i in backlog_eoi_data_points_subs:
                    
                    which_points = re.findall(''';>(.*?)</td><td>''',i)
                    how_many_points = re.findall('''</td><td>(.*?)</td>''',i)
                
                    for j in range(len(which_points[:])):
                        
                        self.points_visa_subclass_subs.append(( ('''"upper_than_{}": "{}"'''.format(which_points[j],how_many_points[j]))))
                        
                        
                # -/////////////////////////////////// submitteds sub /////////////////////////////////////
                backlog_eoi_data_submitted_subs = re.findall('''by State(.*?</td></tr></table></div>)''',
                str(backlog_eoi_data_sub))
                for i in backlog_eoi_data_submitted_subs:
                    
                    which_state = re.findall(''';>(.*?)</td><td>''',i)

                    how_many_state = re.findall('''</td><td>(.*?)</td>''',i)
                    if("ANY" in which_state):
                        which_state.remove("ANY")                    


                    for j in range(len(which_state)):
                        result = hashlib.md5(which_state[j].encode('utf-8'))
                        self.which_state = result.hexdigest()  
                        for k in range(len(self.territories)):
                            if (self.which_state == self.territories[k]):
                                self.state.append(self.which_state)
                        if (len(self.state)):
                            self.anz.territory(self.state)
                        else:
                            self.anz.territory("")
                        #   todo    = refrence state in by state section to territorys
                        self.submitted_by_state.append(( ('''{{ "_key": "d3ec69780689","_type": "territory_backlog_obj","eoi_count": "{}","territory": {{"_ref": "{}","_type": "reference"}}}}'''.format(how_many_state[j],self.state[j]))))
                        
                
                                # //////////////////////////    export  subs    ///////////////////////////////////
               
                if (len(self.points_visa_subclass_subs)):
                    points_visa_subclass_subs = (str(self.points_visa_subclass_subs).replace("[","")).replace("]","")
                    submitted_by_state = (str(self.submitted_by_state).replace("[","")).replace("]","")
                    submitted_by_state = (''',"submited_by_state_{}": [{}]'''.format(lsc,submitted_by_state))


                    self.backlog_export_subs = ((('''{},"submited_{}": {{"_type": "backlog_numbers_obj",{}}} '''.format(submitted_by_state,lsc,points_visa_subclass_subs,)).replace("'","")).replace("\\",""))

                    self.anz.visa_type(lsc)
                else:
                    self.backlog_export_subs = (''',"submited_{}" : {{"_type": "backlog_numbers_obj"}}'''.format(lsc,self.eoi_count_inv))
            else:
                self.backlog_export_subs =  ""

            return self.backlog_export_subs       
        
        #   ///////////////////////////      invited section in 190 - 491       //////////////////////////////
        
        def inviteds(self,lsc):
            self.state = []
            self.points_visa_subclass_inv = []
            self.invited_by_state = []
            backlog_eoi_data_inv = re.findall('''eoi{}_inv(.*?)SUBMITTED'''.format(lsc),self.between_backlog_tag[0])
            
            is_ther_data = re.search('''No EOI data''',str(backlog_eoi_data_inv))
            if(is_ther_data == None):
               

               
                backlog_eoi_data_points_inv = re.findall('''EOI Count(.*?)by State''',
                str(backlog_eoi_data_inv))
                
                for i in backlog_eoi_data_points_inv:
                    
                    which_points = re.findall(''';>(.*?)</td><td>''',i)
                    how_many_points = re.findall('''</td><td>(.*?)</td>''',i)
                    
                    for j in range(len(which_points[:])):
            
                        self.points_visa_subclass_inv.append(( ('''"upper_than_{}": "{}"'''.format(which_points[j],how_many_points[j]))))
                        
              
               
                backlog_eoi_data_submitted_inv = re.findall('''by State(.*?</td></tr></table></div>)''',
                str(backlog_eoi_data_inv))
                
                for i in backlog_eoi_data_submitted_inv:
                    
                    which_state = re.findall(''';>(.*?)</td><td>''',i)
                    how_many_state = re.findall('''</td><td>(.*?)</td>''',i)
          
                    if("ANY" in which_state):
                        which_state.remove("ANY")

                    for j in range(len(which_state)):
                        result = hashlib.md5(which_state[j].encode('utf-8'))
                        self.which_state = result.hexdigest()  
                        
                        for k in range(len(self.territories)):
                            if (self.which_state == self.territories[k]):
                                self.state.append(self.which_state)

                        
                        if (len(self.state)):
                            self.anz.territory(self.state)
                        

                                    
                        else:
                            self.anz.territory("")
                     
                            # todo refrence state to territories
                        self.invited_by_state.append(( ('''{{ "_key": "d3ec69780689","_type": "territory_backlog_obj","eoi_count": "{}","territory": {{"_ref": "{}","_type": "reference"}}}}'''.format(how_many_state[j],self.state[j]))))
                         
                                # //////////////////////////    export  subs    ///////////////////////////////////
                
                if (len(self.points_visa_subclass_subs)):
                    
                    points_visa_subclass_inv = (str(self.points_visa_subclass_inv).replace("[","")).replace("]","")
                    invited_by_state = (str(self.invited_by_state).replace("[","")).replace("]","")
                    invited_by_state = (''',"invited_by_state_{}": [{}]'''.format(lsc,invited_by_state))

                    self.backlog_export_inv = ((('''{},"invited_{}": {{"_type": "backlog_numbers_obj",{}}} '''.format(invited_by_state,lsc,points_visa_subclass_inv)).replace("'","")).replace("\\",""))
             

                    
                    self.anz.visa_type(lsc)
                else:
                    self.backlog_export_inv = (''',"invited_{}": {{"_type": "backlog_numbers_obj"}}'''.format(lsc))
            else:
                self.backlog_export_inv =  ""

            return self.backlog_export_inv  
        
        def export(self,lsc):
            self.backlog_eoi_data = re.findall('''eoi{}_sub(.*?)eoi{}_inv'''.format(lsc,lsc),self.between_backlog_tag[0])
            self.backlog_export_all = ('''{}{}'''.format(self.submitteds(lsc),self.inviteds(lsc)))
            return self.backlog_export_all
                                                       
#   ///////////////////////////     visa sub class 189 - 491 family submitted and invited  //////////////////
    def numbers(self,s):
        return [str(match) for match in re.findall(r"\d+", s)]

    def eoi_sub_class_189_491f(self,lsc):
        
        
            
            self.points_visa_subclass_subs = []
            self.points_visa_subclass_inv = []
            self.total_eoi_count_subs = []
            self.eoi_count_inv = []
            self.anz = anzco()
            self.lscIntOnly = "".join(self.numbers(lsc))
            if self.lscIntOnly == "491":
                self.lscIntOnly = self.lscIntOnly+"_family"
            between_backlog_tag = re.findall('<!-- TAB 5: BACKLOG -->(.*?)<!-- TAB 6: DAMA -->',no_qout_page)
            # to get eoi submitted
            backlog_eoi_data = re.findall('''eoi{}_sub(.*?)eoi{}_inv'''.format(lsc,lsc),between_backlog_tag[0])
            is_ther_data = re.search('''No EOI data''',str(backlog_eoi_data))
            if(is_ther_data == None):
               
                backlog_eoi_data_points_subs = re.findall('''EOI Count(.*?)table''',
                str(backlog_eoi_data))
                
                for i in backlog_eoi_data_points_subs:
                    
                    which_points = re.findall(''';>(.*?)</td><td>''',i)
                    how_many_points = re.findall('''</td><td>(.*?)</td>''',i)
                    which_points[-1] = which_points[-1].replace("TOTAL","")
   

                    for j in range(len(which_points)):
                            
                        self.points_visa_subclass_subs.append(( ('''"upper_than_{}": "{}"'''.format(which_points[j],how_many_points[j]))))

                # find total from eoi data in sub 
                is_ther_total = re.search('''TOTAL''',backlog_eoi_data_points_subs[-1])
                if (is_ther_total):
                    how_many_total_subs =  "".join(re.findall('''>TOTAL</td><td>(.*?)</td>''',backlog_eoi_data_points_subs[-1]))
                else:    
                    how_many_total_subs = ""
                
 

                if (len(self.points_visa_subclass_subs)):
                    self.points_visa_subclass_subs = ((str(self.points_visa_subclass_subs)).replace("[","")).replace("]","")
                    self.backlog_export_subs = (((''',"total_submited_{}": "{}","submited_{}": {{"_type": "backlog_numbers_obj",{}}}'''.format(self.lscIntOnly,how_many_total_subs,self.lscIntOnly,self.points_visa_subclass_subs)).replace("'","")).replace("\\",""))
                    self.anz.visa_type(lsc)

                else:
                    self.backlog_export_subs = (''',"total_submited_{}": "","submited_{}": {{"_type": "backlog_numbers_obj"}}'''.format(self.lscIntOnly,self.lscIntOnly,self.eoi_count_inv))
            else:
                self.backlog_export_subs =  ""





            # to get invited 
            backlog_eoi_data_inv = re.findall('''eoi{}_inv(.*?)SUBMITTED'''.format(lsc),between_backlog_tag[0])
            
            is_ther_data = re.search('''No EOI data''',str(backlog_eoi_data_inv))
            if(is_ther_data == None):
               
                backlog_eoi_data_points_inv = re.findall('''EOI Count(.*?)table''',
                str(backlog_eoi_data_inv))
                
                # find total from eoi data in inv
                is_ther_total = re.search('TOTAL',backlog_eoi_data_points_inv[-1])
                if (is_ther_total):
                    how_many_total_inv =  "".join(re.findall('''>TOTAL</td><td>(.*?)</td>''',backlog_eoi_data_points_inv[-1]))
                else:    
                    how_many_total_inv = ""
 
                
                for i in backlog_eoi_data_points_inv:
                    
                    which_points = re.findall(''';>(.*?)</td><td>''',i)
                    how_many_points = re.findall('''</td><td>(.*?)</td>''',i)
                    which_points[-1] = which_points[-1].replace("TOTAL","")

                    for j in range(len(which_points)):
            
                        self.points_visa_subclass_inv.append(( ('''"upper_than_{}": "{}"'''.format(which_points[j],how_many_points[j]))))
                if (len(self.points_visa_subclass_inv)):
                    self.points_visa_subclass_inv = ((str(self.points_visa_subclass_inv)).replace("[","")).replace("]","")
                    self.backlog_export_inv = ((''',"total_invited_{}": "{}","invited_{}": {{"_type": "backlog_numbers_obj",{}}}'''.format(self.lscIntOnly,how_many_total_inv,self.lscIntOnly,str(self.points_visa_subclass_inv))).replace("'","")).replace("\\","")
                    self.anz.visa_type(lsc)
                    

                else:
                    self.backlog_export_inv = (''',"total_invited_{}": "","invited_{}": {{"_type": "backlog_numbers_obj"}}'''.format(self.lscIntOnly,self.lscIntOnly,self.eoi_count_inv))
                

            else:
                self.backlog_export_inv=""        

            self.backlog_export_all = ('''{}{}'''.format(self.backlog_export_subs,self.backlog_export_inv))
            return self.backlog_export_all     
                
    def groups(self):
        between_groups_tag = re.findall('<!-- TAB 4: ANZSCO CODE -->(.*?)<!-- Alternative Titles -->',no_qout_page)
        groups_and_numbs = re.findall('<span style=display: inline-block;width:10em;>(<b>.*?)<b>',str(between_groups_tag))
        groups = re.findall('<b>(.*?)</b>',str(between_groups_tag))
        nums = re.findall('</span>(.*?)-',str(between_groups_tag))
        self.major_group = self.major_groups(nums)
        self.sub_major_group = self.sub_major_groups(nums)
        self.Minor_Group = self.Minor_Groups(nums)
        return  self.major_group,self.sub_major_group,self.Minor_Group

    def major_groups(self,nums):
        save_groups = []
        save_groups.append('"major_group"'+":"+nums[0])
        return save_groups[0]
  
    def sub_major_groups(self,nums):
        save_groups = []
        save_groups.append('"submajor_group"'+":"+nums[1])
        return save_groups[0]


    def Minor_Groups(self,nums):
        save_groups = []
        
        save_groups.append('"minor_group"'+":"+nums[2])
        return  save_groups[0]

    def occupation_anzco(self):
        

        
        global no_qout_page 
        global qout_page
        with io.open(r'../all_pages/{}.html'.format(current_code),'r',encoding='utf8') as r:
            page = r.read()
        page = page.replace('\xa0',"")
        qout_page = page
        qout_page = qout_page.replace('"',"'").replace('xe2x80x98','`').replace('xe2x80x99','`').replace("\n","").replace("\\","")
        no_qout_page = ((page.replace('"','')).replace("'","")).replace("\\","").replace("\n","")
        
        #for i in 
        self.export_occupation()        

    def export_occupation(self):    
        id = "occupation"+current_code
        result = hashlib.md5(id.encode('utf-8'))
        id = result.hexdigest()       
        
        skills_Priority = self.Skills_Priority()
        
        self.description = self.Description()
        self.title = self.Title()
        self.necs = self.nec()
        self.group = self.groups()
        self.backlogs = self.backlog()
        self.alternative_title = self.Alternative_title()
        self.assesin_authority = self.assesin_auth()
        self.specialisation = self.Specialisations()   
        # first 4 charakter of any current code converts to hash for refrences to unitgroup
        self.unit_group_code = current_code[0:4]
        result = hashlib.md5(self.unit_group_code.encode('utf-8'))
        self.unit_group_refrence = result.hexdigest()  
        slug = list(slugify(self.title))
        del slug[0]
        slug = "".join(slug)
        # print(slug)
        #                                                           id                                                                                                               self.group[0]          self.group[2]       self.group[1]         self.necs            self.alternatives    self.description                                                     skills_Priority                                     self.specialisation                      self.unit_group_refrence                                                                                                       self.assesin_authority   self.backlogs  current_code                        slug               self.title     visa_option
           

        allExport = ('"_createdAt": "2022-11-19T15:51:20Z","_id": "{}","_rev": "q0er4j-pxn-zhv-xak-oune525i0","_type": "occupation","_updatedAt": "2022-11-19T16:21:24Z","anzsco_section": {{"_type": "anzsco_obj", {} ,  {}, {}  {},"alternative_title": {{"en": {}}},"description": {{"en": "{}"}} , "priority_list": [{{"_key": "08e813a79592","_type": "priority_list_obj",{},"year": "2022-01-01"}}],"specialisations": {{"en": {}}},"unit_group": {{"_ref": "{}","_strengthenOnPublish":{{"template":{{"id":"unit_group"}},"type":"unit_group"}},"_type":"reference","_weak":true}}}}    , "assessing_authority":"{}",{},"code":{},"slug": {{"_type": "slug","current": "{}"}},"title":{{"en":"{}"}},{}'.format(id,self.group[0],self.group[2],self.group[1],self.necs,self.alternative_title,self.description,skills_Priority,self.specialisation,self.unit_group_refrence,self.assesin_authority,self.backlogs,current_code,slug,self.title,visa_option)).replace("'",'"').replace(".<br />rn<br />rn"," ")
        ndjson_sanity = ('''{{{},{}}} '''.format(allExport,states)).replace("�","`")
        
        with open(r"../output/occupation.ndjson","a") as write:
             write.write(ndjson_sanity+"\n")        
        
    def loop_in_range_codes(self) :
        for i in range(len(self.allCodes)):
            global current_code  
            current_code = str(self.allCodes[i])
            threads= list()
            x = threading.Thread(target=self.occupation_anzco(), args=(1))
            threads.append(x)
            x.start()    


if os.path.exists(r"../output/occupation.ndjson"):
        os.remove(r"../output/occupation.ndjson")

with open(r"../output/occupation.ndjson","a") as wr:
    wr.write('''{"_createdAt":"2022-11-19T15:35:41Z","_id":"a2557a7b2e94197ff767970b67041697","_rev":"YI3rks3mbRtnzMpdnkW8m6","_type":"visa_type","_updatedAt":"2022-11-19T15:38:07Z","description":{"en":"Skilled Independent"},"title":{"en":"Visa Subclass 189"},"url":{"en":"https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-independent-189"}}
{"_createdAt":"2022-11-19T15:38:52Z","_id":"cfecdb276f634854f3ef915e2e980c31","_rev":"PJutSls1mvFq6xuKwD4Kfh","_type":"visa_type","_updatedAt":"2022-11-19T15:38:52Z","description":{"en":"Skilled Nominated"},"title":{"en":"Visa Subclass 190"},"url":{"en":"https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-nominated-190"}}
{"_createdAt":"2022-11-19T15:39:25Z","_id":"559cb990c9dffd8675f6bc2186971dc2","_rev":"YI3rks3mbRtnzMpdnkWNMU","_type":"visa_type","_updatedAt":"2022-11-19T15:39:25Z","description":{"en":"State/Territory nominated"},"title":{"en":"Visa Subclass 491"},"url":{"en":"https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-work-regional-provisional-491"}}
{"_createdAt":"2022-11-19T15:40:24Z","_id":"94c2fee252465788920a8784820d3b5a","_rev":"YI3rks3mbRtnzMpdnkWaQE","_type":"visa_type","_updatedAt":"2022-11-19T15:40:24Z","description":{"en":"Family Sponsored"},"title":{"en":"Visa Subclass 491 - Family"},"url":{"en":"https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/skilled-work-regional-provisional-491"}}
{"_createdAt":"2022-11-19T15:41:12Z","_id":"90d991b47098ceef3d8283a386cf7e91","_rev":"PJutSls1mvFq6xuKwD4v5F","_type":"territory","_updatedAt":"2022-11-19T15:42:48Z","abv":"ACT","title":{"en":"Australian Capital Territory"},"url":{"en":"https://www.act.gov.au/migration/skilled-migrants"}}
{"_createdAt":"2022-11-19T15:43:25Z","_id":"7fd51c89695b098a88a38f57ae4bfb2d","_rev":"YI3rks3mbRtnzMpdnkXEHW","_type":"territory","_updatedAt":"2022-11-19T15:43:25Z","abv":"NSW","title":{"en":"New South Wales"},"url":{"en":"https://www.nsw.gov.au/visas-and-migration/skilled-visas"}}
{"_createdAt":"2022-11-19T15:44:01Z","_id":"cb48af3e40ab9ec3622c07b8faf27cf3","_rev":"YI3rks3mbRtnzMpdnkXJsY","_type":"territory","_updatedAt":"2022-11-19T15:44:01Z","abv":"NT","title":{"en":"Northern Territory"},"url":{"en":"https://theterritory.com.au/migrate"}}
{"_createdAt":"2022-11-19T15:44:44Z","_id":"c6f45fe1ff59e2232e252c632252c728","_rev":"bUMlF7B1Xxw34pzcKph5Cg","_type":"territory","_updatedAt":"2022-11-19T15:44:44Z","abv":"QLD","title":{"en":"Queensland "},"url":{"en":"https://migration.qld.gov.au/visa-options/skilled-visas"}}
{"_createdAt":"2022-11-19T15:47:23Z","_id":"3dd6b9265ff18f31dc30df59304b0ca7","_rev":"PJutSls1mvFq6xuKwD8pbd","_type":"territory","_updatedAt":"2022-11-19T15:47:23Z","abv":"SA","title":{"en":"South Australia "},"url":{"en":"https://migration.sa.gov.au/skilled-migrants"}}
{"_createdAt":"2022-11-19T15:47:53Z","_id":"f4e1b83458954d7218793cee79be80b0","_rev":"YI3rks3mbRtnzMpdnkeBc2","_type":"territory","_updatedAt":"2022-11-19T15:47:53Z","abv":"TAS","title":{"en":"Tasmania"},"url":{"en":"https://www.migration.tas.gov.au/skilled_migrants"}}
{"_createdAt":"2022-11-19T15:48:27Z","_id":"d48afc599a256e036954100b5cfbe360","_rev":"bUMlF7B1Xxw34pzcKpikes","_type":"territory","_updatedAt":"2022-11-19T15:48:27Z","abv":"VIC","title":{"en":"Victoria"},"url":{"en":"https://liveinmelbourne.vic.gov.au/migrate/skilled-migration-visas/2022-23-skilled-migration-visa-nomination-program"}}
{"_createdAt":"2022-11-19T15:48:51Z","_id":"4306a04670067b5b27e766335d3d40fa","_rev":"bUMlF7B1Xxw34pzcKpilnq","_type":"territory","_updatedAt":"2022-11-19T15:48:51Z","abv":"WA","title":{"en":"Western Australia"},"url":{"en":"https://www.migration.wa.gov.au/services/skilled-migration-western-australia/wa-state-nomination-combined-occupation-list"}}\n''')

ugly_to = beutifull()
occupation = anzco()
occupation.loop_in_range_codes()
