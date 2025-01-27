import requests
import treelib
import re
import sys
import inspect
import random
import json
import Dataset_Creation.Data_Extraction.utilities as utilities

#@dataclass
class TemporalNode(object):
  def __init__(self, medal = "None", year = 0, player = False, place = "None", birth_year = "None", birth_month = "None", birth_date = "None", country_representing = "None", tournament_Name = "None", tournament_Format = "None"):
        self.birth_year = birth_year
        self.birth_month = birth_month       
        self.birth_date = birth_date
        self.year = year
        self.medal = medal
        self.player = player
        self.place = place
        self.country_representing = country_representing
        self.tournament_Name = tournament_Name
        self.tournament_Format = tournament_Format
        
  def __str__(self):
        return "Player: " + str(self.player) + "    Medal: " + self.medal + "   Year: " + str(self.year) + "   Place: " + str(self.place) + "   Birth_Year: " + str(self.birth_year) + "   Birth_Month: " + str(self.birth_month) + "   Birth_Date: " + str(self.birth_date) + "   Country_Representing: " + str(self.country_representing) + "   Tournament_Name: " + str(self.tournament_Name) + "   Tournament_Format: " + str(self.tournament_Format)


def cleanString(input):
    input = input.encode(encoding='utf-8',errors='ignore')
    input = input.decode(encoding='utf-8',errors='ignore')
    input = input.replace('×', 'x')
    input = input.replace('–', '-')
    input = input.replace(':', '')
    return input

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

