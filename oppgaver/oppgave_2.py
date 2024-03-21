import os
import sqlite3
from utils import query, insert

insert('Kundeprofil', ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
       (12345678, 'standardbruker_fornavn', 'standardbruker_etternavn', '0010', 'Slottsplassen', 1, 'Ordinær'))

# insert('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', 12345678)) #2024-02-03
# insert('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', 12345678))
# insert('Billett', ('stolID', 'forestillingID', 'kjøpsID'), ('2024-01-01', '12:00', 12345678))
# def insert_solgte_stoler_hovedscenen():
#     lines = None
#     with open(os.path.join(os.path.dirname(__file__), '../filer/hovedscenen.txt'), 'r') as file:
#         lines = file.readlines()
#     stoler_fra_nummer_en = ''.join([rad.strip() for rad in lines[lines.index('Parkett\n') + 1:]][::-1])
#     solgte_stoler = [stolindex + 1 for stolindex, solgt in enumerate(stoler_fra_nummer_en) if solgt == '1']

    

# insert_solgte_stoler_hovedscenen()

# Anders sitt arbeid

import os
import sqlite3

def insert(table, values):
    con = sqlite3.connect('./database/database.db')
    cursor = con.cursor()
    formatted_values = []
    for val in values:
        if isinstance(val, str):
            formatted_values.append(f"'{val}'")
        elif val is None:
            formatted_values.append('NULL')
        else:
            formatted_values.append(str(val))
    query = f"INSERT INTO {table} VALUES ({', '.join(formatted_values)})"
    cursor.execute(query)
    con.commit()
    con.close()

def lese_sete_config_fra_fil(file_path):
    with open(file_path, 'r') as file:
        content = file.read().split('\n')
        dato = None
        # Extract date from the first line if present
        if "Dato" in content[0]:
            words = content[0].split()
            for word in words:
                if len(word) == 10 and word[4] == "-" and word[7] == "-":
                    dato = word
                    break
        sections = {}
        current_section = None
        current_config = []
        for line in content[1:]:
            if line in ['Galleri', 'Parkett', 'Balkong']:
                if current_section:
                    # Append the reversed configuration list
                    sections[current_section] = '\n'.join(current_config[::-1])
                    current_config = []
                current_section = line
            else:
                current_config.append(line)
        # Don't forget the last section
        if current_section:
            sections[current_section] = '\n'.join(current_config[::-1])
    return dato, sections

def parse_sete_config(date, section, seating_config):
    rows = seating_config.strip().split('\n')
    sold_seats = []
    for row_idx, row in enumerate(rows):
        for col_idx, seat in enumerate(row):
            if seat == '1':  # Sold seat
                sold_seats.append((date, section, row_idx + 1, col_idx + 1))
    return sold_seats

def insert_solgte_seter(sold_seats):
    for dato, section, row, column in sold_seats:
        # insert('Stol', [date, section, row, column])
        insert('BillettKjop', [None,  dato, "naa", "123123"])
        # insert('BillettKjop', ('dato', 'tid', 'mobilnummer'), (dato, '12:00', 12345678))
        # insert('Billett', ('stolID', 'forestillingID', 'kjøpsID'), (, , ))


def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            date, sections = lese_sete_config_fra_fil(file_path)
            for section, config in sections.items():
                sold_seats = parse_sete_config(date, section, config)
                insert_solgte_seter(sold_seats)
            print(f"Processed {filename}")

# Example usage
directory_path = "filer"
process_directory(directory_path)
