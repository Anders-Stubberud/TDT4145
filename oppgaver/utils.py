import sqlite3

'''
Denne filen gir tilgang til databaseoperasjonene "query" og "insert", som henholdsvis leser av og setter inn data.
'''



'''
Leser ut og returnerer spesifisert data.
'''
def query(query):
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()   
    result = cursor.execute(query)
    result = result.fetchall()
    con.close()
    return result

'''
Setter inn data i databasen.

obs:
values oppgis som array med attributter, eksempelvis values = ['Hovedscenen']
'''

def insert(table, columns, values):
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()
    placeholders = ', '.join(['?' for _ in columns])
    cursor.execute(f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({placeholders})', values)
    con.commit()
    con.close()

# insert('Teatersal', ['salnavn'], ['Gamle scenek'])

# insert('Rolle', ('navn', 'navnPaStykke'), ('verdi1', 'verdi2'))









