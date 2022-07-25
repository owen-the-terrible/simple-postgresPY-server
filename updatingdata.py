import psycopg2
import dbENV.environment as environment

conn = psycopg2.connect(database = environment.DB_NAME, user = environment.DB_USER, password = environment.DB_PASS, host = environment.DB_HOST, port = environment.DB_PORT)

print("database connection good yo")    
cur = conn.cursor()
cur.execute("UPDATE Employee set EMAIL = 'update@gmail.com' WHERE ID = 1")
conn.commit()

print("data updated successfully")
print("Total rows affected " + str(cur.rowcount))