import psycopg2
import utilities
import pandas as pd

conn = None
cur = None

def db_conn():
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                    password="admin123", port=5432)
    
    return conn


try:
    conn = db_conn()
    
    cur = conn.cursor()

    create_table_player = '''CREATE TABLE IF NOT EXISTS players (
                playerId SERIAL PRIMARY KEY,
                firstName VARCHAR(255) NOT NULL,
                lastName VARCHAR(255) NOT NULL
                )'''
    
    cur.execute(create_table_player)

    create_table_games = '''CREATE TABLE IF NOT EXISTS games (
        GameId SERIAL PRIMARY KEY,
        date DATE,
        player_id INT REFERENCES players (playerId),
        num_played INT,
        num_win INT
    )'''

    cur.execute(create_table_games)

    insert_into_players = 'INSERT INTO PLAYERS (firstName, lastName) VALUES (%s,%s)'
    insert_values = [('Ryan', 'Smith'), ('Jake', 'Paling'), ('Gopi', 'Sharma')]
    
    for i in insert_values:
        cur.execute(insert_into_players, i)

    df=pd.read_excel('TableTennisData.xlsx')
    
    existing_date_query = "SELECT date FROM games "
    cur.execute(existing_date_query)
    existing_date = set(str(row[0]) for row in cur.fetchall())

    for index, row in df.iterrows():
        if str(row['date']) not in existing_date:
            insert_query = "INSERT INTO GAMES (date, player_id, num_played, num_win) VALUES (%s, %s, %s,%s)"
            values = (row['date'], row['player_id'], row['num_played'],row['num_win'])

            cur.execute(insert_query, values)



    conn.commit()

except Exception as error:
    print (error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()