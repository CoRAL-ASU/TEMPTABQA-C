import random
import secrets
import Dataset_Creation.Data_Extraction.extract_infobox as extract_infobox
random.seed(10)


def GetCountriesPlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"
    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    CountriesPlayedList = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        country = x.tag
        if "Country Representing:" in x.tag:
            country = country.replace("Country Representing:", "")
        country = country.strip()
        CountriesPlayedList.append(country) 
        CountriesPlayedList = list(set(CountriesPlayedList))
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    pass   
    return CountriesPlayedList      

def GetTournamentsPlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    tournamentsList = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    # Tournament Formats _ Level 3 nodes
                    mylist = x3.identifier
                    fields = mylist.split("|")
                    #tournaments = fields[1] + fields[3]
                    tournaments = fields[0] + fields[2]
                    tournamentsList.append(tournaments) 
                    tournamentsList = list(set(tournamentsList))    
    #print(*tournamentsList, sep='\n')
    return tournamentsList      

def GetYearsPlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    YearsPlayedList = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    # Tournament Formats _ Level 3 nodes
                    mylist = x3.identifier
                    fields = mylist.split("|")
                    Years = fields[1]
                    YearsPlayedList.append(Years) 
                    YearsPlayedList = list(set(YearsPlayedList))    
    #print(*YearsPlayedList, sep='\n')
    return YearsPlayedList      


