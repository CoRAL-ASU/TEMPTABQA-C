def fewshot_with_infobox_as_context(context, question):
    return f"""
    Your task is to answer the given question based on the context provided and provide a well-reasoned response seperated by &&.

    Instructions-
    1. Only answer the question based on the infromation given in the context.
    2. Provide the answer in a straigtforward manner and keep it within 1 to 10 words.
    3. Respond with Yes/No in relevant questions.
    4. Note an event is a combination of Tournament, Format and the corresponding year. For example:
        European Junior Championships | Girls' singles | 2009

    Few Example Questions are given below with Context and answers along with reasoning to arrive at the answer:
    
    context :
    P. V. Sindhu    
    Personal Information
    Birth Date
    1995-7-5	

    Birth Place
    Hyderabad, Andhra Pradesh	

    Height
    1.79 m	

    Weight
    65  kg	

    Years Active
    2011-present	

    Handedness
    Right	

    Coach
    Agus Dwi Santoso	

    Career Record
    469 wins, 209 losses	

    Date Of Highest Ranking
    1 	

    Country Representing: IND
    Olympic Games
    Women's singles	MedalSilver | 2016 | Rio de Janeiro, MedalBronze | 2020 | Tokyo

    World Championships
    Women's singles	MedalGold | 2019 | Basel, MedalSilver | 2017 | Glasgow, MedalSilver | 2018 | Nanjing, MedalBronze | 2013 | Guangzhou, MedalBronze | 2014 | Copenhagen

    Uber Cup
    Women's team 	MedalBronze | 2014 | New Delhi, MedalBronze | 2016 | Kunshan

    Commonwealth Games
    Mixed team	MedalGold | 2018 | Gold Coast, MedalSilver | 2022 | Birmingham
    Women's singles	MedalGold | 2022 | Birmingham, MedalSilver | 2018 | Gold Coast, MedalBronze | 2014 | Glasgow

    Asian Games
    Women's singles	MedalSilver | 2018 | Jakarta
    Women's team	MedalBronze | 2014 | Incheon

    Asian Championships
    Women's singles 	MedalBronze | 2014 | Gimcheon, MedalBronze | 2022 | Manila

    Asia Mixed Team Championships
    Mixed team 	MedalBronze | 2023 | Dubai

    Asia Team Championships
    Women's team 	MedalGold | 2024 | Selangor

    South Asian Games
    Women's team 	MedalGold | 2016 | Guwahati
    Women's singles 	MedalSilver | 2016 | Guwahati

    Commonwealth Youth Games
    Girls' singles 	MedalGold | 2011 | Douglas

    Asian Junior Championships
    Girls' singles 	MedalGold | 2012 | Gimcheon, MedalBronze | 2011 | Lucknow
    Mixed team 	MedalBronze | 2011 | Lucknow
    
    question : How many International Bronze Medals did P. V. Sindhu win throughout his/her career?
    answer and reasoning: 12 && There are 12 MedalBronze entities in the above given context.
    
    question : How many times has P. V. Sindhu won medals in Asian Games ?
    answer and reasoning: 2 && In the above context under Asian Games there are 2 medals.
    
    question : How old was P. V. Sindhu when he/she won their first international medal ?
    answer and reasoning: 16 && Based on the above context, P. V. Sindhu won her first inter national medal in Asian Junior Championships
    in the format Girls' singles in the year 2011 at Lucknow. P. V. Sindhu was born in 1995. Hence she was 16 years old in 2011.
    
    question : In which year(s) did P. V. Sindhu win the highest number of medals during their career ?
    answer and reasoning: 2014 && Based on the above context 2014 is the year in which she has won 1 medal each in the World Championships, Uber Cup, Commonwealth Games, Asian Games and Asian Championships.
    Hence, Compared to all the other years in which she has won medals 2014 has the highest medals.
                
    question : In which format did P. V. Sindhu win her first International medal ?
    answer and reasoning: Girls' singles, Mixed team && Based on the above context P. V. Sindhu won medals in 2011 in the Commonwealth Youth Games Girls' singles format, 
    Asian Junior Championships Girls's singles format and Asian Junior Championships Mixed Team format. 2011 was also the first year in which she won an international medal. 
    Hence Girls' singles, Mixed team are the formats in which she won her first International medal.
    
    question : How many medals did P. V. Sindhu win in his mid twenties ?
    answer and reasoning: 5 && During her mid twenties that is from the start of 2019 to the end of 2023, she has won 1 medal in 2019, 1 medal in 2020, no medal in 2021 and 3 medals in 2023.
    This brings the total to 5.
                
    question : Did P. V. Sindhu win international medals in the  2012  ?
    answer and reasoning: Yes && Based on the above context P. V. Sindhu won Asian Junior Championships in the Girls' singles format by securing a Gold Medal in 2012.
    
    Please answer the following question based on the provided context.
    
    context : ***{context}***

    question : {question}
    
    LLM answer: """
    
# Zero Shot without Tabular Context
def zeroshot_without_context(question):
    return f"""
    Your task is to answer the given question.
    
    Instructions-
    1. Provide the answer in a straigtforward manner and keep it within 1 to 10 words.
    3. Respond with Yes/No in relevant questions.
    4. Note an event is a combination of Tournament, Format and the corresponding year. For example:
        European Junior Championships | Girls' singles | 2009
    
    2 Example Questions are given below:
    question : How many International Bronze Medals did P. V. Sindhu win throughout her career?
    answer: 12
    
    question : How many times has P. V. Sindhu won medals in Asian Games ?
    answer: 2
    
    Please answer the following question.
    
    question : {question}
    
    LLM answer: """
    
# Zero Shot with Infobox as Context
def zeroshot_with_infobox_as_context(context, question):
    return f"""
    Your task is to answer the given question based on the context provided.
    
    Instructions-
    1. Provide the answer in a straigtforward manner and keep it within 1 to 10 words.
    3. Respond with Yes/No in relevant questions.
    4. Note an event is a combination of Tournament, Format and the corresponding year. For example:
        European Junior Championships | Girls' singles | 2009
    
    1 Example Question and Context is given below:
    
    Context:
    P. V. Sindhu    
    Personal Information
    Birth Date
    1995-7-5	

    Birth Place
    Hyderabad, Andhra Pradesh	

    Height
    1.79 m	

    Weight
    65  kg	

    Years Active
    2011-present	

    Handedness
    Right	

    Coach
    Agus Dwi Santoso	

    Career Record
    469 wins, 209 losses	

    Date Of Highest Ranking
    1 	

    Country Representing: IND
    Olympic Games
    Women's singles	MedalSilver | 2016 | Rio de Janeiro, MedalBronze | 2020 | Tokyo

    World Championships
    Women's singles	MedalGold | 2019 | Basel, MedalSilver | 2017 | Glasgow, MedalSilver | 2018 | Nanjing, MedalBronze | 2013 | Guangzhou, MedalBronze | 2014 | Copenhagen

    Uber Cup
    Women's team 	MedalBronze | 2014 | New Delhi, MedalBronze | 2016 | Kunshan

    Commonwealth Games
    Mixed team	MedalGold | 2018 | Gold Coast, MedalSilver | 2022 | Birmingham
    Women's singles	MedalGold | 2022 | Birmingham, MedalSilver | 2018 | Gold Coast, MedalBronze | 2014 | Glasgow

    Asian Games
    Women's singles	MedalSilver | 2018 | Jakarta
    Women's team	MedalBronze | 2014 | Incheon

    Asian Championships
    Women's singles 	MedalBronze | 2014 | Gimcheon, MedalBronze | 2022 | Manila

    Asia Mixed Team Championships
    Mixed team 	MedalBronze | 2023 | Dubai

    Asia Team Championships
    Women's team 	MedalGold | 2024 | Selangor

    South Asian Games
    Women's team 	MedalGold | 2016 | Guwahati
    Women's singles 	MedalSilver | 2016 | Guwahati

    Commonwealth Youth Games
    Girls' singles 	MedalGold | 2011 | Douglas

    Asian Junior Championships
    Girls' singles 	MedalGold | 2012 | Gimcheon, MedalBronze | 2011 | Lucknow
    Mixed team 	MedalBronze | 2011 | Lucknow

    question : How many International Bronze Medals did P. V. Sindhu win throughout her career?
    answer: 12
    
    
    Please answer the following question based on the provided context.
    
    context : ***{context}***
        
    question : {question}
    
    LLM answer: """

