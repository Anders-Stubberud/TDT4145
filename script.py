import sqlite3

'''
Denne filen gir tilgang til databaseoperasjonene "query" og "insert", som henholdsvis leser av og setter inn data.
'''



'''
Leser ut og returnerer spesifisert data.
'''
def query(table, select_statement="*", where_statement=None, group_by=None, having=None, order_by=None, join=None, distinct=False):
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()
    sql_query = f"SELECT {'' if not distinct else 'DISTINCT'} {select_statement} FROM {table}"
    if join:
        sql_query += f" {join}"
    if where_statement:
        sql_query += f" WHERE {where_statement}"
    if group_by:
        sql_query += f" GROUP BY {group_by}"
    if having:
        sql_query += f" HAVING {having}"
    if order_by:
        sql_query += f" ORDER BY {order_by}"
    result = cursor.execute(sql_query).fetchall()
    con.close()
    return result

'''
Setter inn data i databasen.

obs:
values oppgis som tuppel med attributter, eksempelvis values = ('Hovedscenen')
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

insert('Teatersal', ['testescene5'])

# for row in query('Teatersal'):
#     print(row)
