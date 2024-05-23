from sqlite3 import * 
from prettytable import from_db_cursor 

# mit folgender Abfrage kann man sehen, wer noch wieviele offene Tasks hat
# select mit inner join, where clause und count. Abfrage mit einem ForeignKey auf people
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT count(*) as numberOfTasks, firstname, lastname FROM tasks INNER JOIN people ON tasks.Responsible = people.Id WHERE status<4 GROUP BY responsible") 
    x= from_db_cursor(cursor)
print(x)


