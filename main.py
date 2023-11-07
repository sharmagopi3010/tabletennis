import psycopg2 #database adaptor
import pandas as pd #this helps to convert excel to python data and databases
# from sqlalchemy import create_engine # establish connection
from flask import Flask, jsonify

app = Flask(__name__)
conn = None
cur = None

try:
    query1 = "SELECT firstName, lastName FROM players"
    df1 = pd.read_sql_query(query1, conn)

    print (df1)
    
    if __name__ == '__main__':
        app.run(debug=True, port=8080)
    
except Exception as error:
    print (error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()