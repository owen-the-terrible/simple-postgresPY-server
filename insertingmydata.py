import psycopg2
import dbENV.environment as environment

conn = psycopg2.connect(database = environment.DB_NAME, user = environment.DB_USER, password = environment.DB_PASS, host = environment.DB_HOST, port = environment.DB_PORT)

print("database connection good yo")    
cur = conn.cursor()
cur.execute("INSERT INTO Employee (ID, NAME, EMAIL) VALUES (1,'Owen', 'owen-the-terrible@stp.com')")
conn.commit()
print(" inserting data executed successfully")