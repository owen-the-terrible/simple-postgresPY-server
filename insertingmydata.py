import psycopg2

DB_NAME = "fvhzkruo"
DB_USER = "fvhzkruo"
DB_PASS = "YdAcjDV7DqADZrZFy3Nh3OnWXiuVwMal"
DB_HOST = "heffalump.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

print("database connection good yo")    
cur = conn.cursor()
cur.execute("INSERT INTO Employee (ID, NAME, EMAIL) VALUES (3,'Nathan', 'robot.nerd@beep.boop')")
conn.commit()
print(" inserting data executed successfully")