def generate_temporal_graph(TITLE):
    ###############################################
    #                                             #  
    #              ALGORITHM START                #
    #                                             #  
    ###############################################
    random.seed(10)
    
    debugMode = False
    player_TITLE = TITLE

    PARAMS = {
        'action': "parse",
        'page': player_TITLE,
        'prop': 'wikitext',
        'section': 0,
        'format': "json"
    }

    def get_table():
        """ Parse a section of a page, fetch its table data and save it to a CSV file
        """
        res = S.get(url=URL, params=PARAMS)
        data = res.json()
        wikitext = data['parse']['wikitext']['*']
        lines = wikitext.split('\n\n\'\'\'')[0]
        
        return lines.split("\n")

    # Print table   
    try:
        l = get_table()
        #print(l)
    except Exception as e:
        if debugMode:
            print("ERROR IN GETTING DATA_1:", e)
            print(player_TITLE)

        
    # Initialize the tree
    G = treelib.Tree()

    try:
        G.create_node("Personal Information", "Personal Information", parent=player_TITLE)
    except Exception as e:
        if debugMode:
            print("ERROR_2:", e)

    # Discard all lines until infobox is found
    infoboxFound = False
    medalTemplatesFound = False
    medalCountryFound = False
    try:
        for line in l:

            #############################
            #                           #
            #    PERSONAL INFO START    #
            #                           #
            #############################

            if "birth_date" in line:
                try:
                    regex = r'(birth_date).*(\d{4})\|(\d{1,2})\|(\d{1,2})'
                    match = re.search(regex, line)
                    try:
                        G.create_node("Birth Date", "Birth Date", parent="Personal Information")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_3:", e)
                            print(line)
                    birthYear = match.group(2)
                    birthMonth = match.group(3)
                    birthDate = match.group(4)
                    combined_birthDate = match.group(2) + "-" + match.group(3) + "-" + match.group(4)
                    try:
                        G.create_node(combined_birthDate, combined_birthDate, parent="Birth Date", data=TemporalNode(birth_date= int(birthDate), birth_month= int(birthMonth), birth_year= int(birthYear)))
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_4:", e)
                            print(line)
                except Exception as e:
                    if debugMode:
                        print("REGEX ERROR_5:", e)
                        print(line)                     
                continue

            if "birth_place" in line:
                try:
                    regex = r'(birth_place).*=\s\[?\[?([\w+, ,-]*).*'
                    match = re.search(regex, line)
                    try:
                        G.create_node("Birth Place", "Birth Place", parent="Personal Information")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_6:", e)
                            print(line)
                    birth_place = match.group(2)
                    try:
                        G.create_node(birth_place, birth_place, parent="Birth Place")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_7:", e)
                            print(line)
                except Exception as e:
                    if debugMode:
                        print("REGEX ERROR_8:", e)
                        print(line)            
                continue

            if "height" in line:
                if all(substr in line for substr in ["height", "Cvt", "ft", "in"]):
                    try:
                        regex = r'(height)\s*=\s*\{?\{?\w*\|(\d+)\|?(\w*)\|(\d+)\|?(\w*).*'
                        match = re.search(regex, line)
                        try:
                            G.create_node("Height", "Height", parent="Personal Information")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_9:", e)
                                print(line)
                        height = match.group(2) + " " +  match.group(3) + " " +  match.group(4) + " " + match.group(5)
                        try:
                            G.create_node(height, height, parent="Height")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_10:", e)
                                print(line)
                    except Exception as e:
                        if debugMode:
                            print("REGEX ERROR:_11", e)
                            print(line)                    
                    continue
                else:
                    try:
                        regex = r'(height)\s*=\s?(\d+\.?\d*)\s*(cm|m)'
                        match = re.search(regex, line)
                        try:
                            G.create_node("Height", "Height", parent="Personal Information")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_12:", e)
                                print(line)
                        height = match.group(2) + " " + match.group(3)
                        try:
                            G.create_node(height, height, parent="Height")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_13:", e)
                                print(line)
                    except Exception as e:
                        if debugMode:
                            print("REGEX ERROR_14:", e)
                            print(line)                    
                    continue

            if "weight" in line:
                if all(substr in line for substr in ["weight", "convert"]):
                    try:
                        regex = r'(weight).*=.*\|{1}(\d+)\|.*'
                        match = re.search(regex, line)
                        try:
                            G.create_node("Weight", "Weight", parent="Personal Information")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_15:", e)
                                print(line)
                        weight = match.group(2) + " " + "kg"
                        try:
                            G.create_node(weight, weight, parent="Weight")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_16:", e)
                                print(line)
                    except Exception as e:
                        if debugMode:
                            print("REGEX ERROR_17:", e)
                            print(line)
                    continue
                else:
                    try:
                        regex = r'(weight).*=\s?(\d+.\d*).*(kg|lb)'
                        match = re.search(regex, line)
                        try:
                            G.create_node("Weight", "Weight", parent="Personal Information")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_18:", e)
                                print(line)
                        weight = match.group(2) + " " + match.group(3)
                        try:
                            G.create_node(weight, weight, parent="Weight")
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_19:", e)
                                print(line)
                    except Exception as e:
                        if debugMode:
                            print("REGEX ERROR_20:", e)
                            print(line)                  
                    continue

            if "years_active" in line:
                try:
                    regex = r'(years_active).*= (\d{4}).(.*)'
                    match = re.search(regex, line)
                    try:
                        G.create_node("Years Active", "Years Active", parent="Personal Information")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_21:", e)
                            print(line)
                    yearsActive = match.group(2) + "-" + match.group(3)
                    try:
                        G.create_node(yearsActive, yearsActive, parent="Years Active")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_22:", e)
                            print(line)
                except Exception as e:
                    if debugMode:
                        print("REGEX ERROR_23:", e)
                        print(line)
                continue

            if "handedness" in line:
                try:
                    regex = r'(handedness).*= (Left|Right)'
                    match = re.search(regex, line)
                    try:
                        G.create_node("Handedness", "Handedness", parent="Personal Information")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_24:", e)
                            print(line)
                    handedness = match.group(2)
                    try:
                        G.create_node(handedness, handedness, parent="Handedness")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_25:", e)
                            print(line)
                except Exception as e:
                    if debugMode:
                        print("REGEX ERROR_26:", e)
                        print(line)  
                continue

            if "coach" in line:
                try:
                    regex = r'(coach)\s*=\s?\[?\[?([\w,\.,\s,\-]*)'
                    match = re.search(regex, line)
                    try:
                        G.create_node("Coach", "Coach", parent="Personal Information")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_27:", e)
                            print(line)   
                    coach = match.group(2)
                    try:
                        G.create_node(coach, coach, parent="Coach")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_28:", e)
                            print(line)
                except Exception as e:
                    if debugMode:
                        print("REGEX ERROR_29:", e)
                        print(line)     
                continue

            if "career_record" in line:
                try:
                    regex = r'(career_record).*= (.*)'
                    match = re.search(regex, line)
                    try:
                        G.create_node("Career Record", "Career Record", parent="Personal Information")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_30:", e)
                            print(line)
                    careerRecord = match.group(2)
                    try:
                        G.create_node(careerRecord, careerRecord, parent="Career Record")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_31:", e)
                            print(line)
                except Exception as e:
                    if debugMode:
                        print("REGEX ERROR_32:", e)
                        print(line)
                continue

            if "date_of_highest_ranking" in line:
                try:
                    regex = r'(date_of_highest_ranking).*=\s([\d,\w,\s]+)'
                    match = re.search(regex, line)
                    try:
                        G.create_node("Date Of Highest Ranking", "Date Of Highest Ranking", parent="Personal Information")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_33:", e)
                            print(line)
                    dateOfHighestRanking = match.group(2)
                    try:                   
                        G.create_node(dateOfHighestRanking, dateOfHighestRanking, parent="Date Of Highest Ranking")
                    except Exception as e:
                        if debugMode:
                            print("NODE ERROR_34:", e)
                            print(line)
                except Exception as e:
                    if debugMode:
                        print("REGEX ERROR_35:", e)
                        print(line)
                continue
            #############################
            #                           #
            #    PERSONAL INFO END      #
            #                           #
            #############################

            if "Infobox" in line:
                infoboxFound = True
                continue
            if medalTemplatesFound:
                fields = line.split("|")
                if "MedalCountry" in fields[0] or (len(fields) > 1 and "Country" in fields[1]):
                    medalCountryFound = True
                    fieldLength = len(fields)
                    text = "Country Representing: "
                    try:
                        regex = r'(\w[\w ]+)}}'       
                        match = re.search(regex, fields[fieldLength - 1])
                        countryRepresenting = text + match.group(1) 
                        try:                        
                            G.create_node(countryRepresenting, countryRepresenting, parent=player_TITLE, data=TemporalNode(country_representing = countryRepresenting))
                        except Exception as e:
                            if debugMode:
                                print("NODE ERROR_36:", e)
                                print(line)

                    except Exception as e:
                        if debugMode:
                            print("REGEX ERROR_37:", e)
                            print(line)

                    continue

                if medalCountryFound:
                    # Tournament Name:
                    if "MedalOlympic" in fields[0]:
                        tournamentName = "Olympic Games"
                        if not G.contains(tournamentName):
                            try:                         
                                G.create_node(tournamentName, tournamentName, parent=countryRepresenting, data=TemporalNode(tournament_Name = tournamentName))
                            except Exception as e:
                                if debugMode:
                                    print("NODE ERROR_38:", e)
                                    print(line)

        
                    if "MedalCompetition" in fields[0] or (len(fields) > 1 and "MedalCompetition" in fields[0]+fields[1]):
                        fieldLength = len(fields)
                        tournamentName = fields[fieldLength - 1]
                        try:
                            regex = r'\w[\w \(\)]*'
                            match = re.search(regex, tournamentName)
                            if match:
                                tournamentName = match.group(0)
                                if not G.contains(tournamentName):
                                    try:                            
                                        G.create_node(tournamentName, tournamentName, parent=countryRepresenting, data=TemporalNode(tournament_Name = tournamentName))
                                    except Exception as e:
                                        if debugMode:
                                            print("NODE ERROR_39:", e)
                                            print(line)

                        except Exception as e:
                            if debugMode:
                                print("REGEX ERROR_40:", e)
                                print(line)
                        continue

                    if (("MedalGold" in fields[0] or (len(fields) > 1 and "MedalGold" in fields[0]+fields[1])) 
                        or ("MedalSilver" in fields[0] or (len(fields) > 1 and "MedalSilver" in fields[0]+fields[1])) 
                        or ("MedalBronze" in fields[0] or (len(fields) > 1 and "MedalBronze" in fields[0]+fields[1]))):
                        fieldLength = len(fields)
                        tournamentFormat = fields[fieldLength - 1]
                        tournamentFormat = cleanString(tournamentFormat)
                        tournamentFormat = tournamentFormat.replace("&nbsp;", " ")
                        try:
                            regex = r'(\w[\w \']*)'                        
                            match = re.search(regex, tournamentFormat)
                            try:
                                tournamentFormat = match.group(0)
                            except Exception as e:
                                tournamentFormat = "None"

                            tournamentFormat_tag = tournamentFormat
                            tournamentFormat = tournamentName + tournamentFormat

                            if not G.contains(tournamentFormat):
                                try:
                                    G.create_node(tournamentFormat_tag, tournamentFormat, parent=tournamentName, data=TemporalNode(tournament_Format = tournamentFormat_tag))
                                except Exception as e:
                                    if debugMode:
                                        print("NODE ERROR_41:", e)
                                        print(line)

                            regex = r'(MedalGold|MedalSilver|MedalBronze|Medal\|Gold|Medal\|Silver|Medal\|Bronze).*(\| *(\d{4}) ([\w ]+\w)|(\|([\w ]+\w)\|(\d{4})))'
                            match = re.search(regex, line)  
                            medalyear = ""
                            medalPlace = ""
                            medalName = ""
                            if match:
                                if match.group(3):
                                    medal_Type_Year_Place = match.group(1).replace("|", "") + " | " + match.group(3) + " | " + match.group(4)
                                    medalyear = match.group(3)
                                    medalPlace = match.group(4)
                                    medalName = match.group(1).replace("|", "")
                                else:
                                    medal_Type_Year_Place = match.group(1).replace("|", "") + " | " + match.group(7) + " | " + match.group(6)
                                    medalyear = match.group(7)
                                    medalPlace = match.group(6)
                                    medalName = match.group(1).replace("|", "")
                                medal_Type_Year_Place_id = medal_Type_Year_Place + tournamentFormat

                                if not G.contains(medal_Type_Year_Place_id): 
                                    try:
                                        G.create_node(medal_Type_Year_Place, medal_Type_Year_Place_id, parent=tournamentFormat, data=TemporalNode(year=int(medalyear), place=str(medalPlace), medal=str(medalName)))
                                    except Exception as e:
                                        if debugMode:
                                            print("NODE ERROR_42:", e)
                                            print(line)
                        except Exception as e:
                            if debugMode:
                                print("REGEX ERROR_43:", e)
                                print(line)
                        continue        
                continue

            if infoboxFound:
                fields = line.split("=")

                if len(fields) > 0 and ("medaltemplates" or "medal_templates" or "medals" in fields[0]):
                    medalTemplatesFound = True

                    continue

    except Exception as e:
        if debugMode:
            print("PARSE ERROR_44:", e)
            print(line)

    return G

    ###############################################
    #                                             #  
    #              ALGORITHM END                  #
    #                                             #  
    ###############################################


