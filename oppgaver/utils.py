import os
import sqlite3


'''
Denne filen gir tilgang til databaseoperasjonene "query" og "insert", som henholdsvis leser av og setter inn data.
'''



'''
Leser ut og returnerer spesifisert data.
'''
def query(query):
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../teater.db'))
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
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../teater.db'))
    cursor = con.cursor()
    placeholders = ', '.join(['?' for _ in columns])
    cursor.execute(f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({placeholders})', values)
    con.commit()
    con.close()

def insert_return_rowID(table, columns, values):
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../teater.db'))
    cursor = con.cursor()
    placeholders = ', '.join(['?' for _ in columns])
    cursor.execute(f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({placeholders})', values)
    rowID = cursor.lastrowid
    con.commit()
    con.close()
    return rowID