# Dynamic few shot with tabular context
def dynamic_few_shot_with_infobox_as_context(df_sqls, question, context, Qtype, n_examples=6):
    
    similar_types_dict_int = {
      1: [27, 53, 14, 21, 32, 13],
      3: [71, 75, 27, 1, 38, 53],
      5: [3, 70, 75, 40, 68, 69],
      13: [53, 52, 1, 74, 96, 95],
      14: [74, 27, 1, 1002, 55, 38],
      19: [77, 35, 34, 78, 43, 75],
      21: [22, 1, 32, 30, 38, 71],
      22: [21, 38, 27, 39, 71, 1],
      27: [1, 14, 38, 74, 22, 52],
      30: [38, 35, 32, 36, 27, 21],
      32: [30, 21, 1, 38, 35, 27],
      34: [77, 19, 35, 43, 39, 78],
      35: [19, 30, 77, 34, 38, 32],
      36: [30, 60, 95, 96, 57, 59],
      38: [30, 27, 22, 65, 66, 35],
      39: [71, 34, 22, 65, 38, 78],
      40: [1, 14, 27, 32, 74, 21],
      43: [77, 34, 19, 52, 54, 22],
      44: [65, 39, 66, 38, 52, 22],
      52: [53, 54, 13, 74, 95, 27],
      53: [13, 52, 1, 74, 54, 27],
      54: [52, 53, 78, 38, 13, 65],
      55: [52, 95, 58, 14, 57, 59],
      57: [59, 58, 95, 96, 52, 66],
      58: [57, 59, 95, 96, 52, 13],
      59: [57, 58, 95, 96, 52, 13],
      60: [78, 36, 73, 96, 77, 95],
      64: [95, 59, 58, 96, 57, 36],
      65: [66, 38, 52, 39, 44, 96],
      66: [65, 38, 52, 57, 96, 58],
      68: [69, 70, 71, 32, 64, 3],
      69: [70, 68, 32, 1, 21, 71],
      70: [69, 68, 32, 1, 21, 30],
      71: [39, 21, 22, 65, 13, 53],
      73: [60, 78, 74, 53, 52, 13],
      74: [14, 53, 52, 27, 13, 1],
      75: [78, 77, 30, 19, 13, 53],
      77: [19, 78, 34, 35, 43, 75],
      78: [77, 75, 60, 19, 54, 73],
      95: [96, 58, 59, 57, 52, 13],
      96: [95, 59, 58, 57, 52, 13],
      1001: [1003, 1004, 1006, 14, 1, 27],
      1002: [14, 74, 1, 27, 1004, 95],
      1003: [1001, 1004, 1006, 1002, 14, 1],
      1004: [1006, 1002, 1003, 1001, 14, 27],
      1006: [1004, 1002, 1003, 14, 1001, 27],
      1016: [38, 14, 27, 30, 74, 36]

    }
    
    # Task Instruction and schema
    task_instruction = '''
Your task is to answer the given question based on the context provided and provide a well-reasoned response seperated by &&.

Instructions-
1. Only answer the question based on the infromation given in the context.
2. Provide the answer in a straigtforward manner and keep it within 1 to 10 words.
3. Respond with Yes/No in relevant questions.
4. Note an event is a combination of Tournament, Format and the corresponding year. For example:
    European Junior Championships | Girls' singles | 2009

6 Example Questions are given below with Context and Answers:'''

    # Initialize variable to store the result
    output_text = task_instruction + "\n\n"

    # Lookup the similar types for the given Qtype
    if Qtype in similar_types_dict_int:
        similar_types = similar_types_dict_int[Qtype]
    else:
        return f"No similar types found for Qtype: {Qtype}"

    # Filter the dataframe for rows matching the types in similar_types
    filtered_df = df_sqls[df_sqls['Types'].isin(similar_types)]

    # Ensure we only take up to 'n_examples' rows
    if len(filtered_df) > n_examples:
        filtered_df = filtered_df.iloc[:n_examples]

    # Generate and append the examples
    for i in range(len(filtered_df)):
        example_context = filtered_df.iloc[i]['Context']
        example_question = filtered_df.iloc[i]['Questions']
        example_answer = filtered_df.iloc[i]['Answers']
        output_text += f"Example {i + 1}:\nContext: {example_context}\nQuestion: {example_question}\nAnswer: {example_answer}\n\n"


    task = f'''
Please answer the following question based on the context provided and provide a well-reasoned response seperated by &&.

context : {context}

question : {question}

LLM answer: '''
    
    # Append the query instruction part
    output_text += task

    # Return the constructed text
    return output_text

