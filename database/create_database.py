import sqlite3
import os

'''
Denne filen leser inn "CREATE TABLE"-setningene fra .sql filen, og oppretter tilsvarende, tomme tabeller i databasen.
'''

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../sql/gruppe_21_db1_sql_script.sql')

con = sqlite3.connect(f'{dirname}/database.db')

cur = con.cursor()

with open(filename, 'r') as sql_file:
    sql_commands = sql_file.read()
    cur.executescript(sql_commands)

con.commit()
con.close()
