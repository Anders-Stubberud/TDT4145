import sqlite3

'''
Denne filen leser inn "CREATE TABEL"-setningene fra .sql filen, og oppretter tilsvarende, tomme tabeller i databasen.
'''

con = sqlite3.connect('database.db')

cur = con.cursor()

with open('gruppe_21_db1_sql_script.sql', 'r') as sql_file:
    sql_commands = sql_file.read()
    cur.executescript(sql_commands)

con.commit()
con.close()
