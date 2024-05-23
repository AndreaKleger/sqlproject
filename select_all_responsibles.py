from sqlite3 import * 
from prettytable import from_db_cursor 
 
# mit folgender Abfrage kann man die Personen sehen, denen Tasks zugewiesen werden können
# simpler select
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT * FROM people") 
    x= from_db_cursor(cursor)
print(x)