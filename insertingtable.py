import psycopg2
import dbENV.environment as environment

conn = psycopg2.connect(database = environment.DB_NAME, user = environment.DB_USER, password = environment.DB_PASS, host = environment.DB_HOST, port = environment.DB_PORT)

print("database connection good yo")    
cur = conn.cursor()
cur.execute("""
            
CREATE TABLE  Employee
(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL
)           
            
""")

conn.commit()
print("Table created successfully")