def generate_Counterfactual_temporal_graph(TITLE):
    ###############################################
    #                                             #  
    #              ALGORITHM START                #
    #                                             #  
    ###############################################
    random.seed(10)
    
    player_TITLE = TITLE

    try:
        TournamentsPlayed = list(set(value.strip() for value in utilities.GetTournamentsPlayed_WithoutYears(player_TITLE)))
        FormatsPlayed = list(set(value.strip() for value in utilities.GetFormatsPlayed(player_TITLE)))
        MedalTypes = list(["MedalBronze", "MedalSilver", "MedalGold"])
        YearsPlayed = list(set(value.strip() for value in utilities.GetYearsPlayed(player_TITLE)))
        CitiesPlayed = list(set(value.strip() for value in utilities.GetCitiesNamePlayed(player_TITLE)))

        original_tree = generate_temporal_graph(player_TITLE)


        counter_tree = treelib.Tree()
        counter_tree.create_node(player_TITLE, player_TITLE)
        

        country_representing = None
        for child in original_tree.children(player_TITLE):
            if "Country Representing" in child.tag:
                counter_tree.create_node(child.tag, child.tag, player_TITLE)
                country_representing = child
                break


        used_tid = []
        for _ in range(len(TournamentsPlayed)):
            tid = random.randint(0, len(TournamentsPlayed)-1)
            while (tid in used_tid):
                tid = random.randint(0, len(TournamentsPlayed)-1)
            used_tid.append(tid)
            counter_tree.create_node(TournamentsPlayed[tid], TournamentsPlayed[tid], country_representing.tag)
            
            used_fid = []
            nFormats = random.randint(1, len(FormatsPlayed)) 
            for _ in range(nFormats):
                fid = random.randint(0, len(FormatsPlayed)-1)
                while (fid in used_fid):
                    fid = random.randint(0, len(FormatsPlayed)-1)
                used_fid.append(fid)
                counter_tree.create_node(FormatsPlayed[fid], TournamentsPlayed[tid]+FormatsPlayed[fid], TournamentsPlayed[tid])

                used_mid = []
                nMedalTypes = random.randint(1, 4) 
                for _ in range(nMedalTypes):
                    mid = random.randint(0, len(MedalTypes)-1)
                    year = int(YearsPlayed[random.randint(0, len(YearsPlayed)-1)].strip()) + random.randint(-4, 4)
                    mtype_year_city = MedalTypes[mid].strip() + " | " + str(year).strip() + " | " + CitiesPlayed[random.randint(0, len(CitiesPlayed)-1)]
                    while mtype_year_city in used_mid or year > 2024:
                        year = int(YearsPlayed[random.randint(0, len(YearsPlayed)-1)].strip()) + random.randint(-4, 4)
                        mtype_year_city = MedalTypes[mid].strip() + " | " + str(year).strip() + " | " + CitiesPlayed[random.randint(0, len(CitiesPlayed)-1)]
                    used_mid.append(mtype_year_city)
                    counter_tree.create_node(mtype_year_city, TournamentsPlayed[tid]+FormatsPlayed[fid]+mtype_year_city, 
                                            TournamentsPlayed[tid]+FormatsPlayed[fid])
        
        birth_year = original_tree.children("Birth Date")

        birth_year_tag = birth_year[0].tag
        birth_year_tag_splits = birth_year_tag.split("-")
        birth_year_tag_year = birth_year_tag_splits[0]
        birth_year_tag_month = birth_year_tag_splits[1]
        birth_year_tag_date = birth_year_tag_splits[2]
        birth_year_tag_year = str(int(birth_year_tag_year) + random.randint(-2, 2))

        birth_year_tag_modified = birth_year_tag_year + "-" + birth_year_tag_month + "-" + birth_year_tag_date

        counter_tree.create_node("Personal Information", "Personal Information", parent=player_TITLE)
        counter_tree.create_node("Birth Date", "Birth Date", parent="Personal Information")
        counter_tree.create_node(birth_year_tag_modified, birth_year_tag_modified, parent="Birth Date")
    except Exception as e:
        print(e)
        pass
 
    return counter_tree
