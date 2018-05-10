import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('CMPE131.db')
c = conn.cursor()

# print all the stuff from database
def read_from_db():
    c.execute("SELECT  * FROM  my_stock")
    for row in c.fetchall():
        print(row)

read_from_db()
c.close()
conn.close()
