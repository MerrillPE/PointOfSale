import sqlite3 # use database

conn = sqlite3.connect('CMPE131.db')  # create a database file 
c = conn.cursor()   # a cursor is used for command things

# put item into the database (file)
#def data_entry():
#    c.execute("INSERT INTO my_stock VALUES (ID, 'A_item_name', price)")
#    conn.commit()  
#    c.close()
#    conn.close()
    
# print all the stuff from the database (you already made)
def read_from_db():
    c.execute("SELECT  * FROM  my_stock")  # select all items
#    c.execute("SELECT  * FROM  my_stock WHERE  value > 30")  # select items only price larger than 30
    for row in c.fetchall():
        print(row)

read_from_db()
c.close()
conn.close()
