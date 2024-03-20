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
def insert(table, values):
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()
    formatted_values = []
    for val in values:
        if isinstance(val, str):
            formatted_values.append(f"'{val}'")
        else:
            formatted_values.append(str(val))
    cursor.execute(f'INSERT INTO {table} VALUES ({", ".join(formatted_values)})')
    con.commit()
    con.close()
