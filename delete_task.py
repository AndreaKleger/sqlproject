from sqlite3 import * 
from prettytable import from_db_cursor 

# delete task
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("DELETE FROM tasks WHERE id=8") 

# mit dieser Abfrage sehen wir die tasks-Tabelle nach dem DELETE
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT * FROM tasks") 
    x= from_db_cursor(cursor)
print(x)