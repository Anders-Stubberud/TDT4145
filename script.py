import sqlite3

con = sqlite3.connect('database.db')

cur = con.cursor()

with open('gruppe_21_db1_sql_script.sql', 'r') as sql_file:
    sql_commands = sql_file.read()
    cur.executescript(sql_commands)

con.commit()
con.close()
