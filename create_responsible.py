from sqlite3 import * 
from prettytable import from_db_cursor 

# eine neue Person, die Tasks übernehmen kann, wird eingefügt
# die Id wird automatisch von der Datenbank vergeben, deswegen wird sie hier nicht gesetzt

# Es wird überprüft, ob dieser Name bereits existiert, damit es keine doppelten Einträge gibt
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    # check, ob Eintrag bereits existiert
    cursor.execute("SELECT * FROM people WHERE firstname='Lea' AND lastname='Herz'") 
    result = cursor.fetchone()
    if result == None:
        cursor.execute("INSERT INTO people (firstname,lastname) VALUES ('Lea', 'Herz')") 
    else:
        print('name already exists')
    
# mit dieser Abfrage sehen wir die People-Tabelle nach dem CREATE
with connect("projectDB.db") as con: 
    cursor = con.cursor() 
    cursor.execute("SELECT * FROM people") 
    x= from_db_cursor(cursor)
print(x)