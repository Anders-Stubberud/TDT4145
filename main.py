import sqlite3
from oppgaver import *

while True:
    oppgave = int(input('''         
    Hvilke(n) oppgave ønsker du å utføre?
    Skriv:
    0 for å opprette databasen med startdata'en,
    [1, 2, 3, 4, 5, 6, 7] for individuelle oppgaver,
    8 for å kjøre alle oppgavene,
    9 for å slette databasen,
    eller 10 for å avslutte.            
    '''))


    if oppgave == 0:
        print('    Setter inn data fra SQL-filen...')
        conn = sqlite3.connect('teater.db')
        try:
            with open('schema.sql', 'r', encoding='utf-8') as f:
                schema_sql = f.read()
                conn.executescript(schema_sql)
            with open('insert-db.sql', 'r', encoding='utf-8') as f:
                insert_sql = f.read()
                conn.executescript(insert_sql)
            print("    Databasen har nå fått data.")
        except sqlite3.Error as e:
            print("Feil:", e)
        finally:
            conn.close()

    elif oppgave == 1:
        print('    Utfører oppgave 1: setter inn stoler i databasen...')
        oppgave_1.insert_stoler_Hovedscenen()
        oppgave_1.insert_stoler_Parkett('Gamle scene', 10)
        oppgave_1.insert_stoler_Balkong('Gamle scene', 4)
        oppgave_1.insert_stoler_Galleri('Gamle scene', 3)
        print('    Databasen har nå registrert stolene.')

    elif oppgave == 2:
        print('    Utfører oppgave 2: registrerer solgte stoler...')
        oppgave_2.insert_solgte_stoler_hovedscenen()
        oppgave_2.insert_solgte_stoler_gamle_scene()
        print('    De solgte stolene er nå registrert.')

    elif oppgave == 3:
        print('    Utfører oppgave 3: kjøper ni voksenbilletter')
        oppgave_3.kjøpe_ni_voksenbilletter()

    elif oppgave == 4:
        print('    Utfører oppgave 4: finner forestillinger på gitt dato, samt antall solgte billetter')
        oppgave_4.forestiller_på_dato()

    elif oppgave == 5:
        print('    Utfører oppgave 5: Finner skuespillere for ulike teaterstykker')
        oppgave_5.skuespillere_i_stykker()

    elif oppgave == 6:
        print('    Utfører oppgave 6: finner bestselgere')
        oppgave_6.print_bestselgere()

    elif oppgave == 7:
        print('    Utfører oppgave 7: finner skuespillere i samme akt')
        oppgave_7.spiller_i_samme_akt()

    elif oppgave == 8:
        print('    Utfører samtlige oppgaver...')
        conn = sqlite3.connect('teater.db')
        try:
            with open('schema.sql', 'r', encoding='utf-8') as f:
                schema_sql = f.read()
                conn.executescript(schema_sql)
            with open('insert-db.sql', 'r', encoding='utf-8') as f:
                insert_sql = f.read()
                conn.executescript(insert_sql)
            print("    Databasen har nå fått data.")
        except sqlite3.Error as e:
            print("Feil:", e)
        finally:
            conn.close()
        oppgave_1.insert_stoler_Hovedscenen()
        oppgave_1.insert_stoler_Parkett('Gamle scene', 10)
        oppgave_1.insert_stoler_Balkong('Gamle scene', 4)
        oppgave_1.insert_stoler_Galleri('Gamle scene', 3)
        oppgave_2.insert_solgte_stoler_hovedscenen()
        oppgave_2.insert_solgte_stoler_gamle_scene()
        oppgave_3.kjøpe_ni_voksenbilletter()
        oppgave_4.forestiller_på_dato()
        oppgave_5.skuespillere_i_stykker()
        oppgave_6.print_bestselgere()
        oppgave_7.spiller_i_samme_akt()

    elif oppgave == 9:
        print('    Tømmer databasen...')
        conn = sqlite3.connect('teater.db')
        try:
            with open('drop_tables.sql', 'r', encoding='utf-8') as f:
                schema_sql = f.read()
                conn.executescript(schema_sql)
        except sqlite3.Error as e:
            print("Feil:", e)
        finally:
            conn.close()
        print('    Databasen er nå tom.')

    else:
        break
