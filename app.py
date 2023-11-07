import psycopg2
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                    password="admin123", port=5432)
    cur = conn.cursor()
    # return conn
    return cur
try:
    @app.route('/players', methods=['GET'])
    def players():
        # conn = db_conn()
        cur = db_conn()
        # cur = conn.cursor()
        query = "SELECT firstName, lastName FROM players"
        cur.execute(query)
        data = cur.fetchall()

        result = [{'firstName': row[0], 'lastName': row[1]} for row in data]
        return jsonify(result)


    @app.route('/games', methods=['GET'])
    def games():
        cur = db_conn()
        # cur = conn.cursor()
        query = '''select games.gameid, players.firstname, games.date,  games.num_played, games.num_win from games
                    join players
                    on games.player_id = players.playerid'''
        cur.execute(query)
        data = cur.fetchall()

        result = [{'games.gameid': row[0], 'players.firstname': row[1], 'games.num_played': row[2], 'games.num_win': row[3]} for row in data]
        return jsonify(result)

    if __name__ == '__main__':
        app.run(debug=True, port=8080)

except Exception as error:
    print (error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()