# SQL Code Generation with Database Schema as Context and 6 static few shots
def sql_with_static_few_shot(question):
  return f"""
  # Task Instruction:
  You will be given a question and your task is to provide the SQL logic to answer a natural language question based on the provided schema. Six Example of the task is provided below. Assume that all the data is already inserted into the database.

  ## 1. Table Schemas:

  CREATE TABLE Athlete (
      athlete_id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100) NOT NULL
  );

  CREATE TABLE Tournament (
      tournament_id INT AUTO_INCREMENT PRIMARY KEY,
      athlete_id INT,
      name VARCHAR(100) NOT NULL,
      FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
  );

  CREATE TABLE Format (
      format_id INT AUTO_INCREMENT PRIMARY KEY,
      tournament_id INT,
      name VARCHAR(100) NOT NULL,
      FOREIGN KEY (tournament_id) REFERENCES Tournament(tournament_id)
  );

  CREATE TABLE Medal (
      medal_id INT AUTO_INCREMENT PRIMARY KEY,
      format_id INT,
      type VARCHAR(50) NOT NULL,
      year INT,
      location VARCHAR(100) NOT NULL,
      FOREIGN KEY (format_id) REFERENCES Format(format_id)
  );

  CREATE TABLE PersonalInformation (
      info_id INT AUTO_INCREMENT PRIMARY KEY,
      athlete_id INT,
      birth_year INT,
      birth_month INT,
      birth_day INT,
      FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
  );

  ## 2. Table Descriptions:

  describe athlete;
  +------------+--------------+------+-----+---------+----------------+
  | Field      | Type         | Null | Key | Default | Extra          |
  +------------+--------------+------+-----+---------+----------------+
  | athlete_id | int(11)      | NO   | PRI | NULL    | auto_increment |
  | name       | varchar(100) | NO   |     | NULL    |                |
  +------------+--------------+------+-----+---------+----------------+

  describe personalinformation;
  +-------------+---------+------+-----+---------+----------------+
  | Field       | Type    | Null | Key | Default | Extra          |
  +-------------+---------+------+-----+---------+----------------+
  | info_id     | int(11) | NO   | PRI | NULL    | auto_increment |
  | athlete_id  | int(11) | YES  | MUL | NULL    |                |
  | birth_year  | int(11) | YES  |     | NULL    |                |
  | birth_month | int(11) | YES  |     | NULL    |                |
  | birth_day   | int(11) | YES  |     | NULL    |                |
  +-------------+---------+------+-----+---------+----------------+

  describe tournament;
  +---------------+--------------+------+-----+---------+----------------+
  | Field         | Type         | Null | Key | Default | Extra          |
  +---------------+--------------+------+-----+---------+----------------+
  | tournament_id | int(11)      | NO   | PRI | NULL    | auto_increment |
  | athlete_id    | int(11)      | YES  | MUL | NULL    |                |
  | name          | varchar(100) | NO   |     | NULL    |                |
  +---------------+--------------+------+-----+---------+----------------+

  describe format;
  +---------------+--------------+------+-----+---------+----------------+
  | Field         | Type         | Null | Key | Default | Extra          |
  +---------------+--------------+------+-----+---------+----------------+
  | format_id     | int(11)      | NO   | PRI | NULL    | auto_increment |
  | tournament_id | int(11)      | YES  | MUL | NULL    |                |
  | name          | varchar(100) | NO   |     | NULL    |                |
  +---------------+--------------+------+-----+---------+----------------+

  describe medal;
  +-----------+--------------+------+-----+---------+----------------+
  | Field     | Type         | Null | Key | Default | Extra          |
  +-----------+--------------+------+-----+---------+----------------+
  | medal_id  | int(11)      | NO   | PRI | NULL    | auto_increment |
  | format_id | int(11)      | YES  | MUL | NULL    |                |
  | type      | varchar(50)  | NO   |     | NULL    |                |
  | year      | int(11)      | YES  |     | NULL    |                |
  | location  | varchar(100) | NO   |     | NULL    |                |
  +-----------+--------------+------+-----+---------+----------------+

  ## 3. Example Data:

  Athlete Table
  +------------+-----------------+
  | athlete_id | name            |
  +------------+-----------------+
  |         50 | Carolina Marín  |
  +------------+-----------------+

  PersonalInformation Table
  +---------+------------+------------+-------------+-----------+
  | info_id | athlete_id | birth_year | birth_month | birth_day |
  +---------+------------+------------+-------------+-----------+
  |      40 |         50 |       1993 |           6 |        15 |
  +---------+------------+------------+-------------+-----------+

  Tournament Table
  +---------------+------------+-------------------------------+
  | tournament_id | athlete_id | name                          |
  +---------------+------------+-------------------------------+
  |           281 |         50 | Olympic Games                 |
  |           282 |         50 | World Championships           |
  |           285 |         50 | European Women                |
  +---------------+------------+-------------------------------+

  Format Table
  +-----------+---------------+------------------+
  | format_id | tournament_id | name             |
  +-----------+---------------+------------------+
  |       392 |           281 | Women's singles  |
  |       393 |           282 | Women's singles  |
  |       396 |           285 | Women's team     |
  +-----------+---------------+------------------+

  Medal Table
  +----------+-----------+-------------+------+----------------+
  | medal_id | format_id | type        | year | location       |
  +----------+-----------+-------------+------+----------------+
  |      692 |       392 | MedalGold   | 2016 | Rio de Janeiro |
  |      696 |       393 | MedalSilver | 2023 | Copenhagen     |
  |      706 |       396 | MedalBronze | 2016 | Kazan          |
  +----------+-----------+-------------+------+----------------+


  ## Example 1:
  Question: How many Dressage World Cup appearances/wins does Charlotte Dujardin have ?
  SQL: SELECT
    COUNT(m.medal_id) AS total_wins
  FROM Medal m
  JOIN Format f ON m.format_id = f.format_id
  JOIN Tournament t ON f.tournament_id = t.tournament_id
  JOIN Athlete a ON t.athlete_id = a.athlete_id
  WHERE a.name = 'Charlotte Dujardin'
    AND t.name = 'Dressage World Cup'
    AND m.type = 'MedalGold';


  ## Example 2:
  Question: How many times has Douglas Brose won medals in Pan American Games ?
  SQL: SELECT COUNT(*) AS medal_count
  FROM Medal m
  JOIN Format f ON m.format_id = f.format_id
  JOIN Tournament t ON f.tournament_id = t.tournament_id
  JOIN Athlete a ON t.athlete_id = a.athlete_id
  WHERE a.name = 'Douglas Brose'
    AND t.name = 'Pan American Games';

  ## Example 3:
  Question: How many years passed between Christian Coleman's first and most recent International medal ?
  SQL: SELECT MAX(m.year) - MIN(m.year) AS years_passed
  FROM Medal m
  JOIN Format f ON m.format_id = f.format_id
  JOIN Tournament t ON f.tournament_id = t.tournament_id
  JOIN Athlete a ON t.athlete_id = a.athlete_id
  WHERE a.name = 'Christian Coleman';

  ## Example 4:
  Question: In which year(s) did Tomokazu Harimoto win the lowest number of medals during their career ?
  SQL: SELECT m.year
  FROM Medal m
  JOIN Format f ON m.format_id = f.format_id
  JOIN Tournament t ON f.tournament_id = t.tournament_id
  JOIN Athlete a ON t.athlete_id = a.athlete_id
  WHERE a.name = 'Tomokazu Harimoto'
  GROUP BY m.year
  HAVING COUNT(m.medal_id) = (
      SELECT MIN(medal_count)
      FROM (
          SELECT COUNT(m2.medal_id) AS medal_count
          FROM Medal m2
          JOIN Athlete a2 ON m2.format_id = a2.athlete_id
          WHERE a2.name = 'Tomokazu Harimoto'
          GROUP BY m2.year
      ) AS yearly_medal_counts
  );

  ## Example 5:
  Question: Which tournament(s) has Angelo Crescenzo won the most Bronze Medals in ?
  SQL: SELECT t.name AS tournament_name, m.year
  FROM Medal m
  JOIN Format f ON m.format_id = f.format_id
  JOIN Tournament t ON f.tournament_id = t.tournament_id
  JOIN Athlete a ON t.athlete_id = a.athlete_id
  WHERE a.name = 'Angelo Crescenzo'
    AND m.type = 'MedalBronze'
  GROUP BY t.name, m.year
  HAVING COUNT(m.medal_id) = (
      SELECT MAX(bronze_medal_count)
      FROM (
          SELECT COUNT(m2.medal_id) AS bronze_medal_count
          FROM Medal m2
          JOIN Format f2 ON m2.format_id = f2.format_id
          JOIN Tournament t2 ON f2.tournament_id = t2.tournament_id
          JOIN Athlete a2 ON t2.athlete_id = a2.athlete_id
          WHERE a2.name = 'Angelo Crescenzo'
            AND m2.type = 'MedalBronze'
          GROUP BY t2.name, m2.year
      ) AS medal_counts
  );


  ## Example 6:
  Question: Does Rubén Limardo have more Silver Medals than Bronze Medals in Team ?
  SQL: SELECT CASE
      WHEN SUM(CASE WHEN m.type = 'MedalSilver' THEN 1 ELSE 0 END) >
          SUM(CASE WHEN m.type = 'MedalBronze' THEN 1 ELSE 0 END)
      THEN 'Yes'
      ELSE 'No'
  END AS has_more_silver_than_bronze
  FROM Medal m
  JOIN Format f ON m.format_id = f.format_id
  JOIN Tournament t ON f.tournament_id = t.tournament_id
  JOIN Athlete a ON t.athlete_id = a.athlete_id
  WHERE a.name = 'Rubén Limardo'
    AND f.name LIKE '%Team%';


  Please use the following instructions while writing the query:
  1. If a question can have multiple answers, do not limit the response to only one. Instead, output all possible answers.
  2. Use the column names as specified in the schema to find the necessary parameters for the query (e.g., athlete name, tournament, format, year, medal type).
  3. An event is a combination of Tournament, Format and the corresponding year. For example:
  +-------------------------------+------------------+------------+
  | European Junior Championships | Girls' singles   |       2009 |
  | World Junior Championships    | Girls' singles   |       2011 |
  +-------------------------------+------------------+------------+
  4. There are three types of medals in the Medal Table: MedalGold, MedalSilver, MedalBronze.
  5. Write one single combined query as the response.
      
  Please generate the SQL logic for the following question assuming that the data is inserted into a database.

  Question : {question}

  LLM SQL Logic: """  

