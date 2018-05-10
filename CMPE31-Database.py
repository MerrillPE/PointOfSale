import sqlite3 # use database

conn = sqlite3.connect('CMPE131.db')  # create a database file 
c = conn.cursor()   # a cursor is used for command things

# print all the stuff from the database you already made
def read_from_db():
    c.execute("SELECT  * FROM  my_stock")
    for row in c.fetchall():
        print(row)

read_from_db()
c.close()
conn.close()
