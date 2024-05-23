from sqlite3 import * 
from prettytable import from_db_cursor 
 
# mit folgender Abfrage kann man sehen, wer welche Tasks bis wann bearbeitet und was der jetztige Status ist
# select mit inner join. Abfrage mit zwei ForeignKeys auf zwei andere Tabellen (people und categories)
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT categorytext as Status, duedate, title, text, firstname, lastname FROM tasks INNER JOIN people ON tasks.Responsible = people.Id INNER JOIN categories ON tasks.status = categories.Id") 
    x= from_db_cursor(cursor)
print(x)




