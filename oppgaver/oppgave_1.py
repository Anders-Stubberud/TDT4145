from oppgaver.utils import insert

def insert_stoler_Hovedscenen():
    row = 1
    for seat in range(1, 505):
        if (466 < seat and seat < 471) or (494 < seat < 499):
            continue
        insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, 'Hovedscenen', 1))
        row = row + 1 if seat  % 28 == 0 else row

def insert_stoler_Parkett(sal, rows_parkett):
    for row in range(1, rows_parkett + 1):
        if row in [1, 4, 5, 7]:
            seats = 18
        elif row == 2:
            seats = 16
        elif row == 10:
            seats = 14
        else:
            seats = 17
        for seat in range(1, seats + 1):
            insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, sal, 1))

def insert_stoler_Balkong(sal, rows_balkong):
    for row in range(1, rows_balkong + 1):
        if row == 1:
            seats = 28
        elif row == 2:
            seats = 27
        elif row == 3:
            seats = 22
        else:
            seats = 17
        for seat in range(1, seats + 1):
            insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, sal, 2))

def insert_stoler_Galleri(sal, rows_galleri):
    for row in range(1, rows_galleri + 1):
        if row == 1:
            seats = 33
        elif row == 2:
            seats = 18
        else:
            seats = 17
        for seat in range(1, seats + 1):
            insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, sal, 3))

