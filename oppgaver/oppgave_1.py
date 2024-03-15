import sqlite3

stol_id_counter = 1  # Initialize a counter for stol_id

def insert(table, values):
    global stol_id_counter  # Access the global counter
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()
    formatted_values = []
    for val in values:
        if isinstance(val, str):
            formatted_values.append(f"'{val}'")
        else:
            formatted_values.append(str(val))
    cursor.execute(f'INSERT INTO {table} VALUES ({", ".join(formatted_values)})')
    if table == 'Stol':  # Increment the counter only for Stol table
        stol_id_counter += 1
    con.commit()
    con.close()

insert('Teatersal', ('Hovedscenen',))
insert('Teatersal', ('Gamle scene',))

def insert_stoler_Hovedscenen(sal, rows, seats):
    global stol_id_counter
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()
    for row in range(1, rows + 1):
        for seat in range(1, seats + 1):
            stol_id = stol_id_counter
            insert('Stol', (stol_id, seat, row, sal, 0))
            stol_id_counter += 1
    con.close()

insert_stoler_Hovedscenen('Hovedscenen', 16, 28)

def insert_stoler_Parkett(sal, rows_parkett):
    global stol_id_counter
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()

    for row in range(1, rows_parkett + 1):
        if row in [1, 4, 5, 7]:
            seats = 18
        elif row == 2:
            seats = 16
        else:
            seats = 17
        for seat in range(1, seats + 1):
            stol_id = stol_id_counter
            insert('Stol', (stol_id, seat, row, sal + ': Parkett', 1))
            stol_id_counter += 1

    con.close()

def insert_stoler_Balkong(sal, rows_balkong):
    global stol_id_counter
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()

    for row in range(1, rows_balkong + 1):
        if row == 1:
            seats = 28
        elif row in [2, 3]:
            seats = 27
        else:
            seats = 17
        for seat in range(1, seats + 1):
            stol_id = stol_id_counter
            insert('Stol', (stol_id, seat, row, sal + ': Balkong', 2))
            stol_id_counter += 1

    con.close()

def insert_stoler_Galleri(sal, rows_galleri):
    global stol_id_counter
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()

    for row in range(1, rows_galleri + 1):
        if row == 1:
            seats = 33
        elif row == 2:
            seats = 18
        else:
            seats = 17
        for seat in range(1, seats + 1):
            stol_id = stol_id_counter
            insert('Stol', (stol_id, seat, row, sal + ': Galleri', 3))
            stol_id_counter += 1

    con.close()

insert_stoler_Parkett('Gamle scene', 10)
insert_stoler_Balkong('Gamle scene', 4)
insert_stoler_Galleri('Gamle scene', 3)


""" def insert_teaterstykker():
    teaterstykke_data = [('Kongsemnene', 'Hovedscenen', '19:00'), ('Størst av alt er kjærligheten', 'Gamle scene', '18:30')]
    for stykke, sal, tid in teaterstykke_data:
        insert('Teaterstykke', (stykke, sal, tid))

def insert_roller():
    rolle_data = [
        ('Håkon Håkonssønn', 1), ('Dagfinn Bonde', 1), ('Jatgeir Skald', 1), ('Sigrid', 1),
        ('Ingebjørg', 1), ('Guttorm Ingesson', 1), ('Skule jarl', 1), ('Inga fra Vartejg', 1),
        ('Paal Flida', 1), ('Fru Ragnhild', 1), ('Gregorius Jonssønn', 1), ('Margrete', 1),
        ('Biskop Nikolas', 1), ('Peter', 1)
    ]
    for rolle, navn in rolle_data:
        insert('Rolle', (None, rolle, navn))


def insert_skuespiller():
    skuespiller_data = [
        ('Arturo', 'Scotti'), ('Emil', 'Olafsson'), ('Emil', 'Olafsson'), ('Emma Caroline', 'Deichmann'),
        ('Emma Caroline', 'Deichmann'), (None, None), ('Hans Petter', 'Nilsen'), ('Ingunn Beate', 'Strige Øyen'),
        ('Isak Holmen', 'Sørensen'), ('Madeleine Brandtzæg', 'Nilsen'), ('Per Bogstad', 'Gulliksen'),
        ('Synnøve Fossum', 'Eriksen'), ('Thomas Jensen', 'Takyi'), ('Snorre Ryen', 'Tøndel')
    ]
    for fornavn, etternavn in skuespiller_data:
        insert('Skuespiller', (None, fornavn, etternavn))


insert_roller()
insert_skuespiller() """