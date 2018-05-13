import sqlite3

conn = sqlite3.connect('CMPE131.db')  # connect to existing file
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS my_stock(ID REAL, Name TEXT, Price REAL, Quantity REAL)")

def read_from_db():  # print the entire list
    c.execute("SELECT  * FROM  my_stock")
    for row in c.fetchall():
        print(row)

read_from_db()
c.close()
conn.close()