# SQL Code Generation with Database Schema as Context and 0 shots
def sql_with_zero_shot(question):
  return f"""
  # Task Instruction:
  You will be given a question and your task is to provide the SQL logic to answer a natural language question based on the provided schema. One Example of the task is provided below. Assume that all the data is already inserted into the database.

  ## 1. Table Schemas:

  CREATE TABLE Athlete (
      athlete_id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100) NOT NULL
  );

  CREATE TABLE Tournament (
      tournament_id INT AUTO_INCREMENT PRIMARY KEY,
      athlete_id INT,
      name VARCHAR(100) NOT NULL,
      FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
  );

  CREATE TABLE Format (
      format_id INT AUTO_INCREMENT PRIMARY KEY,
      tournament_id INT,
      name VARCHAR(100) NOT NULL,
      FOREIGN KEY (tournament_id) REFERENCES Tournament(tournament_id)
  );

  CREATE TABLE Medal (
      medal_id INT AUTO_INCREMENT PRIMARY KEY,
      format_id INT,
      type VARCHAR(50) NOT NULL,
      year INT,
      location VARCHAR(100) NOT NULL,
      FOREIGN KEY (format_id) REFERENCES Format(format_id)
  );

  CREATE TABLE PersonalInformation (
      info_id INT AUTO_INCREMENT PRIMARY KEY,
      athlete_id INT,
      birth_year INT,
      birth_month INT,
      birth_day INT,
      FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
  );

  ## 2. Table Descriptions:

  describe athlete;
  +------------+--------------+------+-----+---------+----------------+
  | Field      | Type         | Null | Key | Default | Extra          |
  +------------+--------------+------+-----+---------+----------------+
  | athlete_id | int(11)      | NO   | PRI | NULL    | auto_increment |
  | name       | varchar(100) | NO   |     | NULL    |                |
  +------------+--------------+------+-----+---------+----------------+

  describe personalinformation;
  +-------------+---------+------+-----+---------+----------------+
  | Field       | Type    | Null | Key | Default | Extra          |
  +-------------+---------+------+-----+---------+----------------+
  | info_id     | int(11) | NO   | PRI | NULL    | auto_increment |
  | athlete_id  | int(11) | YES  | MUL | NULL    |                |
  | birth_year  | int(11) | YES  |     | NULL    |                |
  | birth_month | int(11) | YES  |     | NULL    |                |
  | birth_day   | int(11) | YES  |     | NULL    |                |
  +-------------+---------+------+-----+---------+----------------+

  describe tournament;
  +---------------+--------------+------+-----+---------+----------------+
  | Field         | Type         | Null | Key | Default | Extra          |
  +---------------+--------------+------+-----+---------+----------------+
  | tournament_id | int(11)      | NO   | PRI | NULL    | auto_increment |
  | athlete_id    | int(11)      | YES  | MUL | NULL    |                |
  | name          | varchar(100) | NO   |     | NULL    |                |
  +---------------+--------------+------+-----+---------+----------------+

  describe format;
  +---------------+--------------+------+-----+---------+----------------+
  | Field         | Type         | Null | Key | Default | Extra          |
  +---------------+--------------+------+-----+---------+----------------+
  | format_id     | int(11)      | NO   | PRI | NULL    | auto_increment |
  | tournament_id | int(11)      | YES  | MUL | NULL    |                |
  | name          | varchar(100) | NO   |     | NULL    |                |
  +---------------+--------------+------+-----+---------+----------------+

  describe medal;
  +-----------+--------------+------+-----+---------+----------------+
  | Field     | Type         | Null | Key | Default | Extra          |
  +-----------+--------------+------+-----+---------+----------------+
  | medal_id  | int(11)      | NO   | PRI | NULL    | auto_increment |
  | format_id | int(11)      | YES  | MUL | NULL    |                |
  | type      | varchar(50)  | NO   |     | NULL    |                |
  | year      | int(11)      | YES  |     | NULL    |                |
  | location  | varchar(100) | NO   |     | NULL    |                |
  +-----------+--------------+------+-----+---------+----------------+

  Please use the following instructions while writing the query:
  1. If a question can have multiple answers, do not limit the response to only one. Instead, output all possible answers.
  2. Use the column names as specified in the schema to find the necessary parameters for the query (e.g., athlete name, tournament, format, year, medal type).
  3. An event is a combination of Tournament, Format and the corresponding year. For example:
  +-------------------------------+------------------+------------+
  | European Junior Championships | Girls' singles   |       2009 |
  | World Junior Championships    | Girls' singles   |       2011 |
  +-------------------------------+------------------+------------+
  4. There are three types of medals in the Medal Table: MedalGold, MedalSilver, MedalBronze.
  5. Write one single combined query as the response.
  6. Please output only the SQL Query and no other comments.
      
  Please generate the SQL logic for the following question assuming that the data is inserted into a database.

  Question : {question}

  LLM SQL Logic: """  
  
