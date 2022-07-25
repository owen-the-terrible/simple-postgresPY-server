import psycopg2
import environment

conn = psycopg2.connect(database = environment.DB_NAME, user = environment.DB_USER, password = environment.DB_PASS, host = environment.DB_HOST, port = environment.DB_PORT)

print("database connection good yo")    
cur = conn.cursor()
cur.execute("SELECT ID, NAME, EMAIL FROM Employee")

rows = cur.fetchall()
print(rows, 'rows yo')

for data in rows:
    print("ID: " + str(data[0]))
    print("Name: " + data[1])
    print("Email: " + data[2])

print("data selected successfully")

conn.close()