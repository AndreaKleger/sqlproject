from sqlite3 import * 
from prettytable import from_db_cursor 

# user input entgegennehmen
taskId = input("Geben Sie die Task-Id ein, bei der sie den Status ändern wollen:") 
status = input("Geben Sie den neuen Status ein (als Zahl!!):") 

# mit dieser Abfrage sehen wir den aktuellen Status
with connect("projectDB.db") as con: 
    cursor = con.cursor()  
    cursor.execute("SELECT * FROM tasks WHERE id = ?", taskId)
    x= from_db_cursor(cursor)
print(x)

# status einer Task updaten
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    sql = "UPDATE tasks SET status = ? WHERE id = ?"
    args = (status, taskId)
    cursor.execute(sql, args) 

# mit dieser Abfrage sehen wir den aktualisierten Status
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT * FROM tasks WHERE id=?", taskId) 
    x= from_db_cursor(cursor)
print(x)