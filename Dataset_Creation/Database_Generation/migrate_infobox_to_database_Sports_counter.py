import mysql.connector
import sys
import os
from treelib import Tree
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import Dataset_Creation.Data_Extraction.extract_infobox as extract_infobox
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Connect to MariaDB
db_connection = mysql.connector.connect(
    #####################
    # Connection String #
    #####################
)
cursor = db_connection.cursor()

# Define SQL insert statements
insert_athlete = "INSERT INTO Athlete (name) VALUES (%s)"
insert_tournament = "INSERT INTO Tournament (athlete_id, name) VALUES (%s, %s)"
insert_format = "INSERT INTO Format (tournament_id, name) VALUES (%s, %s)"
insert_medal = "INSERT INTO Medal (format_id, type, year, location) VALUES (%s, %s, %s, %s)"
insert_personal_info = "INSERT INTO PersonalInformation (athlete_id, birth_year, birth_month, birth_day) VALUES (%s, %s, %s, %s)"

Players = GetPlayerNames()



PlayerData_dict_with_P_info = {}
for player in Players:
    try:
        player_tree_with_P_info = extract_infobox.generate_temporal_graph(player)
        PlayerData_dict_with_P_info[player] = player_tree_with_P_info
        print(f"PlayerData_dict_with_P_info: {player}")
    except Exception as e:
        print(f"Error generating tree with personal info for player {player}: {e}")

PlayerData_dict_without_P_info = {}
for player in Players:
    try:
        player_tree_without_P_info = extract_infobox.generate_temporal_graph_WithoutPersonalInfo(player)
        PlayerData_dict_without_P_info[player] = player_tree_without_P_info
        print(f"PlayerData_dict_without_P_info: {player}")
    except Exception as e:
        print(f"Error generating tree without personal info for player {player}: {e}")

print("Generated all trees.")

def parse_and_store_trees(athletes_trees_with_Pinfo, athletes_trees_without_Pinfo):
    for athlete_name, tree in athletes_trees_without_Pinfo.items():
        try:
            athlete_id = None
            country_representing = tree.children(tree.root)[0]
            tournaments = tree.children(country_representing.identifier)

            # Insert Athlete
            cursor.execute(insert_athlete, (athlete_name,))
            athlete_id = cursor.lastrowid

            for tournament_node in tournaments:
                try:
                    tournament_name = tournament_node.tag
                    tournament_id = None

                    # Insert Tournament
                    cursor.execute(insert_tournament, (athlete_id, tournament_name))
                    tournament_id = cursor.lastrowid

                    formats = tree.children(tournament_node.identifier)
                    for format_node in formats:
                        try:
                            format_name = format_node.tag
                            format_id = None

                            # Insert Format
                            cursor.execute(insert_format, (tournament_id, format_name))
                            format_id = cursor.lastrowid

                            medals = tree.children(format_node.identifier)
                            for medal_node in medals:
                                try:
                                    medal_info = medal_node.tag.split(" | ")
                                    medal_type = medal_info[0].strip()
                                    medal_year = int(medal_info[1].strip())
                                    medal_location = medal_info[2].strip()

                                    # Insert Medal
                                    cursor.execute(insert_medal, (format_id, medal_type, medal_year, medal_location))
                                except Exception as e:
                                    print(f"Error inserting medal for player {athlete_name}: {e}")
                                    continue
                        except Exception as e:
                            print(f"Error inserting format for player {athlete_name}: {e}")
                            continue
                except Exception as e:
                    print(f"Error inserting tournament for player {athlete_name}: {e}")
                    continue

            try:
                # Find Birth Date node directly by its tag "Birth Date"
                tree_with_Pinfo = athletes_trees_with_Pinfo[athlete_name]
                birth_date_node = tree_with_Pinfo.children("Birth Date")[0]
                birth_date = birth_date_node.tag
                birth_year, birth_month, birth_day = map(int, birth_date.split('-'))

                # Insert Personal Information (Birth Date only)
                cursor.execute(insert_personal_info, (athlete_id, birth_year, birth_month, birth_day))
            except Exception as e:
                print(f"Error inserting personal information for player {athlete_name}: {e}")

            # Commit changes after processing each athlete
            db_connection.commit()
            print(f"Data for athlete {athlete_name} has been stored in the database.")
        except Exception as e:
            print(f"Error processing player {athlete_name}: {e}")
            db_connection.rollback()
            continue

# Execute the function: First provide with_P_info then provide without_P_info
parse_and_store_trees(PlayerData_dict_with_P_info, PlayerData_dict_without_P_info)

# Close cursor and database connection
cursor.close()
db_connection.close()
