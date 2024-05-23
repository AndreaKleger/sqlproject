from sqlite3 import * 
from prettytable import from_db_cursor 


# ein neuer Task wird eingefügt
# die Id wird automatisch von der Datenbank vergeben, deswegen wird sie hier nicht gesetzt
# der Status wird von der Datenbank automatisch mit 1 ausgefüllt (default)

with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("INSERT INTO tasks (title,text, duedate,responsible ) VALUES ('Meetings', 'Meeting Schedule fürs Steering Committee aufsetzen, Einladungen versenden', '20240624', 3)") 

    
# mit dieser Abfrage sehen wir die neu erstellte task (WHERE mit dem gesetzten responsible)
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT * FROM tasks WHERE responsible=3") 
    x= from_db_cursor(cursor)
print(x)