# SQL Code Generation with 6 Dynamic Generated Few shots
def sql_with_dynamic_few_shot(df_sqls, question, Qtype, n_examples=6):
    
    similar_types_dict_int = {
      1: [27, 53, 14, 21, 32, 13],
      3: [71, 75, 27, 1, 38, 53],
      5: [3, 70, 75, 40, 68, 69],
      13: [53, 52, 1, 74, 96, 95],
      14: [74, 27, 1, 1002, 55, 38],
      19: [77, 35, 34, 78, 43, 75],
      21: [22, 1, 32, 30, 38, 71],
      22: [21, 38, 27, 39, 71, 1],
      27: [1, 14, 38, 74, 22, 52],
      30: [38, 35, 32, 36, 27, 21],
      32: [30, 21, 1, 38, 35, 27],
      34: [77, 19, 35, 43, 39, 78],
      35: [19, 30, 77, 34, 38, 32],
      36: [30, 60, 95, 96, 57, 59],
      38: [30, 27, 22, 65, 66, 35],
      39: [71, 34, 22, 65, 38, 78],
      40: [1, 14, 27, 32, 74, 21],
      43: [77, 34, 19, 52, 54, 22],
      44: [65, 39, 66, 38, 52, 22],
      52: [53, 54, 13, 74, 95, 27],
      53: [13, 52, 1, 74, 54, 27],
      54: [52, 53, 78, 38, 13, 65],
      55: [52, 95, 58, 14, 57, 59],
      57: [59, 58, 95, 96, 52, 66],
      58: [57, 59, 95, 96, 52, 13],
      59: [57, 58, 95, 96, 52, 13],
      60: [78, 36, 73, 96, 77, 95],
      64: [95, 59, 58, 96, 57, 36],
      65: [66, 38, 52, 39, 44, 96],
      66: [65, 38, 52, 57, 96, 58],
      68: [69, 70, 71, 32, 64, 3],
      69: [70, 68, 32, 1, 21, 71],
      70: [69, 68, 32, 1, 21, 30],
      71: [39, 21, 22, 65, 13, 53],
      73: [60, 78, 74, 53, 52, 13],
      74: [14, 53, 52, 27, 13, 1],
      75: [78, 77, 30, 19, 13, 53],
      77: [19, 78, 34, 35, 43, 75],
      78: [77, 75, 60, 19, 54, 73],
      95: [96, 58, 59, 57, 52, 13],
      96: [95, 59, 58, 57, 52, 13],
      1001: [1003, 1004, 1006, 14, 1, 27],
      1002: [14, 74, 1, 27, 1004, 95],
      1003: [1001, 1004, 1006, 1002, 14, 1],
      1004: [1006, 1002, 1003, 1001, 14, 27],
      1006: [1004, 1002, 1003, 14, 1001, 27],
      1016: [38, 14, 27, 30, 74, 36]

    }
    
    # Task Instruction and schema
    schema_instruction = '''
    # Task Instruction:
    You will be given a question and your task is to provide the SQL logic to answer a natural language question based on the provided schema. Few Examples of the task will be provided below. Assume that all the data is already inserted into the database.

    ## 1. Table Schemas:

    CREATE TABLE Athlete (
        athlete_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );

    CREATE TABLE Tournament (
        tournament_id INT AUTO_INCREMENT PRIMARY KEY,
        athlete_id INT,
        name VARCHAR(100) NOT NULL,
        FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
    );

    CREATE TABLE Format (
        format_id INT AUTO_INCREMENT PRIMARY KEY,
        tournament_id INT,
        name VARCHAR(100) NOT NULL,
        FOREIGN KEY (tournament_id) REFERENCES Tournament(tournament_id)
    );

    CREATE TABLE Medal (
        medal_id INT AUTO_INCREMENT PRIMARY KEY,
        format_id INT,
        type VARCHAR(50) NOT NULL,
        year INT,
        location VARCHAR(100) NOT NULL,
        FOREIGN KEY (format_id) REFERENCES Format(format_id)
    );

    CREATE TABLE PersonalInformation (
        info_id INT AUTO_INCREMENT PRIMARY KEY,
        athlete_id INT,
        birth_year INT,
        birth_month INT,
        birth_day INT,
        FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
    );

    ## 2. Table Descriptions:

    describe athlete;
    +------------+--------------+------+-----+---------+----------------+
    | Field      | Type         | Null | Key | Default | Extra          |
    +------------+--------------+------+-----+---------+----------------+
    | athlete_id | int(11)      | NO   | PRI | NULL    | auto_increment |
    | name       | varchar(100) | NO   |     | NULL    |                |
    +------------+--------------+------+-----+---------+----------------+

    describe personalinformation;
    +-------------+---------+------+-----+---------+----------------+
    | Field       | Type    | Null | Key | Default | Extra          |
    +-------------+---------+------+-----+---------+----------------+
    | info_id     | int(11) | NO   | PRI | NULL    | auto_increment |
    | athlete_id  | int(11) | YES  | MUL | NULL    |                |
    | birth_year  | int(11) | YES  |     | NULL    |                |
    | birth_month | int(11) | YES  |     | NULL    |                |
    | birth_day   | int(11) | YES  |     | NULL    |                |
    +-------------+---------+------+-----+---------+----------------+

    describe tournament;
    +---------------+--------------+------+-----+---------+----------------+
    | Field         | Type         | Null | Key | Default | Extra          |
    +---------------+--------------+------+-----+---------+----------------+
    | tournament_id | int(11)      | NO   | PRI | NULL    | auto_increment |
    | athlete_id    | int(11)      | YES  | MUL | NULL    |                |
    | name          | varchar(100) | NO   |     | NULL    |                |
    +---------------+--------------+------+-----+---------+----------------+

    describe format;
    +---------------+--------------+------+-----+---------+----------------+
    | Field         | Type         | Null | Key | Default | Extra          |
    +---------------+--------------+------+-----+---------+----------------+
    | format_id     | int(11)      | NO   | PRI | NULL    | auto_increment |
    | tournament_id | int(11)      | YES  | MUL | NULL    |                |
    | name          | varchar(100) | NO   |     | NULL    |                |
    +---------------+--------------+------+-----+---------+----------------+

    describe medal;
    +-----------+--------------+------+-----+---------+----------------+
    | Field     | Type         | Null | Key | Default | Extra          |
    +-----------+--------------+------+-----+---------+----------------+
    | medal_id  | int(11)      | NO   | PRI | NULL    | auto_increment |
    | format_id | int(11)      | YES  | MUL | NULL    |                |
    | type      | varchar(50)  | NO   |     | NULL    |                |
    | year      | int(11)      | YES  |     | NULL    |                |
    | location  | varchar(100) | NO   |     | NULL    |                |
    +-----------+--------------+------+-----+---------+----------------+

    ## 3. Example Data:

    Athlete Table
    +------------+-----------------+
    | athlete_id | name            |
    +------------+-----------------+
    |         50 | Carolina Marín  |
    +------------+-----------------+

    PersonalInformation Table
    +---------+------------+------------+-------------+-----------+
    | info_id | athlete_id | birth_year | birth_month | birth_day |
    +---------+------------+------------+-------------+-----------+
    |      40 |         50 |       1993 |           6 |        15 |
    +---------+------------+------------+-------------+-----------+

    Tournament Table
    +---------------+------------+-------------------------------+
    | tournament_id | athlete_id | name                          |
    +---------------+------------+-------------------------------+
    |           281 |         50 | Olympic Games                 |
    |           282 |         50 | World Championships           |
    |           285 |         50 | European Women                |
    +---------------+------------+-------------------------------+

    Format Table
    +-----------+---------------+------------------+
    | format_id | tournament_id | name             |
    +-----------+---------------+------------------+
    |       392 |           281 | Women's singles  |
    |       393 |           282 | Women's singles  |
    |       396 |           285 | Women's team     |
    +-----------+---------------+------------------+

    Medal Table
    +----------+-----------+-------------+------+----------------+
    | medal_id | format_id | type        | year | location       |
    +----------+-----------+-------------+------+----------------+
    |      692 |       392 | MedalGold   | 2016 | Rio de Janeiro |
    |      696 |       393 | MedalSilver | 2023 | Copenhagen     |
    |      706 |       396 | MedalBronze | 2016 | Kazan          |
    +----------+-----------+-------------+------+----------------+
    '''

    # Initialize variable to store the result
    output_text = schema_instruction + "\n\n"

    # Lookup the similar types for the given Qtype
    if Qtype in similar_types_dict_int:
        similar_types = similar_types_dict_int[Qtype]
    else:
        return f"No similar types found for Qtype: {Qtype}"

    # Filter the dataframe for rows matching the types in similar_types
    filtered_df = df_sqls[df_sqls['Types'].isin(similar_types)]

    # Ensure we only take up to 'n_examples' rows
    if len(filtered_df) > n_examples:
        filtered_df = filtered_df.iloc[:n_examples]

    # Generate and append the examples
    for i in range(len(filtered_df)):
        example_question = filtered_df.iloc[i]['Questions']
        example_sql = filtered_df.iloc[i]['SQL']
        output_text += f"Example {i + 1}:\nQuestion: {example_question}\nSQL: {example_sql}\n\n"


        # Additional SQL query instructions
    query_instruction = f'''
    Please use the following instructions while writing the query:
    1. If a question can have multiple answers, do not limit the response to only one. Instead, output all possible answers.
    2. Use the column names as specified in the schema to find the necessary parameters for the query (e.g., athlete name, tournament, format, year, medal type).
    3. An event is a combination of Tournament, Format, and the corresponding year. For example:
    +-------------------------------+------------------+------------+
    | European Junior Championships | Girls' singles   |       2009 |
    | World Junior Championships    | Girls' singles   |       2011 |
    +-------------------------------+------------------+------------+
    4. There are three types of medals in the Medal Table: MedalGold, MedalSilver, MedalBronze.
    5. Write one single combined query as the response.

    Please generate the SQL logic for the following question assuming that the data is inserted into a database.

    Question: {question}

    LLM SQL Logic:
    '''
    
    # Append the query instruction part
    output_text += query_instruction

    # Return the constructed text
    return output_text

