import mysql.connector

sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot"
)

my_cursor = sql.cursor()

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)