def GetMedalTypes(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    MedalTypesList = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    # Tournament Formats _ Level 3 nodes
                    mylist = x3.identifier
                    # mylist = x3.tag
                    fields = mylist.split("|")
                    Medal = fields[0]
                    MedalTypesList.append(Medal) 
                    MedalTypesList = list(set(MedalTypesList))    
    #print(*MedalTypesList, sep='\n')
    return MedalTypesList      


def GetCitiesPlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    CitiesList = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    # Tournament Formats _ Level 3 nodes
                    mylist = x3.tag
                    fields = mylist.split("|")
                    City = fields[2].strip()
                    CitiesList.append(City) 
                    CitiesList = list(set(CitiesList))    
    #print(*CitiesList, sep='\n')
    return CitiesList   

def GetCitiesNamePlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    CitiesList = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    # Tournament Formats _ Level 3 nodes
                    mylist = x3.tag
                    fields = mylist.split("|")
                    City = fields[2].strip()
                    CitiesList.append(City) 
    CitiesList = list(set(CitiesList))    
    #print(*CitiesList, sep='\n')
    return CitiesList   

def GetCitiesWithTournamentsPlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    Cities_TournamentList = []
    # Player Name
    l = tree.children(tree.root)
    #tree.show()
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            Tournament = x1.tag
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    # Tournament Formats _ Level 3 nodes
                    mylist = x3.identifier
                    fields = mylist.split("|")
                    City_Tournament = fields[2].strip() + " " + Tournament
                    City_Tournament = City_Tournament.strip()
                    Cities_TournamentList.append(City_Tournament) 
                    Cities_TournamentList = list(set(Cities_TournamentList))    
    #print(*Cities_TournamentList, sep='\n')
    return Cities_TournamentList   


def GetTournamentsPlayed_WithoutYears(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    tournamentsList_WithoutYears = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            tournamentsNames = x1.tag
            tournamentsList_WithoutYears.append(tournamentsNames)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                #print(x2.tag)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    pass

    #print(*tournamentsList_WithoutYears, sep='\n')
    return tournamentsList_WithoutYears    

def GetTournamentsPlayed_And_FormatsPlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    tournamentsAndFormats = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            tournamentsName = x1.tag
            tournamentsName = tournamentsName.strip()
            
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                TournamentFormat = x2.tag
                TournamentFormat = TournamentFormat.strip()
                TournamentNameAndFormat = TournamentFormat + " " + tournamentsName
                tournamentsAndFormats.append(TournamentNameAndFormat)
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    pass

    #print(*tournamentsAndFormats, sep='\n')
    return tournamentsAndFormats      

def GetTournamentsPlayed_And_FormatsPlayed_And_Years(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    TournamentNameAndFormatAndYear = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            tournamentsName = x1.tag
            tournamentsName = tournamentsName.strip()
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                TournamentFormat = x2.tag
                TournamentFormat = TournamentFormat.strip()
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    Year_City_Medal = x3.identifier
                    fields = Year_City_Medal.split("|")
                    Year = fields[1].strip()
                    Year_Format_Tournament = Year + " " + TournamentFormat + " " + tournamentsName
                    TournamentNameAndFormatAndYear.append(Year_Format_Tournament)
                    
    #print(*TournamentNameAndFormatAndYear, sep='\n')
    return TournamentNameAndFormatAndYear      

def GetFormatsPlayed(PassedInPlayer):
    Player_Name = PassedInPlayer
    #Player_Name = "Michael Phelps"

    tree = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(Player_Name)
    #tree.show(key=False)
    FormatsList = []
    FormatsList_Without_Duplicates = []
    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        # print(x.tag)
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            #print(x1.tag)
            l2 = tree.children(x1.identifier)
            for x2 in l2:      
                # Tournament Formats _ Level 3 nodes
                FormatNames = x2.tag
                FormatsList.append(FormatNames)
                FormatsList_Without_Duplicates = list(set(FormatsList))
                l3 = tree.children(x2.identifier)
                for x3 in l3:
                    # Medal Year Place
                    pass

    #print(*FormatsList_Without_Duplicates, sep='\n')
    return FormatsList_Without_Duplicates  



def ConvertGraphToTable(PassedInPlayer):
    Player_Name = PassedInPlayer
    graph = extract_infobox.generate_temporal_graph(Player_Name)
    Table = graph.to_dict()
    return Table

def GetTable(PassedInPlayer):
    context = ""
    Player_Name = PassedInPlayer
    tree = extract_infobox.generate_temporal_graph(Player_Name)
    context += Player_Name + "\n" + "\n"

    # Player Name
    l = tree.children(tree.root)
    for x in l:
        # Personal Info + Country Representing
        context += x.tag + "\n"
        l1 = tree.children(x.identifier)
        for x1 in l1:
            # Tournament Names _ Level 2 nodes
            context += x1.tag + "\n"
            l2 = tree.children(x1.identifier)
            for x2 in l2:
                # Tournament Formats _ Level 3 nodes
                context += x2.tag + "\t"
                l3 = tree.children(x2.identifier)
                medal_info = []
                for x3 in l3:
                    medal_info.append(x3.tag)
                context += ", ".join(medal_info) + "\n"
            context += "\n"
    return context

def RemoveDuplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def generate_random_numbers(number_list):
    if len(number_list) < 2:

        return None

    index1 = random.randint(0, len(number_list) - 1)
    index2 = random.randint(0, len(number_list) - 1)

    while index2 == index1:
        index2 = random.randint(0, len(number_list) - 1)

    return index1, index2



def generate_random_indices(player, TournamentsPlayed, FormatsPlayed, YearsPlayed, CitiesPlayed, MedalTypes):
    try:
        TournamentIndex_1, TournamentIndex_2 = generate_random_numbers(TournamentsPlayed)
    except:
        TournamentIndex_1, TournamentIndex_2 = None, None

    try:
        Formatindex_1, Formatindex_2 = generate_random_numbers(FormatsPlayed)
    except:
        Formatindex_1, Formatindex_2 = None, None

    try:
        Yearindex_1, Yearindex_2 = generate_random_numbers(YearsPlayed)
    except:
        Yearindex_1, Yearindex_2 = None, None

    try:
        Cityindex_1, Cityindex_2 = generate_random_numbers(CitiesPlayed)
    except:
        Cityindex_1, Cityindex_2 = None, None

    try:
        MedalType_Index1, MedalType_Index2 = generate_random_numbers(MedalTypes)
    except:
        MedalType_Index1, MedalType_Index2 = None, None

    return (
        TournamentIndex_1, TournamentIndex_2,
        Formatindex_1, Formatindex_2,
        Yearindex_1, Yearindex_2,
        Cityindex_1, Cityindex_2,
        MedalType_Index1, MedalType_Index2
    )