def faithful_cot(context, question):
    example_code = """
    # To answer this question, write a Python program to answer the following subquestions:
    # 1. In which year did Áron Szilágyi win each gold medal?
    gold_medals = [
        {"year": 2007, "count": 1},  # World Championships - Team
        {"year": 2012, "count": 1},  # Olympic Games - Individual
        {"year": 2015, "count": 1},  # European Championships - Individual
        {"year": 2016, "count": 1},  # Olympic Games - Individual
        {"year": 2018, "count": 1},  # European Championships - Team
        {"year": 2020, "count": 1},  # Olympic Games - Individual
        {"year": 2022, "count": 2},  # World Championships - Individual, European Championships - Team
        {"year": 2023, "count": 1},  # World Championships - Team
        {"year": 2024, "count": 1}   # European Championships - Team
    ]

    # 2. How many gold medals did Áron Szilágyi win each year?
    medal_counts = {}
    for medal in gold_medals:
        year = medal["year"]
        count = medal["count"]
        if year not in medal_counts:
            medal_counts[year] = 0
        medal_counts[year] += count

    # 3. Which year had the highest count of gold medals?
    highest_year = max(medal_counts, key=medal_counts.get)
    highest_count = medal_counts[highest_year]

    # 4. Final Answer: In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?
    answer = highest_year

    return answer
    """

    return f"""
    Given an entity-centric table and corresponding question, answer the question by providing step-by-step reasoning.
    Each table-question pair is presented as a table (identified by "Table:") followed by a question (identified by "Q:"). Tables are presented in a linear format.
    One example is given below:
    
    Table:
    Áron Szilágyi

    Personal Information
    Birth Date
    1990-1-14        

    Birth Place
    Budapest        

    Height
    1.80 m        

    Weight
    78  kg        

    Coach
    András Decsi        
    Béla Somlai, György Gerevich        

    Country Representing: HUN
    Olympic Games
    Individual        MedalGold | 2012 | London, MedalGold | 2016 | Rio de Janeiro, MedalGold | 2020 | Tokyo
    Team        MedalBronze | 2020 | Tokyo

    World Championships
    Team        MedalGold | 2007 | Saint Petersburg, MedalGold | 2023 | Milan, MedalSilver | 2016 | Rio de Janeiro, MedalSilver | 2017 | Leipzig, MedalSilver | 2019 | Budapest, MedalSilver | 2022 | Cairo, MedalBronze | 2009 | Antalya, MedalBronze | 2014 | Kazan, MedalBronze | 2018 | Wuxi
    Individual        MedalGold | 2022 | Cairo, MedalBronze | 2013 | Budapest, MedalBronze | 2023 | Milan

    European Games
    Individual        MedalBronze | 2023 | Kraków

    European Championships
    Individual        MedalGold | 2015 | Montreux, MedalSilver | 2017 | Tbilisi, MedalBronze | 2011 | Sheffield
    Team        MedalGold | 2018 | Novi Sad, MedalGold | 2022 | Antalya, MedalGold | 2024 | Basel, MedalSilver | 2013 | Zagreb, MedalSilver | 2019 | Düsseldorf, MedalBronze | 2015 | Montreux, MedalBronze | 2017 | Tbilisi
    
    Q: In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?
    
    Answer:
    {example_code}
    ========================
    
    Table: {context}
    Q : {question}
    
    LLM Answer:
    # To answer this question, write a Python program to answer the following subquestions:
    # 1. 
    """
    

context = '''
Áron Szilágyi

Personal Information
Birth Date
1990-1-14        

Birth Place
Budapest        

Height
1.80 m        

Weight
78  kg        

Coach
András Decsi        
Béla Somlai, György Gerevich        

Country Representing: HUN
Olympic Games
Individual        MedalGold | 2012 | London, MedalGold | 2016 | Rio de Janeiro, MedalGold | 2020 | Tokyo
Team        MedalBronze | 2020 | Tokyo

World Championships
Team        MedalGold | 2007 | Saint Petersburg, MedalGold | 2023 | Milan, MedalSilver | 2016 | Rio de Janeiro, MedalSilver | 2017 | Leipzig, MedalSilver | 2019 | Budapest, MedalSilver | 2022 | Cairo, MedalBronze | 2009 | Antalya, MedalBronze | 2014 | Kazan, MedalBronze | 2018 | Wuxi
Individual        MedalGold | 2022 | Cairo, MedalBronze | 2013 | Budapest, MedalBronze | 2023 | Milan

European Games
Individual        MedalBronze | 2023 | Kraków

European Championships
Individual        MedalGold | 2015 | Montreux, MedalSilver | 2017 | Tbilisi, MedalBronze | 2011 | Sheffield
Team        MedalGold | 2018 | Novi Sad, MedalGold | 2022 | Antalya, MedalGold | 2024 | Basel, MedalSilver | 2013 | Zagreb, MedalSilver | 2019 | Düsseldorf, MedalBronze | 2015 | Montreux, MedalBronze | 2017 | Tbilisi

'''

