import psycopg2

conn = None
cur = None

def db_conn():
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                    password="admin123", port=5432)
    
    return conn

db_conn()
