import os
import sqlite3
from utils import query, insert

# insert('Kundeprofil', ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
#        (12345678, 'standardbruker_fornavn', 'standardbruker_etternavn', '0010', 'Slottsplassen', 1, 'Ordinær'))

insert('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', 12345678)) #2024-02-03
insert('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', 12345678))
insert('Billett', ('stolID', 'forestillingID', 'kjøpsID'), ('2024-01-01', '12:00', 12345678))
def insert_solgte_stoler_hovedscenen():
    lines = None
    with open(os.path.join(os.path.dirname(__file__), '../filer/hovedscenen.txt'), 'r') as file:
        lines = file.readlines()
    stoler_fra_nummer_en = ''.join([rad.strip() for rad in lines[lines.index('Parkett\n') + 1:]][::-1])
    solgte_stoler = [stolindex + 1 for stolindex, solgt in enumerate(stoler_fra_nummer_en) if solgt == '1']

    

insert_solgte_stoler_hovedscenen()

