import environment
import psycopg2


print(environment)
try: 
    conn = psycopg2.connect(database = environment.DB_NAME, user = environment.DB_USER, password = environment.DB_PASS, host = environment.DB_HOST, port =environment.DB_PORT)
    print("Database connected yo")
except:
    print("database not connected")