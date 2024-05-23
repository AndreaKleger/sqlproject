from sqlite3 import * 
from prettytable import from_db_cursor 

# user input entgegennehmen
taskId = input("Geben Sie die Task-Id ein, bei der sie den Text verändern wollen:") 
text = input("Geben Sie den neuen Text ein:") 

# mit dieser Abfrage sehen wir den aktuellen Text
with connect("projectDB.db") as con: 
    cursor = con.cursor()  
    cursor.execute("SELECT * FROM tasks WHERE id = ?", taskId)
    x= from_db_cursor(cursor)
print(x)

# Text einer Task updaten
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    sql = "UPDATE tasks SET text = ? WHERE id = ?"
    args = (text, taskId)
    cursor.execute(sql, args) 

# mit dieser Abfrage sehen wir den aktualisierten Text
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT * FROM tasks WHERE id=?", taskId) 
    x= from_db_cursor(cursor)
print(x)