def pot(context, question):
    example_code = """
    # To answer this question, write a Python program to answer the following question:
    gold_medals = [
        {"year": 2007, "count": 1},  # World Championships - Team
        {"year": 2012, "count": 1},  # Olympic Games - Individual
        {"year": 2015, "count": 1},  # European Championships - Individual
        {"year": 2016, "count": 1},  # Olympic Games - Individual
        {"year": 2018, "count": 1},  # European Championships - Team
        {"year": 2020, "count": 1},  # Olympic Games - Individual
        {"year": 2022, "count": 2},  # World Championships - Individual, European Championships - Team
        {"year": 2023, "count": 1},  # World Championships - Team
        {"year": 2024, "count": 1}   # European Championships - Team
    ]

    medal_counts = {}
    for medal in gold_medals:
        year = medal["year"]
        count = medal["count"]
        if year not in medal_counts:
            medal_counts[year] = 0
        medal_counts[year] += count

    highest_year = max(medal_counts, key=medal_counts.get)
    highest_count = medal_counts[highest_year]

    answer = highest_year

    return answer
    """

    return f"""
    Given an entity-centric table and corresponding question, answer the question by providing step-by-step reasoning.
    Each table-question pair is presented as a table (identified by "Table:") followed by a question (identified by "Q:"). Tables are presented in a linear format.
    One example is given below:
    
    Table:
    Áron Szilágyi

    Personal Information
    Birth Date
    1990-1-14        

    Birth Place
    Budapest        

    Height
    1.80 m        

    Weight
    78  kg        

    Coach
    András Decsi        
    Béla Somlai, György Gerevich        

    Country Representing: HUN
    Olympic Games
    Individual        MedalGold | 2012 | London, MedalGold | 2016 | Rio de Janeiro, MedalGold | 2020 | Tokyo
    Team        MedalBronze | 2020 | Tokyo

    World Championships
    Team        MedalGold | 2007 | Saint Petersburg, MedalGold | 2023 | Milan, MedalSilver | 2016 | Rio de Janeiro, MedalSilver | 2017 | Leipzig, MedalSilver | 2019 | Budapest, MedalSilver | 2022 | Cairo, MedalBronze | 2009 | Antalya, MedalBronze | 2014 | Kazan, MedalBronze | 2018 | Wuxi
    Individual        MedalGold | 2022 | Cairo, MedalBronze | 2013 | Budapest, MedalBronze | 2023 | Milan

    European Games
    Individual        MedalBronze | 2023 | Kraków

    European Championships
    Individual        MedalGold | 2015 | Montreux, MedalSilver | 2017 | Tbilisi, MedalBronze | 2011 | Sheffield
    Team        MedalGold | 2018 | Novi Sad, MedalGold | 2022 | Antalya, MedalGold | 2024 | Basel, MedalSilver | 2013 | Zagreb, MedalSilver | 2019 | Düsseldorf, MedalBronze | 2015 | Montreux, MedalBronze | 2017 | Tbilisi
    
    Q: In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?
    
    Answer:
    {example_code}
    ========================
    
    Table: {context}
    Q : {question}
    
    LLM Answer:
    # To answer this question, write a Python program to answer the following question:

    """

def clear(context, question):
    return f"""
    Given an entity-centric table and corresponding question, follow the steps below exactly to answer the question:

    Step 1. Comprehend Information: Apply domain knowledge to understand how to approach and answer the question.

    Step 2. Locate Relevant Rows: Identify and extract any rows from the table that could be relevant to the question. Explain why these rows are selected. Also output the relevant rows verbatim.

    Step 3. Examine the Question and Create Sub-Questions: Determine whether the original question can be solved by a simple table lookup. If not, break down the original question into between 2 and 4 smaller, more manageable sub-questions. Assume each sub-problem can be solved using the provided evidence. Explain how one could approach solving each sub-problem.

    Step 4. Answer Sub-Questions: Answer each sub-question using evidence from the table. Explain the step-by-step reasoning process that leads to each answer. Include any calculations or logical deduction to arrive at each conclusion, no matter how simple.

    Step 5. Resolve Information to Form the Final Answer: Using the answers to each sub-question, answer the original question. Explain the step-by-step reasoning process that leads to this final answer. Include any calculations or logical deduction to arrive at each conclusion, no matter how simple. Clearly state the final answer using "Final Answer:", providing the answer as concisely as possible without unnecessary information.


    Each table-question pair is presented as a table (identified by "Table:") followed by a question (identified by "Q:"). Tables are presented in a linear format.

    ========================
    Table:
    Áron Szilágyi

    Personal Information
    Birth Date
    1990-1-14        

    Birth Place
    Budapest        

    Height
    1.80 m        

    Weight
    78  kg        

    Coach
    András Decsi        
    Béla Somlai, György Gerevich        

    Country Representing: HUN
    Olympic Games
    Individual        MedalGold | 2012 | London, MedalGold | 2016 | Rio de Janeiro, MedalGold | 2020 | Tokyo
    Team        MedalBronze | 2020 | Tokyo

    World Championships
    Team        MedalGold | 2007 | Saint Petersburg, MedalGold | 2023 | Milan, MedalSilver | 2016 | Rio de Janeiro, MedalSilver | 2017 | Leipzig, MedalSilver | 2019 | Budapest, MedalSilver | 2022 | Cairo, MedalBronze | 2009 | Antalya, MedalBronze | 2014 | Kazan, MedalBronze | 2018 | Wuxi
    Individual        MedalGold | 2022 | Cairo, MedalBronze | 2013 | Budapest, MedalBronze | 2023 | Milan

    European Games
    Individual        MedalBronze | 2023 | Kraków

    European Championships
    Individual        MedalGold | 2015 | Montreux, MedalSilver | 2017 | Tbilisi, MedalBronze | 2011 | Sheffield
    Team        MedalGold | 2018 | Novi Sad, MedalGold | 2022 | Antalya, MedalGold | 2024 | Basel, MedalSilver | 2013 | Zagreb, MedalSilver | 2019 | Düsseldorf, MedalBronze | 2015 | Montreux, MedalBronze | 2017 | Tbilisi
    
    Q: In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?
    
    A:
    
    Step 1. Comprehend Information  
    - The question asks for the year in which Áron Szilágyi won the most gold medals.  
    - To solve this, count the number of gold medals won in each year across all competitions (Olympics, World Championships, European Championships, and other events). Identify the year with the highest count.

    ---

    Step 2. Locate Relevant Rows  
    Relevant rows include all entries for gold medals in the table, as they provide information about the years and events in which Szilágyi won gold medals:  
    1. **Olympic Games (Individual)**: Gold - 2012 (London), Gold - 2016 (Rio de Janeiro), Gold - 2020 (Tokyo).  
    2. **World Championships (Team)**: Gold - 2007 (Saint Petersburg), Gold - 2023 (Milan).  
    3. **World Championships (Individual)**: Gold - 2022 (Cairo).  
    4. **European Championships (Team)**: Gold - 2018 (Novi Sad), Gold - 2022 (Antalya), Gold - 2024 (Basel).  
    5. **European Championships (Individual)**: Gold - 2015 (Montreux).

    ---

    Step 3. Examine the Question and Create Sub-Questions  
    The question cannot be answered by a single table lookup, so it is broken into manageable sub-questions:  
    **OQ) In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?**  

    **Sub-Questions:**  
    1. How many gold medals did Szilágyi win in each year?  
    2. Which year has the highest count of gold medals?

    ---

    Step 4. Answer Sub-Questions  

    **SQ1) How many gold medals did Szilágyi win in each year?**  
    - **2007**: 1 gold (World Championships - Team).  
    - **2012**: 1 gold (Olympic Games - Individual).  
    - **2015**: 1 gold (European Championships - Individual).  
    - **2016**: 1 gold (Olympic Games - Individual).  
    - **2018**: 1 gold (European Championships - Team).  
    - **2020**: 1 gold (Olympic Games - Individual).  
    - **2022**: 2 golds (World Championships - Individual; European Championships - Team).  
    - **2023**: 1 gold (World Championships - Team).  
    - **2024**: 1 gold (European Championships - Team).  

    **SQ2) Which year has the highest count of gold medals?**  
    - From SQ1, the year **2022** has 2 gold medals, the highest number of gold medals won in a single year.  

    ---

    Step 5. Resolve Information to Form the Final Answer  
    **OQ) In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?**  
    From SQ2, the year 2022 has the highest count of gold medals (2 gold medals).  

    Final Answer: 2022
    
    ========================
    Table : {context}

    Q : {question}
    
    LLM answer: """
    
    
