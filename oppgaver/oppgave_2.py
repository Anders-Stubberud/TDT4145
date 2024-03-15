import os
import sqlite3
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

def lese_sete_config_fra_fil(file_path):
    with open(file_path, 'r') as file:
        content = file.read().split('\n')
        # date = content[0].strip()
        if "Dato" in content[0]:
            print("kommer hit")
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
                    sections[current_section] = "".join(reversed(current_config))
                    current_config = []
                current_section = line
            else:
                current_config.append(line)
        
        # Don't forget the last section
        if current_section:
            sections[current_section] = "".join(reversed(current_config))

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
    insert('Stol', ["1", ])
    # for date, section, row, column in sold_seats:
    #     insert('Stol', [date, section, row, column])

# print(os.getcwd())
# print(os.path.exists("filer"))
# file_path = os.getcwd("filer/")
# for filer in file_path:
#     f = open(filer, "r")
#     print(f.read())
#     f.close()
file1 = "filer/gamle-scene.txt"
file2 = "filer/hovedscenen.txt"

print(lese_sete_config_fra_fil(file1))
print(lese_sete_config_fra_fil(file2))