def chain_of_thought(context, question):
    return f"""
    Given an entity-centric table and corresponding question, answer the question by providing step-by-step reasoning and then clearly and concisely stating the final answer using "Final Answer:".

    Each table-question pair is presented as a table (identified by "Table:") followed by a question (identified by "Q:"). Tables are presented in a linear format.

    Table:
    Áron Szilágyi

    Personal Information
    Birth Date
    1990-1-14        

    Birth Place
    Budapest        

    Height
    1.80 m        

    Weight
    78  kg        

    Coach
    András Decsi        
    Béla Somlai, György Gerevich        

    Country Representing: HUN
    Olympic Games
    Individual        MedalGold | 2012 | London, MedalGold | 2016 | Rio de Janeiro, MedalGold | 2020 | Tokyo
    Team        MedalBronze | 2020 | Tokyo

    World Championships
    Team        MedalGold | 2007 | Saint Petersburg, MedalGold | 2023 | Milan, MedalSilver | 2016 | Rio de Janeiro, MedalSilver | 2017 | Leipzig, MedalSilver | 2019 | Budapest, MedalSilver | 2022 | Cairo, MedalBronze | 2009 | Antalya, MedalBronze | 2014 | Kazan, MedalBronze | 2018 | Wuxi
    Individual        MedalGold | 2022 | Cairo, MedalBronze | 2013 | Budapest, MedalBronze | 2023 | Milan

    European Games
    Individual        MedalBronze | 2023 | Kraków

    European Championships
    Individual        MedalGold | 2015 | Montreux, MedalSilver | 2017 | Tbilisi, MedalBronze | 2011 | Sheffield
    Team        MedalGold | 2018 | Novi Sad, MedalGold | 2022 | Antalya, MedalGold | 2024 | Basel, MedalSilver | 2013 | Zagreb, MedalSilver | 2019 | Düsseldorf, MedalBronze | 2015 | Montreux, MedalBronze | 2017 | Tbilisi
    
    Q: In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?
    
    A:  
    Let's think step by step:
    1. Identify all the years Áron Szilágyi won gold medals across all competitions:
    - **Olympic Games (Individual)**: Gold - 2012 (London), Gold - 2016 (Rio de Janeiro), Gold - 2020 (Tokyo).
    - **World Championships (Team)**: Gold - 2007 (Saint Petersburg), Gold - 2023 (Milan).
    - **World Championships (Individual)**: Gold - 2022 (Cairo).
    - **European Championships (Team)**: Gold - 2018 (Novi Sad), Gold - 2022 (Antalya), Gold - 2024 (Basel).
    - **European Championships (Individual)**: Gold - 2015 (Montreux).

    2. Count the gold medals won in each year:
    - **2007**: 1 gold (World Championships - Team).
    - **2012**: 1 gold (Olympic Games - Individual).
    - **2015**: 1 gold (European Championships - Individual).
    - **2016**: 1 gold (Olympic Games - Individual).
    - **2018**: 1 gold (European Championships - Team).
    - **2020**: 1 gold (Olympic Games - Individual).
    - **2022**: 2 golds (World Championships - Individual; European Championships - Team).
    - **2023**: 1 gold (World Championships - Team).
    - **2024**: 1 gold (European Championships - Team).

    3. Determine which year has the highest count of gold medals:
    - **2022** has the highest number of gold medals with 2.

    Final Answer: 2022
    
    ========================
    Table : {context}

    Q : {question}
    
    LLM answer: """
    
def plan_and_solve(context, question):
    return f"""
    Given an entity-centric table and corresponding question, answer the question by providing step-by-step reasoning and then clearly and concisely stating the final answer using "Final Answer:".

    Each table-question pair is presented as a table (identified by "Table:") followed by a question (identified by "Q:"). Tables are presented in a linear format.

    Table:
    Áron Szilágyi

    Personal Information
    Birth Date
    1990-1-14        

    Birth Place
    Budapest        

    Height
    1.80 m        

    Weight
    78  kg        

    Coach
    András Decsi        
    Béla Somlai, György Gerevich        

    Country Representing: HUN
    Olympic Games
    Individual        MedalGold | 2012 | London, MedalGold | 2016 | Rio de Janeiro, MedalGold | 2020 | Tokyo
    Team        MedalBronze | 2020 | Tokyo

    World Championships
    Team        MedalGold | 2007 | Saint Petersburg, MedalGold | 2023 | Milan, MedalSilver | 2016 | Rio de Janeiro, MedalSilver | 2017 | Leipzig, MedalSilver | 2019 | Budapest, MedalSilver | 2022 | Cairo, MedalBronze | 2009 | Antalya, MedalBronze | 2014 | Kazan, MedalBronze | 2018 | Wuxi
    Individual        MedalGold | 2022 | Cairo, MedalBronze | 2013 | Budapest, MedalBronze | 2023 | Milan

    European Games
    Individual        MedalBronze | 2023 | Kraków

    European Championships
    Individual        MedalGold | 2015 | Montreux, MedalSilver | 2017 | Tbilisi, MedalBronze | 2011 | Sheffield
    Team        MedalGold | 2018 | Novi Sad, MedalGold | 2022 | Antalya, MedalGold | 2024 | Basel, MedalSilver | 2013 | Zagreb, MedalSilver | 2019 | Düsseldorf, MedalBronze | 2015 | Montreux, MedalBronze | 2017 | Tbilisi
    
    Q: In which year did Áron Szilágyi achieve his personal highest number of gold medal wins?
    
    A:  
    Let's first understand the problem, extract relevant variables and their corresponding numerals, and devise a plan. Then, let's carry out the plan, calculate intermediate results (pay attention to calculation and common sense), solve the problem step by step, and show the answer. We will clearly state the final answer using "Final Answer:", providing the answer as concisely as possible without unnecessary information.

    Variables:
    Gold medals:

    2007: 1 gold (World Championships - Team).

    2012: 1 gold (Olympic Games - Individual).

    2015: 1 gold (European Championships - Individual).

    2016: 1 gold (Olympic Games - Individual).

    2018: 1 gold (European Championships - Team).

    2020: 1 gold (Olympic Games - Individual).

    2022: 2 golds (World Championships - Individual; European Championships - Team).

    2023: 1 gold (World Championships - Team).

    2024: 1 gold (European Championships - Team).

    Plan:
    We can count the number of gold medals won in each year and find the year with the highest count.

    Calculation:
    From the table, 2022 has the highest number of gold medals with 2.

    Answer:
    Áron Szilágyi achieved his personal highest number of gold medal wins in the year 2022.
    
    Final Answer: 2022
        
    ========================
    Table : {context}

    Q : {question}
    
    LLM answer: """

